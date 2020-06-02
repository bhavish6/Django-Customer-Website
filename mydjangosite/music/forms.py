from django.forms import ModelForm
from .models import *


class orderForm(ModelForm):
    class Meta:
        model = order
        fields = '__all__'

