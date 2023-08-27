from django.forms import ModelForm
from .models import Image, UserInformation


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['im']


class UserInformationForm(ModelForm):
    class Meta:
        model = UserInformation
        fields = ['id_in_socials', 'socials']
