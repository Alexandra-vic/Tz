from rest_framework import serializers
from .models import Category, Tag


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =('id',
                 'name',
                 )


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields =('id',
                 'tag',
                 )