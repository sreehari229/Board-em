# Generated by Django 4.1.1 on 2022-10-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intendance', '0004_rename_created_by_notificationuser_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationuser',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]