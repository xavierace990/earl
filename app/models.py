from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
# models.py

class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    result_picture = models.ImageField(upload_to='result_pictures')

    def __str__(self):
        return f'{self.student.username} - Result'


#blogpost
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='uploads')
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})
    
#contact-information
class Contact_information(models.Model):
    name=models.CharField(max_length=100)
    email = models.EmailField(
    max_length=255,  # Maximum length of the email address (adjust as needed)
    unique=True,     # Ensure email addresses are unique in the database
    blank=False,     # Email is required (set to True if it's optional)
    null=False,      # Email is required (set to True if it can be null)
    help_text="Please enter a valid email address",  # Help text for the field
)
    message = models.TextField(null=True)   
    
class Student_signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name    