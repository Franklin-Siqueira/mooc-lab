'''

Views for the courses' related instances

. index
. details
. enrollment
. undo_enrollment
. announcements
. show_announcement
. lesson
. lessons
. material

'''
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
#
from .decorators import enrollment_required
from .forms import ContactCourse, send_mail, CommentForm
from .models import Course, Enrollment, Announcement, Lesson, Material

# Create your views here.
def index(request):
    
    courseList = Course.objects.all()
    template_name = 'courses/index.html'
    context = {'courseList': courseList, "courses_page": "active"} #, 'enrollments': Enrollment.objects.filter(user = request.user)}
    
    return render(request, template_name, context)
#
@login_required
def FontTest(request):
    
    template_name = 'courses/fontTest.html'
    context = {"courses_page": "active"}
    
    return render(request, template_name, context)
#
def details(request, shortcut):
    # get Course by shortcut  or returns page not found
    courseName = get_object_or_404(Course, shortcut = shortcut)
    #
    context = {}
    # maybe a ternary?
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            #
            form.send_mail(courseName)
            #
            form = ContactCourse()
    else:
        form = ContactCourse()  
    
    template_name = 'courses/details.html'
    context = {'courseName': courseName, 'form': form}
    
    return render(request, template_name, context)
#
@login_required
def enrollment(request, shortcut):
    #
    MESSAGE_SUCCESS = 'Success!'
    MESSAGE_ENROLLED = "Hey! You're enrolled in this course, already!"
    #
    course = get_object_or_404(Course, shortcut = shortcut)
    enrollment, created = Enrollment.objects.get_or_create(user = request.user, course = course)
    #
    # checks for creation and student enrollment and proper message to base.html
    if created:
        # enrollment.active()
        messages.success(request, MESSAGE_SUCCESS)
    else:
        messages.info(request, MESSAGE_ENROLLED)

    return redirect('accounts:dashboard')
#
@login_required
def undo_enrollment(request, shortcut):
    
    course = get_object_or_404(Course, shortcut = shortcut)
    enrollment = get_object_or_404(Enrollment, user=request.user, course = course)
    
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, 'Enrollment cancelled! Hope to see you here again. Thank you!')
        return redirect('accounts:dashboard')
    
    template = 'courses/undo_enrollment.html'
    context = {'enrollment': enrollment,'course': course,}
    
    return render(request, template, context)
#
@login_required
@enrollment_required
def announcements(request, shortcut):
    
    course = request.course
    template = 'courses/announcements.html'
    context = {'course': course, 'announcements': course.announcements.all()}
    
    return render(request, template, context)
#
@login_required
@enrollment_required
def show_announcement(request, shortcut, pk):
    
    course = request.course
    announcement = get_object_or_404(course.announcements.all(), pk = pk)
    form = CommentForm(request.POST or None)
    
    if form.is_valid():
        comment = form.save(commit = False)
        comment.user = request.user
        comment.announcement = announcement
        comment.save()
        form = CommentForm()
        messages.success(request, 'Your comment was submitted. Thank you!')
    
    template = 'courses/show_announcement.html'
    context = {'course': course, 'announcement': announcement, 'form': form,}
    
    return render(request, template, context)
#
@login_required
@enrollment_required
def lessons(request, shortcut):
    course = request.course
    template = 'courses/lessons.html'
    lessons = course.release_lessons()
    
    if request.user.is_staff:
        lessons = course.lessons.all()
    
    context = {'course': course, 'lessons': lessons}
    
    return render(request, template, context)
#
@login_required
@enrollment_required
def lesson(request, shortcut, pk):
    
    course = request.course
    lesson = get_object_or_404(Lesson, pk = pk, course = course)
    
    if not request.user.is_staff and not lesson.is_available():
        messages.error(request, 'Sorry! This lesson is not available, yet!')
        return redirect('courses:lessons', shortcut = course.shortcut)
    
    template = 'courses/lesson.html'
    context = {'course': course, 'lesson': lesson}
    
    return render(request, template, context)
#
@login_required
@enrollment_required
def material(request, shortcut, pk):
    
    course = request.course
    material = get_object_or_404(Material, pk = pk, lesson__course = course)
    lesson = material.lesson
    
    if not request.user.is_staff and not lesson.is_available():
        messages.error(request, 'Sorry! This material is not available, yet!')
        return redirect('courses:lesson', shortcut = course.shortcut, pk = lesson.pk)
    
    if not material.is_embedded():
        return redirect(material.file.url)
    
    template = 'courses/material.html'
    context = {'course': course,'lesson': lesson,'material': material,}
    
    return render(request, template, context)
###################################################
##########             END             ############
###################################################