from django import forms





class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')


class RegisterForm(forms.Form):
    school_name = forms.CharField(label='School Name')
    school_email = forms.EmailField(label='School Email')
    school_phone_number = forms.CharField(label='School Phone No.', widget=forms.NumberInput(), min_length=10, max_length=10)
    city = forms.CharField(label='City')
    country = forms.CharField(label='Country')
    school_address = forms.CharField(label='School Address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), min_length=8)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(), min_length=8)


    def clean(self):
        data = super().clean()
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError("Passwords don't match")

        return data