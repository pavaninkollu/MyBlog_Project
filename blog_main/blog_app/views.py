from django.shortcuts import render, get_object_or_404,redirect
from .models import Post, Comment, Category
from .forms import CommentForm

# Create your views here.



def post_list(request):
    # posts=Post.objects.all().order_by('-created_at')
    posts = Post.objects.all()

    categories = Category.objects.all()  # Fetch all categories
    
    posts_by_category = {}  # Dictionary to store posts grouped by category
    
    # Loop through categories and get related posts
    for category in categories:
        posts_by_category[category] = Post.objects.filter(category=category)
        
    
    
    return render(request, 'blog_app/post_list.html', {'posts':posts, 'posts_by_category':posts_by_category,'categories': categories})


def post_detail(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    comments=post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    
    return render(request, 'blog_app/post_detail.html', {'post':post, 'comments':comments, 'form':form})



