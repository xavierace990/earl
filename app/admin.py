from django.contrib import admin
from .models import BlogPost
# Register your models here.
from .models import Result
from.models import Contact_information
from .models import Student_signup
admin.site.register(Result)
admin.site.register(BlogPost)
admin.site.register(Contact_information)
admin.site.register(Student_signup)