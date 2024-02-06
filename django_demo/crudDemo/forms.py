from django import forms
from django.forms import ModelForm
from .models import myItem

class myItemForm(ModelForm):
    class Meta:
        model = myItem
        fields = "__all__"
        
class myItemDeleteForm(ModelForm):
    class Meta:
        model = myItem
        fields = ('title',)