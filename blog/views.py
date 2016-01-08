from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from django.utils import timezone
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required,permission_required
from django.core.paginator import Paginator
# Create your views here.
def post_list(request,page_number=1):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    current_page=Paginator(posts,5)
    return render(request, 'blog/post_list.html', {'posts': current_page.page(page_number)})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
@permission_required('blog.delete_post', login_url='/blog/')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
@permission_required('blog.delete_post', login_url='/blog/')
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
@permission_required('blog.delete_post', login_url='/blog/')
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)

@login_required
@permission_required('blog.delete_post', login_url='/blog/')
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
@permission_required('blog.delete_comment', login_url='/blog/')
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)

@permission_required('blog.delete_comment', login_url='/blog/')
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)

def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if pk in request.COOKIES:
        post.likes-=1
        post.save()
        response=redirect('/')
        response.delete_cookie(pk)
        return response
    else:
        post.likes+=1
        post.save()
        response=redirect('/')
        response.set_cookie(pk,'test')
        return response