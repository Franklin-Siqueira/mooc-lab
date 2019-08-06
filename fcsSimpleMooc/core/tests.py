'''

Testing for the URLs

. HomeViewTest
    .. test_home_status_code
    .. test_home_template_used

run:

$ python manage.py test

'''
from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
#
from fcsSimpleMooc.core import views


class HomeViewTest(TestCase):

    def test_home_status_code(self):
        #
        client = Client()
        #
        response = client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_template_used(self):
        
        client = Client()
        #
        response = client.get(reverse('core:home'))
        # 
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')
#########################################################
##########                END                ############
#########################################################
