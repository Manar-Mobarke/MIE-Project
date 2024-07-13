from django.urls import path, include
from rest_framework import routers
from . apis import ContactUsApi


router = routers.SimpleRouter()
router.register("contact-us", ContactUsApi, basename="contact-us")
urlpatterns = [
    path("", include(router.urls)),
]
