from django.db import models
from django.db.models.base import Model
from django.core.mail import send_mail

from django.db.models.signals import post_save

from django.dispatch import receiver

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=100)
    closure_date = models.DateTimeField(null=True)
    final_closure_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.title

        
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Idea(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField(max_length=500, null=True)
    file = models.FileField(upload_to='')
    date = models.DateTimeField(null=True)


class Comment(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)



@receiver(post_save, sender=Idea)
def send_new_officer_notification_email(sender, instance, created, **kwargs):
    if created:
        subject = 'subject'
        message = 'A New Idea has been assigned!\n'

        message += '--' * 30

        send_mail(
            subject,
            message,
            'tangthienan9@example.com',
            ['dksky456@xample.com'],
            fail_silently=False,
        )