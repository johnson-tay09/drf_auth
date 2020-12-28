from rest_framework import generics

from .models import Card
from .permissions import IsAuthorOrReadOnly
from .serializers import CardSerializer


class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


# this class covers read, update and delete
class CardRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Card.objects.all()
    serializer_class = CardSerializer