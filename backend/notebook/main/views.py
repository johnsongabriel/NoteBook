from django.shortcuts import render, redirect
from rest_framework.response import Response
from .serializers import NoteSerializers
from .models import Note
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework import generics

# Create your views here.
class NoteListView(APIView):
    def get(self, request):
        query = Note.objects.all()
        serializer = NoteSerializers(query, many=True)
        return Response(serializer.data)


#viewing each of the created note
class NoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializers



#Creating note view
class NoteCreateView(APIView):
    def post(self, request):
        serializer = NoteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# Updating creatred note
class NoteUpdateAPIView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializers
    lookup_field = 'pk'

    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
# deleting created note
class NoteDeleteAPIView(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializers
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)