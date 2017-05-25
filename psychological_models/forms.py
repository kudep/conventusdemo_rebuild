from django import forms
from .models import *


class BasisOfPsychotypeForm(forms.ModelForm):

    class Meta:
        model = BasisOfPsychotype
        exclude = []


