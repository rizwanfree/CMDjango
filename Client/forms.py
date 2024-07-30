from django import forms
from .models import Client, City

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'client_name', 'contact_person', 'email', 'phone_number', 
            'mobile_number', 'address', 'city', 'client_type', 'gst', 
            'ntn', 'director_name', 'nic', 'soap_manufacturer', 'director_address'
        ]
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'city': forms.Select(attrs={'class': 'form-select'}),
            'client_type': forms.Select(choices=Client.CLIENT_TYPE_CHOICES, attrs={'class': 'form-select'}),
            'gst': forms.TextInput(attrs={'class': 'form-control'}),
            'ntn': forms.TextInput(attrs={'class': 'form-control'}),
            'director_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nic': forms.TextInput(attrs={'class': 'form-control'}),
            'soap_manufacturer': forms.CheckboxInput(attrs={'class': 'form-check-input', }),
            'director_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
        }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        # Customize form fields here if needed
        self.fields['city'].queryset = City.objects.all()