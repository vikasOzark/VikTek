from nturl2path import url2pathname
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('get-started/', views.get_started, name='get_started'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('confirmation/<str:type>', views.confirmation_project, name='confirmation'),
    path('confirmation/project_req/', views.project_reqeust, name = 'project_req'),
    path('contact-us/', views.contect_us, name="make_contact" ),
    path('thank-you/<str:name>', views.thank_you, name='thank-you')
]
