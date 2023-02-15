from django.urls import path, include
from . import views


urlpatterns = [
    path('',  views.home, name='home'),
    path('signup/', views.signup, name="signup" ),
    path('events/', views.events, name="events" ),
    path('business/', views.bs, name="business" ),
    
    
    path('django/', views.django, name='django'),
]
