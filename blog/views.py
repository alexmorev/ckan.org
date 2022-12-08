from django.contrib.auth.models import User
from django.views.generic.list import ListView
from .models import BlogPostPage, PostCategoryPage
from django.shortcuts import redirect
from wagtail.contrib.modeladmin.views import CreateView
from wagtail.admin import messages


class UsersBlogPostListView(ListView):

    model = BlogPostPage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_name = self.kwargs.get('username', '')
        author = User.objects.get(username=user_name)
        context['posts'] = BlogPostPage.objects.filter(owner=author.id)
        context['author'] = author
        return context


class TagsBlogPostListView(ListView):

    model = BlogPostPage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.kwargs.get('tag', '')
        context['posts'] = BlogPostPage.objects.filter(tags__name=tag)
        context['tag'] = tag
        return context



class CategoriesBlogPostListView(ListView):

    model = BlogPostPage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_id = self.kwargs.get('cat_id', '')
        if cat_id == 0:
            context['posts'] = BlogPostPage.objects.all()
        else:    
            context['posts'] = BlogPostPage.objects.filter(category=cat_id).order_by("-created")
            context['categories'] = PostCategoryPage.objects.all().order_by('category_title')
            context['cat_selected'] = PostCategoryPage.objects.filter(id=cat_id).first()
        return context


class ProfileCreateView(CreateView):
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        instance = form.save()
        messages.success(
            self.request, self.get_success_message(instance),
            buttons=self.get_success_message_buttons(instance)
        )
        return redirect(self.get_success_url())

