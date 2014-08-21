import os
import random
import string
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import Context
from django.template.loader import get_template
from postmark import PMMail
from beta.forms import BetaSignupForm
from beta.models import BetaSignup


class Signup(generic.CreateView):
    """ View to handle beta signup """
    template_name = 'signup.html'
    form_class = BetaSignupForm
    model = BetaSignup

    @staticmethod
    def send_email_confirmation(email_addr, token):
        subject = "Caseworx Beta Confirmation"
        to = email_addr

        html_email = get_template('email_confirmation.html')

        d = Context({'confirmation_code': token})
        body = html_email.render(d)

        message = PMMail(api_key=os.environ.get('POSTMARK_API_KEY'),
                         subject=subject,
                         sender=os.environ.get('POSTMARK_SENDER'),
                         to=to,
                         html_body=body,
                         tag="hello")
        message.send()

    def get_success_url(self):
        return reverse('thanks')

    def form_valid(self, form):
        confirm_token = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(33))
        self.send_email_confirmation(form.cleaned_data['email'], confirm_token)
        form.instance.token = confirm_token
        form.instance.contacted = True
        form.save()
        return super(Signup, self).form_valid(form)


class Thanks(generic.TemplateView):
    """ Confirmation Page """
    template_name = 'thanks.html'


def confirmation_view(request):
    """ Confirmation Page """
    token = request.GET.get('token')
    if token:
        user = BetaSignup.objects.get(token=token)
        user.registered = True
        user.save()

    return render(request, 'confirmation.html')





