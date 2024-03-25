from rest_framework import serializers
from ebooks.models import Ebook, Review


# This Model, serializer fields and relationships will be automatically generated for you.
# Inspecting these automatically generated fields can be useful tool for determing how to 
# customize the relationship style
class ReviewSerializer(serializers.ModelSerializers):
    
    # StringRelatedField used to represent the target of the relationship using its __str_- method
    review_author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        
        model = Review
        exclude = ("ebook")

class EbookSerializer(serializers.ModelSerializers):
    
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Ebook
        fields = "__all__"s
