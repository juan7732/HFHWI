from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, CreateItemForm, MakeDonationForm
from django.contrib.auth.decorators import login_required
from .models import Project, ProjectMembers, Donation

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
def member_dashboard_active(request):
    template = loader.get_template('WIMS/activeprojectdashboard.html')
    projects = Project.objects.raw('SELECT * FROM wims_Project WHERE ProjectState=2')
    context = {
        'type': 'Active',
        'projects': projects
    }
    return HttpResponse(template.render(context, request))


@login_required
def member_dashboard_completed(request):
    template = loader.get_template('WIMS/completedprojectdashboard.html')
    projects = Project.objects.raw('SELECT * FROM wims_Project WHERE ProjectState=3')
    context = {
        'type': 'Completed',
        'projects': projects
    }
    return HttpResponse(template.render(context, request))


@login_required
def member_dashboard_proposed(request):
    template = loader.get_template('WIMS/proposedprojectdashboard.html')
    projects = Project.objects.raw('SELECT * FROM wims_Project WHERE ProjectState=1')
    context = {
        'type': 'Proposed',
        'projects': projects
    }
    return HttpResponse(template.render(context, request))


@login_required
def member_dashboard_search(request, searchTerm):
    template = loader.get_template('WIMS/searchprojectdashboard.html')
    projects = Project.objects.raw("SELECT * FROM wims_Project WHERE Name like '%" + searchTerm + "%'")
    context = {
        'type': 'Results',
        'projects':projects
    }
    return HttpResponse(template.render(context, request))


@login_required
def donor_dashboard(request):
    template = loader.get_template('WIMS/donationwall.html')
    current_user = request.user
    donations = Donation.objects.filter(DonorID=current_user)
    context = {
        'donations': donations,
    }
    return HttpResponse(template.render(context, request))


@login_required
def make_donation(request):
    if request.method == 'POST':
        form = CreateItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('make_donation_two')
    else:
        form = CreateItemForm()
    template = loader.get_template('WIMS/makedonation.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def make_donation_two(request):
    if request.method == 'POST':
        form = MakeDonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor_dashboard')
    else:
        form = MakeDonationForm()
    template = loader.get_template('WIMS/makedonation2.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))


@login_required
def project_page(request, project_id):
    template = loader.get_template('WIMS/projectpage.html')
    project = Project.objects.get(pk=project_id)
    context = {
        'project': project,
    }
    return HttpResponse(template.render(context, request))
