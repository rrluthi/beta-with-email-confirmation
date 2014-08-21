from django.conf.urls import *

from beta.views import Signup, confirmation_view, Thanks

urlpatterns = patterns('',
    url(regex='^$', view=Signup.as_view(), name='beta_signup',),
    url(r'^signup/confirmed/$', confirmation_view,),
    url(regex='^signup/thanks/$', view=Thanks.as_view(), name='thanks',),
)
