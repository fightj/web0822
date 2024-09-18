from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 현재 로그인한 사용자를 작성자로 설정
            post.save()
            return redirect('post_list')  # 게시글 목록 페이지로 리다이렉트
    else:
        form = PostForm()
    return render(request, 'boards/create_post.html', {'form': form})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')  # 게시글 목록 페이지로 리다이렉트
    return render(request, 'boards/delete_post.html', {'post': post})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'boards/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'boards/post_detail.html', {'post': post})