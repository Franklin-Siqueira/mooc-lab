from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Course, Enrollment

def enrollment_required(view_func):
    
    def _wrapper(request, *args, **kwargs):
        
        shortcut = kwargs['shortcut']
        course = get_object_or_404(Course, shortcut = shortcut)
        has_permission = request.user.is_staff
        
        if not has_permission:
            try:
                enrollment = Enrollment.objects.get(user = request.user, course = course)
            except Enrollment.DoesNotExist:
                message = "Sorry! You don't have permission to access this page"
            else:
                if enrollment.is_approved():
                    has_permission = True
                else:
                    message = 'Pending subscription! Enrollment is being processed!'
                    
        if not has_permission:
            messages.error(request, message)
            return redirect('accounts:dashboard')
        request.course = course
        
        return view_func(request, *args, **kwargs)
    
    return _wrapper
