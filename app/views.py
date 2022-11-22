from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .forms import ToDoProjectForm,LoginForm,UserForm
from .models import ToDoProject
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# from django.

# Create your views here. 
def index(req):
    form = ToDoProjectForm()
    userform = UserForm()
    login_form = LoginForm
    if req.user.is_authenticated:
        user = req.user
        to_do_list = ToDoProject.objects.filter(user=user).filter(complete = False)
        completed_list = ToDoProject.objects.filter(user=user).filter(complete = True)
    else:
        to_do_list = []
        completed_list = []
        user = None
    rendered_form = form.render("app/form_snippet.html")
    rendered_userform = userform.render('app/userform_snippet.html')
    # print(to_do_list)
    context = {
        'user': user,
        'form':rendered_form,
        'to_do_list': to_do_list,
        'signup_form':rendered_userform,
        'login_form':login_form,
        'completed_list':completed_list
    }
    # print(context)
    return render(req,'app/home.html',context)


@login_required(login_url='/login')
def add(req):
    if req.user :
        user = req.user
        print(user)
        if req.method == 'POST':
            form = ToDoProjectForm(req.POST)
            # form.user = req.user
            # print(form)
            if form.is_valid():
                print(req.user,req.user.id)
                task = form.save(commit=False)
                task.user = req.user
                task.save()
                messages.success(req,'Happy to complete your '+str.upper(task.project_name)+' project on time'.format(task.project_name))
            else:
                messages.info(req,'form is not seen as valid')
                return redirect('/')
    
    return redirect('/')

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_user(req):
    if req.method == 'POST':
        
        name = req.POST['your_name']
        password = req.POST['your_password']
        user = authenticate(req,username = name,password =password)
        print(user,name,password)
        if user is not None:
            login(req,user)
            print('logged In',name)
            messages.success(req,'Successful Login for '+name )
            return redirect('/')
        else:
            messages.add_message(req,40,'Invalid Credentials')
            return redirect('/')
    else:
        view = 'loginview'
        # return JsonResponse({'view':'loginview'})
        return redirect('/')

@login_required(login_url='/login')
def logoutuser(req):
    logout(req)
    return redirect('/')

def signup(req):
    if req.method == 'POST':
        contact_form = UserForm(req.POST)
        # print(contact_form)
        if contact_form.is_valid():
            print(contact_form)
            user = contact_form.cleaned_data.get('username')
            contact_form.save()
            logout(req)
            messages.success(req,'Thank You... Successfully made an Account')
            return redirect('/')
        else:
            messages.error(req,'Please submit your datas as unique')
            return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='/login')
def delete(req,id):
    todo = ToDoProject.objects.get(pk = id)
    # print(str(todo))
    user = req.user
    messages.warning(req,str(todo)+' has deleted successfully')
    todo.delete()
    # todo.save()
    return redirect('/')

@login_required(login_url='/login')
def complete(req,id):
    todo = ToDoProject.objects.get(pk= id)
    print(todo)
    todo.complete = True
    todo.save()
    return redirect('/')

@login_required(login_url='/login')
def update(req,id):
    if req.method == 'POST':
        form = ToDoProjectForm(req.POST)
        if form.is_valid():
            project = ToDoProject.objects.get(pk = id)
            project.project_name = form.cleaned_data.get('project_name')
            project.deadline = form.cleaned_data.get('deadline')
            project.timeline = form.cleaned_data.get('timeline')
            project.save()
            task = project
            messages.success(req,'Happy to complete your '+str.upper(task.project_name)+' project on time'.format(task.project_name))
        else:
            messages.error(req,'Could not update data! Please enter valid Data')
        return redirect('/')
    else:
        project = ToDoProject.objects.get(pk = id)
        form = ToDoProjectForm()
        rendered_form = form.render("app/form_snippet.html")
        name = project.project_name
        deadline = project.deadline
        timeline = project.timeline
        return JsonResponse({'name':name,'deadline':deadline,'timeline':timeline})