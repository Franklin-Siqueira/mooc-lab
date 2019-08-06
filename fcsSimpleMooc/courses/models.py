'''

Models for the courses' related instances

. CourseManager
. Course
. Enrollment
. Announcement
. Lesson
. Material
. Comment

'''
from django.db import models
from django.conf import settings
from django.utils import timezone
#
from fcsSimpleMooc.core.mail import send_mail_template

# Create your models here.
class CourseManager(models.Manager):
    
    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains = query)|models.Q(desc__icontains = query))

class Course(models.Model):
    
    name = models.CharField('Name', max_length = 100)
    shortcut = models.SlugField('Shortcut')
    desc = models.TextField('Description', blank = True)
    about = models.TextField('About the course', blank = True)
    startDate = models.DateField('Start date', null = True, blank = True)
    image = models.ImageField(upload_to = 'courses/images', verbose_name = 'Image', null = True, blank = True)
    created_on = models.DateTimeField('Creation date', auto_now_add = True)
    updated_on = models.DateTimeField('Last update', auto_now = True)
    
    #
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['name']
    #
    objects = CourseManager()
    #
    def __str__(self):
        return self.name
    #
    def release_lessons(self):
        today = timezone.now().date()
        return self.lessons.filter(release_date__gte = today)
    # from a tip given by Gustavo(?)
    def get_absolute_url(self):
        return '/courses/' + self.shortcut

class Lesson(models.Model):

    name = models.CharField('Name', max_length = 100)
    description = models.TextField('Description', blank = True)
    number = models.IntegerField('Number (ordering)', blank = True, default = 0)
    release_date = models.DateField('Release date', blank = True, null = True)

    course = models.ForeignKey(Course, 
                               verbose_name = 'Course', 
                               related_name = 'lessons', 
                               on_delete = models.PROTECT)

    created_on = models.DateTimeField('Creation date', auto_now_add = True)
    updated_on = models.DateTimeField('Updated on', auto_now = True)

    def __str__(self):
        return self.name

    def is_available(self):
        if self.release_date:
            today = timezone.now().date()
            return self.release_date >= today
        return False

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ['number']

class Material(models.Model):

    name = models.CharField('Name', max_length = 100)
    embedded = models.TextField('Vídeo embedded', blank = True)
    file = models.FileField(upload_to='lessons/materials', blank = True, null = True)

    lesson = models.ForeignKey(Lesson, 
                               verbose_name='Lesson', 
                               related_name='materials', 
                               on_delete = models.PROTECT)

    def is_embedded(self):
        return bool(self.embedded)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
    
class Enrollment(models.Model):

    STATUS_CHOICES = ((0, 'Pending'),(1, 'Approved'),(2, 'Cancelled'),)
    
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'User', on_delete=models.PROTECT)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             verbose_name = 'User', 
                             related_name ='enrollments',
                             on_delete = models.PROTECT)
    course = models.ForeignKey(Course, verbose_name = 'Course', 
                               related_name = 'enrollments', 
                               on_delete = models.PROTECT)
    status = models.IntegerField('Status', choices = STATUS_CHOICES, default = 1, blank = True)

    created_on = models.DateTimeField('Creation date', auto_now_add = True)
    updated_on = models.DateTimeField('Updated on', auto_now = True)

    def active(self):
        self.status = 1
        self.save()

    def is_approved(self):
        return self.status == 1

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
        unique_together = (('user', 'course'),)

class Announcement(models.Model):

    course = models.ForeignKey(Course, 
                               verbose_name='Course', 
                               related_name='announcements', 
                               on_delete=models.PROTECT)
    
    title = models.CharField('Title', max_length=100)
    content = models.TextField('Contents')

    created_on = models.DateTimeField('Creation date', auto_now_add = True)
    updated_on = models.DateTimeField('Updated on', auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'
        ordering = ['-created_on']

class Comment(models.Model):

    announcement = models.ForeignKey(Announcement, 
                                     verbose_name = 'Announcement', 
                                     related_name = 'comments', 
                                     on_delete = models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             verbose_name = 'User',
                             on_delete=models.PROTECT)
    
    comment = models.TextField('Comment')

    created_on = models.DateTimeField('Creation date', auto_now_add = True)
    updated_on = models.DateTimeField('Updated on', auto_now = True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['created_on']

def post_save_announcement(instance, created, **kwargs):
    #
    if created:
        subject = instance.title
        context = {'announcement': instance}
        template_name = 'courses/announcement_mail.html'
        enrollments = Enrollment.objects.filter(course = instance.course, status=1)
        #
        for enrollment in enrollments:
            recipient_list = [enrollment.user.email]
            send_mail_template(subject, template_name, context, recipient_list)

models.signals.post_save.connect( post_save_announcement, 
                                  sender = Announcement, 
                                  dispatch_uid = 'post_save_announcement')
###################################################
##########             END             ############
###################################################