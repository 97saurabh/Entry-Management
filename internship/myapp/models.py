from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime
# Create your models here.
from django.urls import reverse
class Host(models.Model):
    host_name = models.CharField(max_length=30,blank=False)
    email = models.EmailField(max_length=254)
    phone_no = PhoneNumberField(blank=True, help_text='Contact Phone Number')
    def get_absolute_url(self):
        return reverse('myapp:host_list')
    def __str__(self):
        return self.host_name
class Visitor(models.Model):
    host=models.ForeignKey('Host',on_delete = models.CASCADE,related_name='visitor')
    visitor_name = models.CharField(max_length=30,blank=False)
    email = models.EmailField(max_length=254)
    phone_no = PhoneNumberField(blank=True, help_text='Contact phone number')
    date = models.DateField(auto_now=True)
    check_in = models.TimeField(auto_now_add=True)
    check_out=models.TimeField(null=True,blank=True)

    def checking_out(self):
        self.check_out = datetime.datetime.now().time()
        self.save()
    def get_absolute_url(self):
        return reverse('myapp:visit_list')
    def __str__(self):
        return self.visitor_name
