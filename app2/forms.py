from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S','Stripe'),
    ('P','PayPal')
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(required=True,widget=forms.TextInput(attrs={
        'placeholder':'1234 Main St',
        'class': 'form-control',
        'id': 'address',
    }))
    apartment_address = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'placeholder':'Apartment or suite',
        'class': 'form-control',
        'id': 'address2',
    }))
    state = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    country = CountryField(blank_label='select country').formfield(widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100',
        'id': 'country'
    }))
    zip = forms.IntegerField(required=True, max_value=999999, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'zip',
    }))
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_options = forms.ChoiceField(widget=forms.RadioSelect(),choices=PAYMENT_CHOICES)