'''

forms for the forum's related instances

    . ReplyForm
        . Meta:
'''
from django import forms
#
from .models import Reply

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ['reply']
