from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import BlogForm
from .models import Blog

# from django.contrib import admin



class BlogIndex(generic.TemplateView):
    model = Blog
    paginate_by = 10
    template_name = "blogs/blog_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_list'] = Blog.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
        return context


class BlogUpdateView(generic.FormView, generic.UpdateView):
    model = Blog
    form_class = BlogForm
    object = None
    template_name = 'blogs/blog_edit.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['blog_post'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse('blogs:blog_index')

    def form_valid(self, form):
        return super().form_valid(form)


class BlogCreateView(generic.FormView, generic.CreateView):
    model = Blog
    form_class = BlogForm
    object = None
    template_name = 'blogs/blog_edit.html'

    def get_success_url(self):
        return reverse('blogs:blog_index')


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 40
    template_name = 'blogs/blog_list.html'

    def get_queryset(self):
        return Blog.objects.all()


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_post'] = context['object']
        return context
