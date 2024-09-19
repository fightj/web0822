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

def edit_post(request, pk):
    post = get_object_or_404(Post, id=pk)  # 게시물 가져오기
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # 기존 게시물로 폼 초기화
        if form.is_valid():
            form.save()  # 수정 내용 저장
            return redirect('post_detail', pk=pk)  # 리다이렉트 시 pk 사용
    else:
        form = PostForm(instance=post)  # GET 요청 시 기존 데이터로 폼을 초기화
    
    return render(request, 'boards/edit_post.html', {'form': form, 'post': post})
