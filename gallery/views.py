from django.shortcuts import render, redirect
from .forms import AddCarForm
from .models import Car

def home(request):
    context = {
        'cars': Car.objects.all()
    }
    return render(request, 'gallery/home.html', context)

def addwheel(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('gallery-home')
        
    else:
            form = AddCarForm()
    return render(request, 'gallery/add_wheel.html', {'form': form})

def about(request):
    return render(request, 'gallery/about.html')


