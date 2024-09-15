# payment/forms.py

from django import forms
from .models import BillingAddress

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['address', 'city', 'state', 'zip_code', 'country']
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Street Address'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'placeholder': 'State'}),
            'zip_code': forms.TextInput(attrs={'placeholder': 'Zip Code'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
        }

