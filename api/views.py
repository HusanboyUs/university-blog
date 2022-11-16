from base.models import Blog
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializers import BlogSerializer 


class ListBlogApi(ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

list_blog_api=ListBlogApi.as_view()


class ListBlogApi(RetrieveAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

detail_blog_api=ListBlogApi.as_view()

