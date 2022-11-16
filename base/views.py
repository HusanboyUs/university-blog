from django.shortcuts import render
from .models import Blog
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



class ListBlogView(ListView):
    template_name='main/blog-card.html'
    model=Blog
    context_object_name = 'blog'

    def get_queryset(self):
        title = self.request.GET.get('search-title')
        blog_list=self.model.objects.all()
        if title:
            blog_list=blog_list.filter(title__icontains=title)
        return blog_list    


list_view=ListBlogView.as_view()

class DetailBlogView(DetailView):
    template_name = 'main/detail.html'
    model= Blog
    context_object_name = 'detail'


detail_view=DetailBlogView.as_view()    



def BlogAboutView(request):
    return render(request, 'main/about.html')