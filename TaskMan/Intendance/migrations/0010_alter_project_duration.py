# Generated by Django 4.1.1 on 2022-10-23 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intendance', '0009_rename_user_discussions_posted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
    ]