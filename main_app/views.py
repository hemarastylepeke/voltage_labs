from django.shortcuts import render, redirect
from .forms import ProjectForm

# Define the landing page
def home(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_success') # Redirect to success page after saving the form
    else:
        form = ProjectForm()
    return render(request, 'main_app/home.html', {'form':form})

# Define the success page after a user submits the get quote form.
def success(request):
    return render(request, 'main_app/success.html')
