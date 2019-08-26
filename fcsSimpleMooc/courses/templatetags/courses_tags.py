'''

    . courses_tags
        .. my_courses(user)
        .. load_my_courses(user)

'''
from django.template import Library

register = Library()

from fcsSimpleMooc.courses.models import Enrollment

@register.inclusion_tag('courses/templatetags/my_courses.html')
def my_courses(user):
    
    enrollments = Enrollment.objects.filter(user = user)
    context = {'enrollments': enrollments}
    
    return context

@register.simple_tag
def load_my_courses(user):
    
    return Enrollment.objects.filter(user = user)