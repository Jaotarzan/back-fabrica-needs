from rest_framework.serializers import ModelSerializer
from fabrica_needs.models import Product
from uploader.models import Image
from uploader.serializers import ImageSerializer
from rest_framework.serializers import SlugRelatedField

class ProductSerializer(ModelSerializer):
    appearence_attachment_key = SlugRelatedField(
        source="appearence",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    appearence = ImageSerializer(required=False, read_only=True)

    def create(self, validated_data):
        
        product = Product.objects.create(**validated_data)

        return product
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1