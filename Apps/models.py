from django.db import models

# Create your models here.
class Education(models.Model):
    education_id = models.AutoField(primary_key=True)
    institution_name = models.CharField(max_length=200,null=False)
    course = models.CharField(max_length=500,null=False)
    passout_date = models.DateField(auto_now=False, auto_now_add=False,null=False)

    def __str__(self):
        return self.institution_name    

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200,null=False)
    project_description = models.TextField(null=False)
    project_duration = models.CharField(max_length=200,null=False)
    start_date = models.DateField(auto_now=False, auto_now_add=False,null=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False,null=False)
    website = models.URLField(max_length=500,null=False)

    def __str__(self):
        return self.project_name    