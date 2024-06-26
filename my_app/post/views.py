from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView
from post.forms import PostForm
from post.models import Post


def posts(request):
    search_query = request.GET.get("search", "")
    if search_query:
        posts = Post.objects.filter(title__icontains=search_query)
    else:
        posts = Post.objects.all().order_by("id")
    all_images = Post.objects.all()
    return render(request, "posts.html", {"posts": posts, "all_images": all_images})




# def posts_view(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     return render(request, "posts_view.html", {"post": post})


@permission_required(perm="post.add_post", raise_exception=True)
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.my_user = request.user
            post.save()
            form.save_m2m()
            return redirect("/")
        else:
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "create.html", {"form": form})




def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.custom_user:
        return redirect(f"/posts/{post_id}/")
    if request.method == "GET":
        form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect("posts")
    return render(request, "edit_post.html", {"form": form, "post": post})


class PostDeleteView(DeleteView):
    model = Post
    success_url = "posts"
    template_name = "delete_post.html"


