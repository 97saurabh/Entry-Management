from django.urls import path,re_path
app_name='myapp'
from myapp import views
urlpatterns=[
             path('',views.home,name="home"),
             path('form_host',views.CreateHostView.as_view(),name='host_form'),
             path('hosts',views.HostList.as_view(),name='host_list'),
             path('form_visitor',views.CreateVisitorView.as_view(),name='visitor_form'),
             path('visit',views.VisitorList.as_view(),name='visit_list'),
             re_path(r'^(?P<pk>\d+)/update/$',views.checkout,name="checked"),
             re_path(r'^(?P<pk>\d+)/mail/$',views.sendmail,name="sendmail"),


]
