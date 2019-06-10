from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions, renderers, reverse
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response


"""
using generic class based views which are already mixed-in 
"""


class SnippetList(generics.ListCreateAPIView):


    """
        to give write permissions to authenticated users only 
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    """
    to update the owner of snippet code override serialized create() 
    """

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    """
        to create new snippet or list all snippets
        """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    to get, put(update) and delete a particular snippet
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetHighlight(generics.GenericAPIView):
    """
    class to display highlighted snippet in pre-rendered html
    """
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


@api_view
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
    })


