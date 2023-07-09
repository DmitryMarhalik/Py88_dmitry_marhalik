from django.forms import ModelForm, TextInput, CharField, ChoiceField, Select, ModelChoiceField
from .models import User, Auto, AutoModel, Brand


class AutoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['auto_model'].empty_label = 'choice auto->'

    class Meta:
        model = Auto
        fields = ('vin_code', 'auto_model')
        widgets = {
            'vin_code': TextInput(attrs={'class': 'input vin_code',
                                         'placeholder': 'VIN'}),
            'auto_model': Select(attrs={'class': 'input auto_model_input select',
                                        'placeholder': 'auto model'})}



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            'name': TextInput(attrs={'class': 'input '}),
            'phone': TextInput(attrs={'class': 'input '})}


class BookTakeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['auto_model'].empty_label = 'select auto->'
        self.fields['user'].empty_label = 'select user->'

    class Meta:
        model = Auto
        fields = "__all__"
        widgets = {
            'vin_code': TextInput(attrs={'class': 'input'}),
            'user': Select(attrs={'class': 'input'}),
            'status': Select(attrs={'class': 'input'}),
            'auto_model': Select(attrs={'class': 'input'})}
