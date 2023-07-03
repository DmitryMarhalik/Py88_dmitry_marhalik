from django.forms import ModelForm, TextInput
from .models import Auto


class AutoForm(ModelForm):
    class Meta:
        model = Auto
        # fields = "__all__"
        fields = ('vin_code', 'auto_model')
        widgets = {
            'vin_code': TextInput(attrs={'class': 'input vin_code',
                                         'placeholder': 'VIN'})
        }
