from .models import Blog
from .forms import ProjectForm
from operator import attrgetter
from django.shortcuts import render, redirect

# Define the landing page
def home(request):
    # Get a list of blogs.
    all_blogs = Blog.objects.all()
    # sort the blogs with respect to date
    blogs = sorted(all_blogs, key=attrgetter('time'), reverse=True)
    # Handle project form submission
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page after saving the form
            return redirect('project_success')
    else:
        form = ProjectForm()
    return render(request, 'main_app/home.html', {'form':form, "blogs":blogs})

# View for individual blog page.
def blog_detail(request, blog_id):
    # Get the specific blog post using the blog_id
    blog = Blog.objects.get(id=blog_id)
    return render(request, "main_app/blog_detail.html", {"blog":blog})

# Page to list all blogs ever written.
def blogs_page(request):
    # Get the list of all blogs
    blogs = Blog.objects.all()
    return render(request, "main_app/list_of_blogs.html", {'blogs':blogs})

# Define the success page after a user submits the get quote form.
def success(request):
    return render(request, 'main_app/success.html')

# Page for projects case study.
def case_study_page(request):
    return render(request, 'main_app/case_study_page.html')