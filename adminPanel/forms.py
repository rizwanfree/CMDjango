# forms.py
from django import forms
from .models import Item, Port


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
            'custom_duty_rate': forms.NumberInput(attrs={'class': 'form-control text-end'}),
            'additional_custom_duty_type': forms.Select(attrs={'class': 'form-select'}),
            'additional_custom_duty_rate': forms.NumberInput(attrs={'class': 'form-control text-end'}),
            'regulatory_duty_type': forms.Select(attrs={'class': 'form-select'}),
            'regulatory_duty_rate': forms.NumberInput(attrs={'class': 'form-control text-end'}),

            'sales_tax_rate': forms.NumberInput(attrs={'class': 'form-control text-end'}),
            'additional_sales_tax_rate': forms.NumberInput(attrs={'class': 'form-control text-end'}),
            'income_tax_rate': forms.NumberInput(attrs={'class': 'form-control text-end'}),
            'psqc_rate': forms.NumberInput(attrs={'class': 'form-control text-end'}),
            'wharfage_rate': forms.NumberInput(attrs={'class': 'form-control text-end'}),
        }


class PortForm(forms.ModelForm):
    class Meta:
        model = Port
        fields = '__all__'
        widgets = {
            'port_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
        }