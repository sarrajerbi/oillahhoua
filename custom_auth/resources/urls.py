from django.urls import path
from .views import ResourceListCreateAPIView, ResourceDetailAPIView, CommentCreateAPIView, RatingCreateAPIView, ResourceSearchAPIView

urlpatterns = [
    path('resources/', ResourceListCreateAPIView.as_view(), name='resource-list-create'),
    path('resources/<int:pk>/', ResourceDetailAPIView.as_view(), name='resource-detail'),
    path('comments/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('ratings/', RatingCreateAPIView.as_view(), name='rating-create'),
    path('search/', ResourceSearchAPIView.as_view(), name='resource-search'),
]
