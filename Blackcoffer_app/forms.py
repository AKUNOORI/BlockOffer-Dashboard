from django import forms
from .models import JsonFile

class JsonUploadForm(forms.ModelForm):
     class Meta:
          model = JsonFile
          fields = ['file']