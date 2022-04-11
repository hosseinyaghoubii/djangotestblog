from django.urls import reverse_lazy
from django.views import generic

from .models import Post
from .forms import PostForm

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(status="pub").order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail_view.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/add_post.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('post_list')

# def post_list_views(request):
#     post_list = Post.objects.filter(status="pub").order_by('-datetime_modified')
#     return render(request, 'blog/post_list.html', context={"post_list": post_list})
#
# def post_detail_views(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/detail_view.html', context={'post': post})
# def views_add_new_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("post_list"))
#     else:
#         form = PostForm()
#
#     return render(request, 'blog/add_post.html', context={'form': form})
#
# def views_update_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect(reverse("post_detail", kwargs={'post': post}))
#     return render(request, 'blog/add_post.html', context={'form': form})
#
# def views_post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#
#     if request.method == "POST":
#         post.delete()
#         return redirect('post_list')
#     return render(request, 'blog/delete_post.html', context={'post': post})

