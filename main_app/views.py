from operator import attrgetter
from django.conf import settings
from .models import Blog, Comment
from django.core.mail import send_mail
from django.utils.html import strip_tags
from .forms import ProjectForm, CommentForm
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404, redirect


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
    all_blogs = Blog.objects.all()
    blogs = sorted(all_blogs, key=attrgetter('time'), reverse=True)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            instance = form.save()

            # Send email to your inbox
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
            request.session['project_submitted'] = True

            return redirect('success_url')
    else:
        form = ProjectForm()
    return render(request, 'main_app/home.html', {'form': form, "blogs": blogs})


# View for individual blog page.
def blog_detail(request, blog_id):
    # Get the specific blog post using the blog_id
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter(blog=blog)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()

            # Send email to my inbox about new comment
            email_subject = 'New comment has been posted'
            email_message = f'''
                A new comment has been submitted:
                Email: {comment.email}
                Comment: {comment.body}
            '''
            send_mail(
                email_subject,
                email_message,
                settings.EMAIL_HOST_USER,
                [settings.YOUR_INBOX_EMAIL],
                fail_silently=False,
            )
            return redirect('blog_detail', blog_id=blog_id)
    else:
        form = CommentForm()
    return render(request, 'main_app/blog_detail.html', {'blog': blog, 'comments': comments, 'form': form})

# Page to list all blogs ever written.
def blogs_page(request):
    # Get the list of all blogs
    blogs = Blog.objects.all()
    return render(request, "main_app/list_of_blogs.html", {'blogs':blogs})

# Page for projects case study.
def case_study_page(request):
    return render(request, 'main_app/case_study_page.html')

# Page for Terms and Condictions
def terms_and_conditions(request):
    return render(request, 'main_app/terms_of_conditions.html')

def privacy_policy(request):
    return render(request, 'main_app/privacy_policy.html')