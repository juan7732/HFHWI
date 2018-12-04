from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template('WIMS/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('WIMS/login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def donor_signup(request):
    template = loader.get_template('WIMS/donorsignup.html')
    context = {}
    return HttpResponse(template.render(context, request))


def member_signup(request):
    template = loader.get_template('WIMS/membersignup.html')
    context = {}
    return HttpResponse(template.render(context, request))


def member_dashboard(request):
    template = loader.get_template('WIMS/memberdashboard.html')
    context = {}
    return HttpResponse(template.render(context, request))


def project_page(request, project_id):
    template = loader.get_template('WIMS/projectpage.html')
    context = {}
    return HttpResponse(template.render(context, request))
