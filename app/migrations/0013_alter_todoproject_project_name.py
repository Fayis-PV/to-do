# Generated by Django 4.1.2 on 2022-11-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_todoproject_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoproject',
            name='project_name',
            field=models.CharField(max_length=50),
        ),
    ]
