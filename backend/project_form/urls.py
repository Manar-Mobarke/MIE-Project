from django.urls import path, include
from rest_framework import routers
from . apis import ProjectFormAPI


router = routers.SimpleRouter()
router.register("project-form", ProjectFormAPI, basename="project-form")
urlpatterns = [
    path("", include(router.urls)),
]
