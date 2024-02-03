from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField,PasswordResetForm,SetPasswordForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer,NGO,Country,UserType,CustomUser
from paypal.standard.forms import PayPalPaymentsForm

class NGO_RegistrationForm(forms.ModelForm):
    name = forms.CharField(label='NGO Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_person = forms.CharField(label='Contact Person',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone_number = forms.IntegerField(label='Phone Number',widget=forms.NumberInput(attrs={'class':'form-control'}))
    address = forms.Textarea()
    countries = Country.objects.all()
    country = forms.ModelChoiceField(
        queryset=countries,
        empty_label='Select a country',  # Optional: Add an empty label
        widget=forms.Select(attrs={'class': 'custom-select-class'}),
    )
    mission_statement = forms.Textarea()
    website = forms.CharField(label='NGO Website',widget=forms.TextInput(attrs={'class':'form-control'}))    
    registration_proof = forms.ImageField()
    class Meta:
        model=NGO
        fields = ['name','contact_person','email','phone_number','address','country','mission_statement','website','registration_proof']
        # 'name',
        # labels = {'email':'Email'}
        # widgets = {'name':forms.TextInput(attrs={'class':'form-control'})}

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    # country = forms.CharField(requited=True,widget=forms.) 
    countries = Country.objects.all()
    country = forms.ModelChoiceField(
        queryset=countries,
        empty_label='Select a country',  # Optional: Add an empty label
        widget=forms.Select(attrs={'class': 'custom-select-class'}),
    )
    user_types = UserType.objects.all()
    user_type = forms.ModelChoiceField(
        queryset=user_types,
        empty_label='User type',  # Optional: Add an empty label
        widget=forms.Select(attrs={'class': 'custom-select-class'}),
    )
    class Meta:
        model=CustomUser
        fields = ['username','user_type','email','country','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}


# Ignore this or now
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        # fields = '__all__'
        fields = ['phone','address','country']
        # 'ac_number', 'ifsc_code'
        widgets = {'phone':forms.NumberInput(attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}),
        'country':forms.TextInput(attrs={'class':'form-control'}),
        # 'ac_number':forms.NumberInput(attrs={'class':'form-control'}),
        # 'ifsc_code':forms.TextInput(attrs={'class':'form-control'})
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Enter registered email"),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
    )

class DonationForm(forms.Form):
    amount=forms.DecimalField(label='Donation Amount')
