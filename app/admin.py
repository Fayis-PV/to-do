from django.contrib import admin

# Register your models here.
from .models import ToDoProject

admin.site.register([ToDoProject])