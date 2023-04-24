from .models import Note
from rest_framework import serializers

class NoteSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Note
        fields = ['id','title', 'descr', 'date']