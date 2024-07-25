from django.urls import path, include
from rest_framework import routers
from . apis import ProjectFormAPI
from django.urls import path, include
from . import views



router = routers.SimpleRouter()
router.register("project-form", ProjectFormAPI, basename="project-form")
urlpatterns = [
    path("", include(router.urls)),
    path('home', views.home),
    path('about', views.about),
    path('contact', views.contact),
    path('projects', views.projects),
    path('registration', views.registration),
    
]
