from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics


"""
using generic class based views which are already mixed-in 
"""


class SnippetList(generics.ListCreateAPIView):

    """
    to create new snippet or list all snippets
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    to get, put(update) and delete a particular snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
