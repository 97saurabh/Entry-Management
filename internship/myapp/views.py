from django.shortcuts import render
from django.views.generic import (DeleteView,TemplateView,ListView,DetailView,CreateView,UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from myapp.models import Host,Visitor
from myapp.forms import HostForm,VisitorForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.mail import EmailMessage
import datetime
from django.core.mail import send_mail
from django.conf import settings
import urllib.request
import urllib.parse
# Create your views here.
def home(request):
    #Host.objects.all().delete()
    #Visitor.objects.all().delete()
    return render(request,'home.html')
class CreateHostView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    #redirect_field_name = "host_form.html"
    form_class = HostForm
    model = Host
class HostList(ListView):
    model = Host
    context_object_name = 'host'
class CreateVisitorView(CreateView):

    #redirect_field_name = "host_form.html"
    form_class = VisitorForm
    model = Visitor
    def get_success_url(self):
        print(self.object.id)
        return reverse('myapp:sendmail',args=(self.object.id,))



def sendSMS(numbers,message):
    data =  urllib.parse.urlencode({'apikey': 'mjQq3UioT04-Yc1CskXZn3kmgHM5arOJNt4g2hP5CG', 'numbers': numbers,
        'message' : message,})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)






def sendmail(request,pk):
    time = Visitor.objects.get(pk=pk)
    subject = 'Visitor Came To Meet'
    #message="Hi"
    message = 'Name: ' +time.visitor_name+"\n"+'Phone :'+str(time.phone_no) +"\n"+"Checkin Time: "+str(time.check_in)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [str(time.host.email),]
    send_mail( subject, message, email_from, recipient_list )
    resp =  sendSMS(str(time.host.phone_no),message)
    print (resp)
    return HttpResponseRedirect(reverse('myapp:visit_list'))
class VisitorList(ListView):
    model = Visitor
    context_object_name = 'visit'
    def get_queryset(self):
        return Visitor.objects.order_by('-date','-check_in')

def checkout(request,pk):
    time = Visitor.objects.get(pk=pk)
    time.check_out=datetime.datetime.now().strftime('%H:%M:%S')
    time.save()

    subject = 'Thanks for Visiting'
    message = 'Name: ' +time.visitor_name+"\n"+'Phone :'+str(time.phone_no) +"\n"+"Checkin Time: "+str(time.check_in)+"\n"+'Checkout Time: '+str(time.check_out)+"\n"+"Host Name: "+str(time.host.host_name)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [str(time.email),]
    send_mail( subject, message, email_from, recipient_list )
    print(message)
    resp =  sendSMS(str(time.phone_no),message)
    print (resp)


    return HttpResponseRedirect(reverse('myapp:visit_list'))
