from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
#from .forms import ProjectForm, PortfolioForm
from django.contrib import messages

# Create your views here.
def index(request): 
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    #Render the HTML template index.html with the data in the context variable
    return render( request, 'portfolio_app/index.html',
                   {'student_active_portfolios':student_active_portfolios})

#Update the views to use the generic list and details views
class StudentListView(generic.ListView):
    model = Student
class StudentDetailView(generic.DetailView):
    model = Student

class PortfolioListView(generic.ListView):
    model = Portfolio
class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    #def get_context_data to send additional variables to template
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PortfolioDetailView, self).get_context_data(**kwargs)

        
        # Get projects that use the current portfolio and add it to the context
        context['projects'] = Project.objects.filter(portfolio=context['portfolio'])
        return context

class ProjectListView(generic.ListView):
    model = Project
class ProjectDetailView(generic.DetailView):
    model = Project