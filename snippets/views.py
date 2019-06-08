from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics, mixins



"""
using mixins class (which provide same behaviour as we were doing with class based view)
, GENERICAPIView is the base class for all generic view and mixins is inherited them 
"""


class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    """
    to create new snippet or list all snippets
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(self, request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    """
    to get, put(update) and delete a particular snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def retrieve(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
