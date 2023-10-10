from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
# Create your views here.
from .models import HomePage,AboutPage,Post,Comment
from .forms import CommentForm

def home(request):
    page = HomePage.objects.all()[0]
    posts = Post.objects.filter(status='PUB')
    paginator = Paginator(posts, per_page=5)  # عرض 10 عناصر في كل صفحة
    page_number = request.GET.get('page')  # احصل على رقم الصفحة من الطلب
    page_obj = paginator.get_page(page_number)
    context ={'page':page,'page_obj': page_obj}
    return render(request, 'blog/home.html', context)


###############################
def about(request):
    page = AboutPage.objects.all()[0]
    context ={'page':page}
    return render(request, 'blog/about.html', context)


###########################
def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, 
                             status =Post.Status.PUBLISHED,
                             publish__year = year,
                             publish__month = month,
                             publish__day = day,
                             slug = post
                             )
    
    comments = post.comments.filter( active=True)
    context ={'post':post ,'comments':comments}
    return render(request, 'blog/post_detail.html', context)


def post_comment(request,post_id):
    post = get_object_or_404(Post, id=post_id, status= Post.Status.PUBLISHED) 

    comment = None

    form = CommentForm(data=request.POST)  
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save() 
    context={'comment':comment,'form':form,'post':post}
    return render(request,'blog/comment.html',context) 

            



