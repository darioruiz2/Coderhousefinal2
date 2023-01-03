from django import forms
from django.contrib.auth.models import User

class MensajeForm(forms.Form):
    para = forms.ModelChoiceField(User.objects.all())
    mensaje = forms.CharField(max_length=500)
    