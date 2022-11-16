from rest_framework import serializers
from base.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'