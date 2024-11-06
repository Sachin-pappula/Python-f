from django import forms
from .models import students


class studentForm(forms.ModelForm):
    class Meta:
        model = students
        fields = ['SID', 'NAME', 'BRANCH', 'SUBJECT']
