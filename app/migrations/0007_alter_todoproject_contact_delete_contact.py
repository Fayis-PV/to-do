# Generated by Django 4.1.2 on 2022-11-07 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_alter_contact_options_alter_contact_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoproject',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
