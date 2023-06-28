from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

# Generate a list to categorize the blog posts.
blog_category = (
    ("Tutorial", "Tutorial"),
    ("Article", "Article"),
)

# import the custom user model from settings
User = get_user_model()

# model for creating customer quote.
class Project(models.Model):
    email = models.EmailField(max_length=255)
    confirm_email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=255)
    business_address = models.CharField(max_length=255)
    project_description = models.TextField()
    project_file = models.FileField(upload_to='project_files/', null=True, blank=True, validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])])

    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Model for a blog.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=blog_category, default="Tutorial")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
    
# Model to handle blog comments.
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    email = models.EmailField()
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on '{self.blog.title}' by {self.email}"