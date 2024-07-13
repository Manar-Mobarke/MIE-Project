from rest_framework.viewsets import ModelViewSet
from .serializers import ContactUsSerializer
from .models import ContactUs


class ContactUsApi(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
