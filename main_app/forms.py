from django import forms
from .models import Comment
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['email', 
                  'confirm_email', 
                  'first_name', 
                  'last_name', 
                  'phone', 
                  'company', 
                  'business_address', 
                  'project_description',
                  'project_file']
        widgets = {
            'project_description': forms.Textarea(attrs={'rows': 5}),  # Set the number of rows for the textarea
        }

class CommentForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Comment
        fields = ['email', 'body']
