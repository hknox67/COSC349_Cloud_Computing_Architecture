from urllib.parse import urlparse
from django.urls import path, include
from card import views

urlpatterns = [
    path("latest-cards/", views.LatestCardsList.as_view()),
    path("card/<slug:card_slug>/", views.CardDetails.as_view()),
    path("cards/<int:page>/", views.AllCards.as_view()),
]