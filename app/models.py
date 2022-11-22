from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class ContactManager(BaseUserManager):
#     use_in_migrations: True 
       
#     @classmethod
#     def create_user(cls,self,username,email,password,**extra_fields):
#         if username is None:
#             raise ValueError(('User Name is not available'))

#         email = self.normalize_email(email)
#         user = self.model(email,**extra_fields)
#         user.set_password(password)
#         user.save(using = self.db)
#         return user

#     def create_super_user(self,username,email,password,**extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_active',True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(('User is not a menmber of staff'))
        
#         user = self.create_user(self,username,email,password,**extra_fields)
#         return user

# class Contact(AbstractUser):
#     username = models.CharField( max_length=50,unique= True,blank=True,null=True)
#     email = models.EmailField(blank=True,null=True)
#     phone_number = models.IntegerField(blank=True,null=True)
#     password = models.CharField(max_length = 15,blank=True,null=True)
#     login_date = models.DateTimeField(auto_now_add = True,blank=True,null=True)

#     def __str__(self):
#         return self.username

#     objects = ContactManager





class ToDoProject(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,blank=True,null=True)
    project_name = models.CharField(max_length = 50)
    deadline = models.DateField(blank=True,null=True)
    timeline = models.TimeField(blank=True,null=True)
    complete = models.BooleanField(default = False)

    def __str__(self):
        return self.project_name

    def auto_user(req,self):
        if req.user.is_authenticated:
            self.user = req.user

    