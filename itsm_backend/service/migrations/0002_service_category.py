# Generated by Django 5.1.3 on 2024-12-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
    ]