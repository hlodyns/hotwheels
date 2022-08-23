from django.shortcuts import render, redirect
from .forms import AddCarForm
from .models import Car
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'cars': Car.objects.all()
    }
    return render(request, 'gallery/home.html', context)

@login_required
def addwheel(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'A new car has been added to your collection.')
            return redirect ('gallery-home')
        
    else:
            form = AddCarForm()
    return render(request, 'gallery/add_wheel.html', {'form': form})

def about(request):
    return render(request, 'gallery/about.html')




