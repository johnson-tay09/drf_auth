from django.urls import path

from .views import CardList, CardRetrieveUpdateDestroy

urlpatterns = [
    # path("<int:pk>/", EntryDetail.as_view()),
    path("cards", CardList.as_view(), name="card_list_create"),
    path("<int:pk>/", CardRetrieveUpdateDestroy.as_view()),
]