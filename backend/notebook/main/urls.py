from django.urls import path
from .views import NoteListView, NoteDetailAPIView,NoteCreateView, NoteUpdateAPIView, NoteDeleteAPIView

urlpatterns = [
    path('', NoteListView.as_view()),
    path('<int:pk>/', NoteDetailAPIView.as_view(), name="note-details"),
    path('new/', NoteCreateView.as_view(), name="new"),
    path('update/<int:pk>/', NoteUpdateAPIView.as_view(), name="update"),
    path('delete/<int:pk>/', NoteDeleteAPIView.as_view(), name="delete")
]