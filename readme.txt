beta-with-email-confirmation
===========

``beta-with-email-confirmation`` is a fork of django-beta, a simple application to help you
capture pre-beta interest with your sites. This fork adds an email confirmation step.

By default ``django-beta`` only captures a user's email address, however you
can alternately set one of these two configuration options:

BETA_CAPTURE_FIRST = True, will use a form and require the user to enter their
first name and email address.

BETA_CAPTURE_BOTH = True, will use a form and require the user enter their
first name, last name, and email address.

Installation
============
For emailing this uses postmarkapp, so pip install python-postmark.
Sign up for postmarkapp and get a key and verify your sender's email.
Add POSTMARK_API_KEY and POSTMARK_SENDER to your settings.py

Add ``beta`` to your ``INSTALLED_APPS`` and run syncdb.

Add the following to your urls.py:

    url(r'^beta/', include('beta.urls')),

Using the example templates provided in the code, create your customized beta signup templates.

Managers
--------

The ``BetaSignup`` model has the following manager method to help out:

BetaSignup.objects.contacted()
BetaSignup.objects.not_contacted()
BetaSignup.objects.registered()
BetaSignup.objects.not_registered()

Side Effects
------------

``beta-with-email-confirmation`` listens for a signal on User creation and marks the
corresponding BetaSignup entry as 'registered'.


TODO
----
* Expire unverified emails
* Admin views to show beta registrations over time
* Management commands to simplify emailing the interested users
