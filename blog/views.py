from django.shortcuts import render


def blog_page(request):
    return render(request,'blog/blog-home.html')
   
def single_page(request):
    return render(request,'blog/blog-single.html')









# Create your views here.
