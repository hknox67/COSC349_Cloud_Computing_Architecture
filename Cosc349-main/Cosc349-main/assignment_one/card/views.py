from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Card
from .serializers import CardSerializer
from django.core.paginator import Paginator

class LatestCardsList(APIView):
    def get(self, request, format=None):
        cards = Card.objects.all()[0:4]
        serializer = CardSerializer(cards, many = True)
        return Response(serializer.data)

class CardDetails(APIView):
    def get_object(self, card_slug):
        try:
            return Card.objects.get(slug = card_slug)
        except Card.DoesNotExist:
            raise Http404("card not found")

    def get(self, request, card_slug, format = None):
        card = self.get_object(card_slug)
        serializer = CardSerializer(card)
        return Response(serializer.data)

class AllCards(APIView):
    def get(self, request, page, format = None):
        cards = Card.objects.all()
        paginator = Paginator(cards, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        serializer = CardSerializer(page_obj, many = True)
        return Response(serializer.data) 