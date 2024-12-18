import pytest
from rest_framework.test import APIClient
from main.models import CustomUser
from incident.models import Incident
from service.models import BusinessService, TechnicalService
import uuid


@pytest.fixture
def api_client():
    """Создание клиента API для тестов."""
    return APIClient()


@pytest.fixture
def create_user():
    """Создание тестового пользователя."""
    def _create_user(username, password, role):
        unique_username = f"{username}_{uuid.uuid4().hex[:8]}"
        user = CustomUser.objects.create_user(username=unique_username, password=password)  
        user.role = role 
        user.save()
        return user
    return _create_user


@pytest.fixture
def authenticated_client(api_client, create_user):
    """Создание аутентифицированного клиента с ролью сотрудника."""
    user = create_user("employee", "password123", "employee")
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def create_incident(create_user):
    """Создание инцидента для тестов."""
    user = create_user("employee", "password123", "employee")
    return Incident.objects.create(
        type="incident",
        topic="Тестовая тема",
        description="Тестовое описание",
        status="new",
        created_by=user,
    )


@pytest.fixture
def create_business_service():
    """Создание бизнес-услуги для тестов."""
    def _create_service(category, name, description, status):
        return BusinessService.objects.create(
            category=category,
            name=name,
            description=description,
            status=status,
        )
    return _create_service


@pytest.fixture
def create_technical_service():
    """Создание технической услуги для тестов."""
    def _create_service(category, name, configuration_items, status):
        return TechnicalService.objects.create(
            category=category,
            name=name,
            configuration_items=configuration_items,
            status=status,
        )
    return _create_service


@pytest.mark.django_db
def test_create_business_service(authenticated_client):
    """Тест на создание бизнес-услуги."""
    response = authenticated_client.post("/api/services/business/", {
        "category": "Бизнес-услуги",
        "name": "Бизнес-услуга 1",
        "description": "Описание бизнес-услуги 1",
        "status": "active"
    })
    assert response.status_code == 201
    assert response.data["name"] == "Бизнес-услуга 1"


@pytest.mark.django_db
def test_create_technical_service(authenticated_client):
    """Тест на создание технической услуги."""
    response = authenticated_client.post("/api/services/technical/", {
        "category": "Технические услуги",
        "name": "Техническая услуга 1",
        "configuration_items": "Конфигурация 1, Конфигурация 2",
        "status": "active"
    })
    assert response.status_code == 201
    assert response.data["name"] == "Техническая услуга 1"


@pytest.mark.django_db
def test_get_all_services(authenticated_client, create_business_service, create_technical_service):
    """Тест на получение всех услуг."""
    create_business_service("Категория 1", "Бизнес-услуга", "Описание", "active")
    create_technical_service("Категория 2", "Тех.услуга", "Конфигурация 1, Конфигурация 2", "active")
    
    response_business = authenticated_client.get("/api/services/business/")
    assert response_business.status_code == 200
    assert len(response_business.data) == 1

    response_technical = authenticated_client.get("/api/services/technical/")
    assert response_technical.status_code == 200
    assert len(response_technical.data) == 1


@pytest.mark.django_db
def test_create_incident(authenticated_client):
    """Тест на создание инцидента."""
    response = authenticated_client.post("/api/incidents/create/", {
        "type": "incident",
        "topic": "Тестовая тема",
        "description": "Описание тестового инцидента",
        "status": "new"
    })
    assert response.status_code == 201
    assert response.data["topic"] == "Тестовая тема"


@pytest.mark.django_db
def test_get_user_incidents(authenticated_client, create_incident):
    """Тест на получение инцидентов пользователя."""
    response = authenticated_client.get("/api/incidents/my/")
    assert response.status_code == 200
    assert len(response.data) == 0


@pytest.mark.django_db
def test_get_incident_detail(authenticated_client, create_incident):
    """Тест на просмотр конкретного инцидента."""
    incident = create_incident
    response = authenticated_client.get(f"/api/incidents/{incident.id}/")
    assert response.status_code == 200
    assert response.data["topic"] == "Тестовая тема"


@pytest.mark.django_db
def test_update_incident_status(authenticated_client, create_incident):
    """Тест на обновление статуса инцидента."""
    incident = create_incident
    response = authenticated_client.patch(f"/api/incidents/{incident.id}/", {
        "status": "in_progress"
    })
    assert response.status_code == 200
    assert response.data["status"] == "in_progress"


@pytest.mark.django_db
def test_send_message(authenticated_client, create_user):
    """Тест на отправку сообщения сотрудником."""
    admin_user = create_user("admin", "password123", "admin")
    response = authenticated_client.post("/api/messaging/", {
        "content": "Тестовое сообщение",
        "receiver": admin_user.id
    })
    assert response.status_code == 201
    assert response.data["content"] == "Тестовое сообщение"


@pytest.mark.django_db
def test_get_user_messages(authenticated_client):
    """Тест на получение сообщений пользователя."""
    response = authenticated_client.get("/api/messaging/")
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_create_business_service_without_required_fields(authenticated_client):
    """Тест на создание бизнес-услуги без обязательных полей."""
    response = authenticated_client.post("/api/services/business/", {
        "category": "",
        "name": "",
        "description": "",
        "status": "active"
    })
    assert response.status_code == 400
    assert "category" in response.data
    assert "name" in response.data
    assert "description" in response.data


@pytest.mark.django_db
def test_update_technical_service(authenticated_client, create_technical_service):
    """Тест на обновление данных технической услуги."""
    service = create_technical_service("Техническая категория", "Техническая услуга 2", "Конфигурация 3, Конфигурация 4", "active")
    
    response = authenticated_client.patch(f"/api/services/technical/{service.id}/", {
        "name": "Обновлённая тех. услуга",
        "configuration_items": "Обновленная конфигурация 1, Конфигурация 2",
        "status": "inactive"
    })
    
    assert response.status_code == 200
    assert response.data["name"] == "Обновлённая тех. услуга"
    assert response.data["configuration_items"] == "Обновленная конфигурация 1, Конфигурация 2"
    assert response.data["status"] == "inactive"

