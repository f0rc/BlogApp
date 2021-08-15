from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django_oso.auth import authorize
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



# Create your views here.


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
        
    }
    return render(request, 'social/list.html', context)

#
class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'social/list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'contents']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'contents']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# @login_required
# def new_post(request):
#     if request.method == 'POST':
#         # This branch runs when the user submits the form.

#         # Create an instance of the form with the submitted data.
#         form = PostForm(request.POST)

#         # Convert the form into a model instance.  commit=False postpones
#         # saving to the database.
#         post = form.save(commit=False)

#         # Make the currently logged in user the Post creator.
#         post.date_posted = request.user

#         # Save post in database.
#         post.save()

#         # Rediect to post list.
#         return HttpResponseRedirect(reverse('index'))
#     elif request.method == 'GET':
#         # GET evaluated when form loaded.
#         form = PostForm()
#         # Render the view with the form for the user to fill out.
#         return render(request, 'social/new_post.html', { 'form': form })
#     else:
#         return HttpResponseNotAllowed(['GET', 'POST'])