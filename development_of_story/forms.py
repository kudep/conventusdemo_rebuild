from django import forms
from .models import *


class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        exclude = ['likes']
        widgets = {'bases': forms.CheckboxSelectMultiple}


class SceneForm(forms.ModelForm):

    class Meta:
        model = Scene
        exclude = ['story', 'likes']


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        exclude = ['story', 'scene']


class PsychotypeCharacteristicForm(forms.ModelForm):

    class Meta:
        model = PsychotypeCharacteristic
        exclude = ['basis', 'answer']


