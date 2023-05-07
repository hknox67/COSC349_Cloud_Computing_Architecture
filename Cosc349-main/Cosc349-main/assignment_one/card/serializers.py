from rest_framework import serializers

from .models import Card, Card_colour, Card_subtype, Card_supertype, Card_type, Card_set

class ColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card_colour
        fields = (
            "id",
            "name",
        )

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card_supertype
        fields = (
            "id",
            "name",
        )

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card_type
        fields = (
            "id",
            "name",
        )

class SubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card_subtype
        fields = (
            "id",
            "name",
        )

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card_set
        fields = (
            "id",
            "code",
            "name",
        )

class CardSerializer(serializers.ModelSerializer):
    superTypes = SuperTypeSerializer(read_only = True, many=True)
    cardTypes = TypeSerializer(read_only = True, many=True)
    subTypes = SubTypeSerializer(read_only = True, many=True)
    colours = ColourSerializer(read_only = True, many=True)
    cardSet = serializers.StringRelatedField(many=False)

    class Meta:
        model = Card
        fields = (
            "id",
            "name",
            "description",
            "price",
            "image",
            "manaCost",
            "cmc",
            "artist",
            "rarity",
            "get_absolute_url",
            "superTypes",
            "cardTypes",
            "subTypes",
            "colours",
            "cardSet",
        )