from django.forms import ModelForm
from .models import profile
class MainForm(ModelForm):
    class Meta:
        model = profile
        fields = '__all__'