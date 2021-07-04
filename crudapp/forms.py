from django import forms
from .models import crudapp

class PostForm(forms.ModelForm):
    class Meta:
        model = crudapp
        fields = ['title', 'body', 'pub_date']
        widgets = {
            'pub_date' : forms.DateInput(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'date'
                }
            )
        }