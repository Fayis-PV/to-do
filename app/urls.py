from django.urls import path
from . import views

app_name='todo'
urlpatterns = [
    path('',views.index,name = 'home'),
    path('add',views.add, name = 'add'),
    path('login',views.login_user, name = 'login'),
    path('logout',views.logoutuser,name='logout'),
    path('signup',views.signup, name = 'signup'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('complete/<int:id>',views.complete,name='complete'),
    path('update/<int:id>',views.update,name='update'),
]