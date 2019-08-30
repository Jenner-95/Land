from django.shortcuts import render, HttpResponse
from users.models import User
from django.shortcuts import HttpResponseRedirect, reverse


# Create your views here.

def register_user_form(request):
    if request.method == 'POST':
        new_user = User(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            telephone=request.POST['telephone'],
            email=request.POST['email'],
            permissions=request.POST['permissions'],
            photo=request.FILES['photo'],
        )
        new_user.save()

        return HttpResponseRedirect(reverse('users:login'))
    elif request.method == 'GET':
        template = 'users/register.html'
        return render(request, template)
    return HttpResponse('Error: method not allowed.')


def login_user_form(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'], permissions=request.POST['permissions'])
        except User.DoesNotExist:
            return HttpResponse('User does not exist.')

        return HttpResponseRedirect(reverse('estate:estate_detail', kwargs={'user_id': user.id}))
    elif request.method == 'GET':
        template = 'login.html'
        return render(request, template)
    return HttpResponse('Error: method not allowed.')

