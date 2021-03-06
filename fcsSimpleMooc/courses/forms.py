'''

forms for the courses' related instances

    . ContactCourse
        . send_mail
    
    . CommentForm
        . Meta
        
'''
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from fcsSimpleMooc.core.mail import send_mail_template
from .models import Comment
from logging import PlaceHolder

class ContactCourse(forms.Form):

    name = forms.CharField(label = 'Name', max_length=100,
                           widget= forms.TextInput(attrs = {'placeholder':' Please, enter your name...'}))
    email = forms.EmailField(label = 'E-mail',
                             widget= forms.TextInput(attrs = {'placeholder':' and your e-mail...'}))
    message = forms.CharField(label = 'Message/Question', 
                              widget = forms.Textarea(attrs = {'placeholder':' and, finally, enter your message/question here.'}))
    
    def send_mail(self, course):
        subject = '%s Course Information' % course
        # message = 'Name: %(name)s;E-mail: %(email)s;%(message)s'
        context = {'name': self.cleaned_data['name'],
                   'email': self.cleaned_data['email'],
                   'message': self.cleaned_data['message'],}
        # message = message % context
        #
        template_name = 'courses/contact_email.html'
        #
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])
#                   message, 
#                   settings.DEFAULT_FROM_EMAIL, 
#                   [settings.CONTACT_EMAIL])
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']
############################################################
##################        End         ######################
############################################################