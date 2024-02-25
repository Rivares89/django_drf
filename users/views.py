from rest_framework import generics

from users.serializers import PaymentSerializer


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
