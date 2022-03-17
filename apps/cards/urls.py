from django.urls import path
from apps.cards.api.views import SearchCardListAPIView


urlpatterns = [
    path("search=<str:query>", SearchCardListAPIView.as_view(), name="search_card_list_api")
]