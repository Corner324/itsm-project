install_dep:
	echo Installing dependencies for the frontend
	cd itsm_frontend && pnpm install
	echo Installing dependencies for the backend
	cd itsm_backend && poetry install

run_back: 
	echo Running backend
	cd itsm_backend && poetry run python manage.py runserver
run_front: 
	echo Running frontend
	cd itsm_frontend && pnpm run serve
