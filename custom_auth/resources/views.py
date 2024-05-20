from rest_framework import generics, permissions
from django.db.models import Q
from .models import Resource, Comment, Rating
from .serializers import ResourceSerializer, CommentSerializer, RatingSerializer

class ResourceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

class ResourceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RatingCreateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ResourceSearchAPIView(generics.ListAPIView):
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query_params = self.request.query_params
        subject = query_params.get('subject')
        level = query_params.get('level')
        # You can add more filter criteria as needed

        queryset = Resource.objects.all()

        if subject:
            queryset = queryset.filter(subject__icontains=subject)
        if level:
            queryset = queryset.filter(level__icontains=level)
        # Add more filters here for additional criteria

        return queryset
