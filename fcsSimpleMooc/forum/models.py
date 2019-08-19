'''

Models for the forum's related instances

. Classes

    . Thread
    . Reply

. Methods

    . post_save_reply
    . post_delete_reply

. Signals

    . post_save_reply

'''
from django.db import models
from django.conf import settings
#
from taggit.managers import TaggableManager

# Create your models here.
class Thread(models.Model):
    #
    title = models.CharField('Title', max_length=100)
    slug = models.SlugField('Identifier', max_length=100, unique=True)
    body = models.TextField('Message')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               verbose_name='Author', 
                               related_name='threads', 
                               on_delete = models.PROTECT)
    views = models.IntegerField('Views', blank=True, default=0)
    answers = models.IntegerField('Responses', blank=True, default=0)
    
    tags = TaggableManager()

    created_on = models.DateTimeField('Created on', auto_now_add=True)
    updated_on = models.DateTimeField('Last update', auto_now=True)

    def __str__(self):
        #
        return self.title

    #@models.permalink
    def get_absolute_url(self):
        #
        return '/forum/' + self.slug

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        ordering = ['-updated_on']


class Reply(models.Model):

    thread = models.ForeignKey(Thread, 
                               verbose_name='Topic', 
                               related_name='replies',
                               on_delete = models.PROTECT)
    reply = models.TextField('Reply')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               verbose_name='Autor',
                               related_name='replies', 
                               on_delete = models.PROTECT)
    correct = models.BooleanField('Correct?', blank=True, default=False)

    created_on = models.DateTimeField('Created on', auto_now_add=True)
    updated_on = models.DateTimeField('Last update', auto_now=True)

    def __str__(self):
        return self.reply[:100]


    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'
        ordering = ['-correct', 'created_on']


def post_save_reply(created, instance, **kwargs):
    
    instance.thread.answers = instance.thread.replies.count()
    instance.thread.save()
    
    if instance.correct:
        instance.thread.replies.exclude(pk = instance.pk).update(correct = False)

def post_delete_reply(instance, **kwargs):
    
    instance.thread.answers = instance.thread.replies.count()
    instance.thread.save()

models.signals.post_save.connect(post_save_reply, sender = Reply, dispatch_uid = 'post_save_reply')
models.signals.post_delete.connect(post_delete_reply, sender = Reply, dispatch_uid = 'post_delete_reply')
    
    