from rest_framework import parsers, viewsets

from uploader.models import Document, Image
from uploader.serializers import DocumentUploadSerializer, ImageUploadSerializer


class DocumentUploadViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
