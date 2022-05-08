from django import forms
from django.contrib.auth.models import User
from django.forms import widgets, modelformset_factory
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from .models import *
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Column, Div, Field, Layout, Row, Submit

import json


class DateInput(forms.DateInput):
    input_type = 'date'

class DateTimePickerInput(forms.DateTimeInput):
        input_type = 'datetime'


class OrderForm(forms.ModelForm):
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
    number_of_sources = forms.IntegerField(label="Number of Sources" )
    number_of_pages = forms.IntegerField(label="Number of pages")
    powerpoint_slides = forms.CharField(label="Powerpoint Slides")
    prefered_spacing = forms.ChoiceField(choices=SPACING, widget=forms.RadioSelect)
    assignment_details = forms.Textarea()
    assignment_file = forms.FileField(label='Assignment File')

    total_price = forms.CharField(
                    required=True,
                    label="Total price in $:",
                    
                )


    number = forms.CharField(required=False)
   
    subject = forms.ChoiceField(
        choices=SUBJECTS,
        required=True,
        label='Select the subject',
        widget=forms.Select(attrs={'class': 'form-control mb-3'}),)

    prefered_format = forms.ChoiceField(
        choices=FORMATS,
        required=True,
        label='Prefered Format',
        widget=forms.Select(attrs={'class': 'form-control mb-3'}),)

    topic = forms.CharField(
        required=True,
        label='Your Topic',
    )

    deadline = forms.DateTimeField(
        required=True,
        label='Deadline',
        widget=forms.DateInput(attrs=dict(type='date')))
    

    


    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            

            Submit('submit', ' SUBMIT '))
        
        self.fields['number'].widget.attrs['readonly'] = True
        self.fields['number'].widget.attrs['class'] = "form-control"
        self.fields['topic'].widget.attrs['class'] = "form-control"
        self.fields['number'].widget.attrs['type'] = "hidden"
        self.fields['number_of_pages'].widget.attrs['class'] = "form-control"
        self.fields['total_price'].widget.attrs['class'] = "form-control"
        self.fields['number_of_sources'].widget.attrs['class'] = "form-control"
        self.fields['assignment_file'].widget.attrs['class'] = "form-control"
        self.fields['deadline'].widget.attrs['class'] = "form-control"
        self.fields['deadline'].widget.attrs['id'] = "datetimepicker12"
        self.fields['assignment_details'].widget.attrs['class'] = "form-control"
        self.fields['powerpoint_slides'].widget.attrs['class'] = "form-control"
        self.fields['prefered_format'].widget.attrs['class'] = "form-select"
        self.fields['subject'].widget.attrs['class'] = "form-select"
     
        #self.fields['discount'].widget.attrs['placeholder'] = "Enter percentage discount"

    class Meta:
        model = Order
        fields = ['number','number_of_sources','number_of_pages','deadline','prefered_format','prefered_spacing','assignment_details','powerpoint_slides',
        'assignment_file','topic','total_price','client'
        ]
        """model = Invoice
        fields = ['number', 'dueDate', 'paymentTerms', 'status',
                  'description', 'client', 'istaxable', 'apply_discount', 'discount']"""

    def clean(self, *args, **kwargs):
        super(OrderForm, self).clean()

        # getting username and password from cleaned_data
        number = self.cleaned_data.get('number')
        

        # validating the username and password
    """if 'ODR' not in number:
            self._errors['number'] = self.error_class(
                ['Invalid ORDER number'])"""


class ClientForm(forms.ModelForm):
    confirm_email = forms.CharField(label="Re-type Email")
    emailAddress= forms.CharField(label="Email")
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    class Meta:
        model = Client
        fields = ['first_name', 'last_name','emailAddress']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            

            Submit('submit', ' SUBMIT '))

        self.fields['first_name'].widget.attrs['class'] = "form-control"
        self.fields['last_name'].widget.attrs['class'] = "form-control"
        self.fields['emailAddress'].widget.attrs['class'] = "form-control"
        self.fields['confirm_email'].widget.attrs['class'] = "form-control"


        
     
        #self.fields['discount'].widget.attrs['placeholder'] = "Enter percentage discount"

    

    def clean(self, *args, **kwargs):
        super(ClientForm, self).clean()

        
