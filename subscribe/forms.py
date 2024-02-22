from django import forms

from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'


# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError("Invalid Last name")
#     return value

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100, required= False, label="Enter first name", help_text= "Enter your first name")
#     last_name = forms.CharField(max_length=100, validators=[validate_comma])
#     email = forms.EmailField(max_length=100)
