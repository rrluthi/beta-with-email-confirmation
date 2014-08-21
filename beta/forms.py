from django import forms
from django.conf import settings
from django.core.exceptions import *

from beta.models import BetaSignup


class BetaSignupForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BetaSignupForm, self).__init__(*args, **kwargs) 
        self.capture_first = getattr(settings, 'BETA_CAPTURE_FIRST', False)
        self.capture_both = getattr(settings, 'BETA_CAPTURE_BOTH', False) 

        if self.capture_first:
            self.fields.pop('last_name')
            self.fields['first_name'].required = True 

        elif not self.capture_both:
            self.fields.pop('first_name')
            self.fields.pop('last_name')
        else:
            self.fields['first_name'].required = True 
            self.fields['last_name'].required = True

    email = forms.EmailField(
        min_length=5,
        max_length=75,
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email Address'}
        )
    )

    class Meta:
        model = BetaSignup
        exclude = ('contacted', 'registered', 'created', 'token')

