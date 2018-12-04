from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    template = loader.get_template('WIMS/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def donor_signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now ready to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    template = loader.get_template('WIMS/donorsignup.html')
    context = {
        'title': 'Donor',
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def member_signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now ready to log in!!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    template = loader.get_template('WIMS/membersignup.html')
    context = {
        'title': 'Volunteer',
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def member_dashboard(request):
    template = loader.get_template('WIMS/memberdashboard.html')
    context = {
        'type': 'Proposed',
    }
    return HttpResponse(template.render(context, request))


@login_required
def donor_dashboard(request):
    template = loader.get_template('WIMS/donordashboard.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required
def project_page(request, project_id):
    template = loader.get_template('WIMS/projectpage.html')
    context = {}
    return HttpResponse(template.render(context, request))
