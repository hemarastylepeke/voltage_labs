from .models import Blog
from .forms import ProjectForm
from operator import attrgetter
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string

def test_html_for_mail(request):
    return render(request, 'main_app/email_template.html') # This fnction should be removed after the test.



# Success page after submitting the form
def success_url(request):
    # Check if the project was submitted successfully
    if not request.session.get('project_submitted'):
        
        # If not, redirect to a different URL or display an error message
        return redirect('home') 

    # Clear the session flag to prevent accessing the success page again
    del request.session['project_submitted']

    # Render the success page
    return render(request, 'main_app/success.html')

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
            instance = form.save()

            # Send email to my inbox
            email_subject = 'New project submission'
            email_message = f'''
                A new project has been submitted:
                Email: {instance.email}
                First Name: {instance.first_name}
                Last Name: {instance.last_name}
                Phone: {instance.phone}
                Company: {instance.company}
                Business Address: {instance.business_address}
                Project Description: {instance.project_description}
            '''
            send_mail(
                email_subject,
                email_message,
                settings.EMAIL_HOST_USER,
                [settings.YOUR_INBOX_EMAIL],
                fail_silently=False,
            )

            # Send project submission success email to the customer
            customer_subject = 'Project Submission Confirmation'
            customer_message = render_to_string('main_app/email_template.html', {'instance': instance})
            customer_message_plain = strip_tags(customer_message)
            send_mail(
                customer_subject,
                customer_message_plain,
                settings.EMAIL_HOST_USER,
                [instance.email],
                html_message=customer_message,
                fail_silently=False,
            )

            # Redirect the user to a different URL
            return redirect('success_url')
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

# Page for projects case study.
def case_study_page(request):
    return render(request, 'main_app/case_study_page.html')