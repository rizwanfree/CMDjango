# forms.py
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'custom_duty_type': forms.Select(choices=Item.DUTY_TYPE_CHOICE),
            'additional_custom_duty_type': forms.Select(choices=Item.DUTY_TYPE_CHOICE),
            'regulatory_duty_type': forms.Select(choices=Item.DUTY_TYPE_CHOICE),

            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'hs_code': forms.TextInput(attrs={'class': 'form-control'}),
            'custom_duty_type': forms.Select(attrs={'class': 'form-select'}),
            'custom_duty_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'additional_custom_duty_type': forms.Select(attrs={'class': 'form-select'}),
            'additional_custom_duty_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'regulatory_duty_type': forms.Select(attrs={'class': 'form-select'}),
            'regulatory_duty_rate': forms.NumberInput(attrs={'class': 'form-control'}),

            'sales_tax_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'additional_sales_tax_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'income_tax_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'psqc_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'wharfage_rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }
