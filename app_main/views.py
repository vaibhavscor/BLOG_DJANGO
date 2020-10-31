from django.shortcuts import render, get_object_or_404
from .models import blog
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

 
def home_page(request):
    blogs = blog.objects.all()
    return render(request,'blogs.html',{'blogs':blogs})

def blog_read(request,slug):
    read_blog = blog.objects.filter(slug=slug).first()     # accesing the 1st obejct of queryset
    print(read_blog)
    context = {'blog': read_blog}
    return render(request,'read_blog.html', context)

def searchkey(request):
    query = request.GET['search']
    blog_searched = blog.objects.all()
    if len(query)>80:
        parms = blog.objects.none()
    else:
        blog_title = blog.objects.filter(title__icontains=query)
        blog_content = blog.objects.filter(content_main__icontains=query)
        blog_auth = blog.objects.filter(name__icontains=query)
        blog_searched = blog_title.union(blog_content,blog_auth)
        parms = {'blog_searched': blog_searched}

    return render(request,'search.html',parms)

# def like_post(request):
#     user = request.User
#     if request.method == "POST":
#         blog_id = request.POST.get['post_id']
#         blog_obj = blog.objects.get(id=post_id)

#     return render(request,'search.html',parms)



def blog_home(request):
    return render(request, 'blog_home.html')

