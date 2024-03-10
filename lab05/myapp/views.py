from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PersonForm

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __str__(self):
        return self.username

people = []

def add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            people.append(Person(username, password))
            return redirect('list_people')  # Redirect to the list view
    else:
        form = PersonForm()
    return render(request, 'myapp/add.html', {'form': form})

def list_people(request):
    return render(request, 'myapp/list_people.html', {'people': people})
