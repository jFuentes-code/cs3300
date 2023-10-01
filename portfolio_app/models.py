from django.db import models
from django.urls import reverse

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    contact_email= models.CharField(max_length=200)
    is_active= models.BooleanField(default = False)
    about = models.TextField(blank = True)

    #Define default String to return the title for representing the Model object.
    def __str__(self):
        return self.title
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse("portfolio_detail",  args=[str(self.id)])
    


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank = False)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, default = None)

    #Define default String to return the title for representing the Model object.
    def __str__(self):
        return self.title
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse("project_detail",  args=[str(self.id)])

class Student(models.Model):
    #list of majors to choose from
    major = (
        ('CSCI-BS', 'BS in Computer Science'),
        ('CPEN-BS', 'BS in Computer Engineering'),
        ('BIGD-BI', 'BI in Game Design and Development'),
        ('BICS-BI', 'BI in Computer Science'),
        ('BISC-BI', 'BI in Computer Security'),
        ('CSCI-BA', 'BA in Computer Science'),
        ('DASE-BS', 'BS in Data Analytics and Systems Engineering')
    )

    name = models.CharField(max_length=200)
    email = models.CharField("UCCS Email", max_length=200)
    major = models.CharField(max_length=200, choices=major, blank = False)

    #Define default String to return the name for representing the Model object.
    def __str__(self):
        return self.name
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse("student-detail", args=[str(self.id)])
    
    portfolio = models.OneToOneField(Portfolio, null =True, on_delete=models.CASCADE, unique=True)
    