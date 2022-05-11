from django.db import models
from django.core import validators
from django.template.defaultfilters import slugify
from django.urls.base import reverse
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django import forms
# Create your models here.



class Client(models.Model):

    # Basic Fields.
    first_name = models.CharField(null=True, blank=True, max_length=200)
    last_name = models.CharField(null=True, blank=True, max_length=200)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    # RELATED fields
    
    

    def __str__(self):
        return '{} {}'.format(self.first_name, self.uniqueId)

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.first_name, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.first_name, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)




def increment_order_number():
    last_order = Order.objects.all().order_by('id').last()
    if not last_order:
        return 'ODR00001'
    order_no = last_order.number
    order_int = int(order_no.split('ODR')[-1])
    new_order_int = order_int + 1
    new_order_no = 'ODR' + "%05d" % (new_order_int, )
    return new_order_no

class Order(models.Model):

    SUBJECTS = [
        ('Subject one','Subject one'),
        ('Subject two','Subject two'),
        ('Subject three','Subject three'),
        ('Subject four','Subject four')
    ]


    FORMATS = [
        ('PDF','PDF'),
        ('WORD(.docx)','WORD(.docx)'),
        ('APA','APA')
       
    ]


    
    SPACING = [
        ('Single spaced','Single spaced'),
        ('Double Spaced','Double spaced')
       
    ]
    # Basic Fields.
    number = models.CharField(
        null=False, default=increment_order_number, blank=False, max_length=100, unique=True)
    subject = models.CharField(
        choices=SUBJECTS, default='Subject one', max_length=100)
    prefered_format = models.CharField(choices=FORMATS, null=True, blank=True, max_length=200)
    number_of_sources = models.IntegerField(
        default=1, validators=[MinValueValidator(1)], null=True, blank=True)
    number_of_pages = models.IntegerField(
        default=1, validators=[MinValueValidator(1)], null=True, blank=True)
    powerpoint_slides = models.CharField(null=True, blank=True, max_length=100)
    prefered_spacing = forms.ChoiceField(choices=SPACING, widget=forms.RadioSelect)
    topic = models.CharField(null=True, blank=True, max_length=100)
    assignment_details = models.TextField(null=True, blank=True, max_length=600)
    assignment_file = models.FileField(upload_to='clientuploads')

    total_price = models.CharField(null=True, blank=True, max_length=100)

    payment_transaction_id = models.CharField(null=True, blank=True, max_length=100)



    client = models.ForeignKey(
        Client, blank=True, null=True, on_delete=models.SET_NULL)



    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.CharField(null=True, blank=True, default="Pending", max_length=15)

    payment_made = models.BooleanField(null=True, blank=True, default=0)

    

    def __str__(self):
        return '{} {}'.format(self.number, self.uniqueId)

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.number, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.number, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Order, self).save(*args, **kwargs)

class Assignmentfile(models.Model):
    file_directory = models.FileField(upload_to='clientuploads')

    # Related Fields
    order = models.ManyToManyField(Order, through='OrderAssignmentfile')

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.file_directory)

    """def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})"""

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(
                self.file_directory, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.file_directory, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Assignmentfile, self).save(*args, **kwargs)
