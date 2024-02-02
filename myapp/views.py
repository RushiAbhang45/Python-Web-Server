from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import FormSubmission

# Create your views here.



def index(request):
    current_datetime = datetime.now()
    context = {
        'current_datetime': current_datetime
    }
    return render(request, 'index.html', context)

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        # Process the form data (e.g., save to database)
        # For now, just print the data to console
        print("Name:", name)
        print("Email:", email)
        return HttpResponseRedirect(reverse('index'))  # Redirect to home page
    else:
        # If the form is accessed via GET method, redirect to home page
        return HttpResponseRedirect(reverse('index'))
    
def submissions(request):
    submissions = FormSubmission.objects.all()
    return render(request, 'submissions.html', {'submissions': submissions})
