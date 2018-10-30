from django.shortcuts import render, redirect
from time import gmtime, strftime
from django.contrib import messages
from .models import *

def index(request):
    print('index method')
    context = {
        'all_users' : User.objects.all()
    }
    return render(request, 'restful_app/index.html', context)

def new(request):
    print('new method')
    return render(request, 'restful_app/new.html')

# def create(request):
    # print('create method')
    # user = User.objects.create(
    # first_name = request.POST['first_name'],
    # last_name = request.POST['last_name'],
    # email = request.POST['email']
    # )
    # return redirect('/')

def create(request):
    print('create method')
    # errors = User.objects.basic_validator(request.POST)
    # if len(errors):
    #     print("IF_CREATE")
    #     for key, error in errors.items():
    #         messages.error(request, error, messages=messages)
    #     print("IF WORKS!")
    #     return redirect('/new')
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        print("IF_CREATE")
        for key, value in errors.items():
            messages.error(request, value)
        print("IF WORKS!")
        return redirect('/new')
    else:
        print("ELSE_CREATE")
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email']
            )
        return redirect('/')

def show(request, user_id):
    print('show method')
    context = {
        'user' : User.objects.get(id=user_id)
    }

    return render(request, 'restful_app/show.html', context)

def edit(request, user_id):
    print('edit method')
    print(user_id)
    context = {
        'user' : User.objects.get(id=user_id)
    }
    return render(request, 'restful_app/edit.html', context)

# def update(request, user_id):
    # print(request.POST)
    # user = User.objects.get(id=request.POST['user_id'])
    # user.first_name = request.POST['first_name']
    # user.last_name = request.POST['last_name']
    # user.email = request.POST['email']
    # user.save()
    # return redirect('/')

def update(request, user_id):
    print('update method')
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        print("IF_UPDATE")
        for key, value in errors.items():
            messages.error(request, value)
        print("IF UPDATE WORKS!")
        uid = '/users/'+str(user_id)+'/edit'
        return redirect(uid)
        # or return redirect('/users/'+str(user_id)+'/edit')
    else:
        print("ELSE_UPDATE")
        user = User.objects.get(id=user_id)
        user.id = request.POST['user_id']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        messages.success(request,"User successfully updated")
        return redirect('/')

def destroy(request, user_id):
    print('destroy method')
    User.objects.get(id=user_id).delete()
    return redirect('/')

