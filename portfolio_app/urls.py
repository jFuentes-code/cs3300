from django_project.urls import path
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empy to represent based path to app
#views.index is the function defined in views.py
#name='index' parameter is to dynamically create url
#example in html <a href="{% url 'index' %}">Home</a>
path('', views.index, name='index'),
#Update urls.py to include path to list and detail views
path('students/', views.StudentListView.as_view(), name= 'students'),
path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
path('portfolios/', views.PortfolioListView.as_view(), name= 'portfolio'),
path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
path('projects/', views.ProjectListView.as_view(), name= 'project'),
path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),

path('portfolio/<int:portfolio_id>/create_project/', views.createProject, name='create_project'),
path('portfolio/<int:portfolio_id>/update_project/<int:id>', views.updateProject, name='update_project'),
#url for deletion that takes in portfolio id and project id
path('portfolio/<int:portfolio_id>/delete_project/<int:id>', views.deleteProject, name='delete_project'),

]
