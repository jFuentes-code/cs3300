from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import ProjectForm, PortfolioForm


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
        # Call the base implementation first to get the context for the current portfolio
        context = super(PortfolioDetailView, self).get_context_data(**kwargs)
        # Get projects that use the current portfolio and add it to the context
        context['projects'] = Project.objects.filter(portfolio=context['portfolio'])
        return context

class ProjectListView(generic.ListView):
    model = Project
class ProjectDetailView(generic.DetailView):
    model = Project


def createProject(request, portfolio_id):

    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == 'POST':
        
        form = ProjectForm(request.POST)

        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)

    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)

def updateProject(request, portfolio_id, id):
    #sets portfolio based on portfolio id of project in url
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    #sets the project based on the id from the url
    project = Project.objects.get(id = id)
    #generates a project form using the current instance of the project
    form = ProjectForm(instance = project)
    
    #check the method is as expected
    if request.method == 'POST':
        
        #generates a project form using the current instance of the project and trys to post the updated information
        form = ProjectForm(request.POST, instance = project)

        #if all required values are set then continue
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)

    #pass in the form as a form in the dictionary so that we can use it in the project_form template
    context = {'form': form}
    #go to project_form template with this information
    return render(request, 'portfolio_app/project_form.html', context)

#method to delete a project in a portfolio
def deleteProject(request, portfolio_id, id):
    #sets portfolio based on portfolio id of project in url
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    #sets the project based on the id from the url
    project = Project.objects.get(id = id)

    #check the method is as expected
    if request.method == 'POST':
        #delete the project using funtion delete()
        project.delete()
        # Redirect back to the portfolio detail page
        return redirect('portfolio-detail', portfolio_id)

    #pass in the project as an item in the dictionary because thats what we called it in the delete template
    context = {'item': project}
    #go to delete template with this information
    return render(request, 'portfolio_app/delete.html', context)

def updatePortfolio(request,  id):
    #sets portfolio based on the portfolio id in url
    portfolio = Portfolio.objects.get(pk=id)
    #generates a portfolio form using the current instance of the portfolio
    form = PortfolioForm(instance = portfolio)
    
    #check the method is as expected
    if request.method == 'POST':
        
        #generates a portfolio form using the current instance of the portfolio and trys to post the updated information
        form = PortfolioForm(request.POST, instance = portfolio)

        #if all required values are set then continue
        if form.is_valid():
            # Save the form without committing to the database
            student = form.save(commit=False)
            # Set the portfolio relationship
            student.portfolio = portfolio
            student.save()

            # Redirect back to the portfolio detail page
            return redirect('students')
    #pass in the form as a form in the dictionary so that we can use it in the portfolio_form template
    context = {'form': form}
    #go to portfolio_form template with this information
    return render(request, 'portfolio_app/portfolio_form.html', context)