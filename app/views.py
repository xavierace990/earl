# Create your views here.
from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import BlogPost
from .models import Contact_information
from django.shortcuts import render,redirect
from .models import Result
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Result
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .forms import UserLoginForm
from .models import Student_signup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')  # Redirect to the results page after login
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    # Get the logged-in user
    user = request.user
    
    # Try to fetch the corresponding result for the logged-in user
    try:
        result = Result.objects.get(student=user)
        result_picture = result.result_picture
    except Result.DoesNotExist:
        result_picture = None
    
    return render(request, 'profile.html', {'result_picture': result_picture})

def form(request):
    return render(request, 'form.html')   
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'post': post})
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        obj = Contact_information(name=name, email=email, message=message)
        obj.save()
        print(f"the name is {name}, email is {email}, message is {message}")
        return redirect('success')  # Redirect to the success page upon successful submission

    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        # Do something with the form data, such as saving it to a database
        obj = Student_signup(name=name, email=email, phone=phone)
        obj.save()
        # For demonstration purposes, let's just print the data
        print(f"Name: {name}, Email: {email}, Phone: {phone}")
        
        # Optionally, you can return an HTTP response indicating success
        return redirect('success')
    else:
        # Handle GET requests if needed
        return render(request, 'signup.html')  
def success(request):
    return render(request, 'success.html')  

def blog(request):
    # Retrieve all posts
    posts = BlogPost.objects.order_by('-published_date')

    # Set the number of posts per page
    posts_per_page = 9

    # Paginate the posts
    paginator = Paginator(posts, posts_per_page)

    # Get the current page number from the URL parameters
    page_number = request.GET.get('page')

    try:
        # Get the posts for the requested page
        paginated_posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {'posts': paginated_posts})