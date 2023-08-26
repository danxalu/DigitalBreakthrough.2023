from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image
from .forms import ImageForm
from PIL import Image


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance
            print(img_obj)
            return redirect('index')

        return render(request, 'index.html', {'form': form})

    form = ImageForm()
    return render(request, 'index.html', {'form': form})
