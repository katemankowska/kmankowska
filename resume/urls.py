from django.conf.urls import url
from resume import views

urlpatterns = [
    url(r'^$', views.profile, name='index'),
    url(r'^resume', views.resume_pdf, name='resume_pdf')
]
