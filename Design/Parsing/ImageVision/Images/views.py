from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image
from .forms import ImageForm, UserInformationForm
from PIL import Image


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UserInformationForm(request.POST)

        if form.is_valid():
            form.save()
            user_id = form.cleaned_data["id_in_socials"]
            user_socials = form.cleaned_data["socials"]
            return redirect('index')

        return render(request, 'index.html', {'form': form})

    form = UserInformationForm()
    return render(request, 'index.html', {'form': form})
