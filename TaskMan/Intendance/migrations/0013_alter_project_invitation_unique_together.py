# Generated by Django 4.1.1 on 2022-10-24 06:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Intendance', '0012_alter_project_invitation_created_date_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='project_invitation',
            unique_together={('project', 'receiver')},
        ),
    ]
