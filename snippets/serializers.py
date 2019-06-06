from .models import Snippet, LANGAUGE_CHOICES, STYLE_CHOICES
from rest_framework import serializers

class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

    def create(self, validated_data):
        """ create and return a new  Snippet instance(model object) given the validated data"""
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ update and return an existing Snippet instance(model object) given the validated data"""
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('styles', instance.style)

        instance.save()
        return instance


