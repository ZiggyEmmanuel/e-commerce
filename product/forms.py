# product/forms.py

from django import forms
from .models import Review

class ProductFilterForm(forms.Form):
    
    min_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False, label='Min Price')
    max_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False, label='Max Price')
    discount = forms.BooleanField(required=False, label='Only Discounts')
    sort_by = forms.ChoiceField(choices=[
        ('price', 'Price (Low to High)'),
        ('-price', 'Price (High to Low)'),
        ('name', 'Name (A to Z)'),
        ('-name', 'Name (Z to A)')
    ], required=False, label='Sort By')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, i) for i in range(6)]),
            'comment': forms.Textarea(attrs={'rows': 4}),
        }
