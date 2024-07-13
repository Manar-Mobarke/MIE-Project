from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', help_text='Your full name', default='Anonymous')
    email = models.EmailField(help_text='Your email address', verbose_name='email address')
    message = models.TextField(help_text='Your message')

    class Meta:
        verbose_name_plural = "Contact Us Entries"
