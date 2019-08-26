'''

. ContactCourseTestCase

    .. setUp(self)
    .. tearDown(self)
    .. test_contact_form_error(self)

run:

    $ python manage.py test

'''
from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.conf import settings
#
from fcsSimpleMooc.courses.models import Course

class ContactCourseTestCase(TestCase):

    def setUp(self):
        # create new course instance
        self.course = Course.objects.create(name = 'Django', shortcut = 'django')

    def tearDown(self):
        # delete course instance
        self.course.delete()

    def test_contact_form_error(self):
        # 
        data = {'name': 'John Doe', 'email': '', 'message': ''}
        client = Client()
        path = reverse('courses:details', args = [self.course.shortcut])
        response = client.post(path, data)
        self.assertFormError(response, 'form', 'email', 'This field is required.')
        self.assertFormError(response, 'form', 'message', 'This field is required.')

    def test_contact_form_success(self):
        
        data = {'name': 'John Doe', 'email': 'admin@admin.com', 'message': 'Hi!!!'}
        client = Client()
        path = reverse('courses:details', args = [self.course.shortcut])
        response = client.post(path, data)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [settings.CONTACT_EMAIL])
#########################################################
##########                END                ############
#########################################################