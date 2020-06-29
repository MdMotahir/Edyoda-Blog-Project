from django.shortcuts import render
from blog.models import *
from blog.forms import ContactUsForm,PostCreateForm,PostUpdateForm
from django.views import View,generic
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
# Create your views here.
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from django.contrib.auth import get_user_model
from account.models import *
from django.db.models import Q
from django.contrib import messages

class PostListView(generic.ListView):
    model = Post
    template_name = "blog/Home.html"
    queryset=Post.objects.filter(status='P')
    context_object_name='posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category=Category.objects.all()
        context["category"] = category
        return context

def search(request):
    query=request.GET['query']
    posts=Post.objects.filter(
            Q(title__icontains=query),
            Q(content__icontains=query),
        ).distinct()
    context={'posts':posts,'query':query}
    return render(request,'blog/Search.html',context)

class PostDetailView(LoginRequiredMixin,generic.DetailView):
    model = Post
    template_name = "blog/Blog Details.html"
    login_url=reverse_lazy('login')

def category_page(request,slug):
    category=Category.objects.all()
    cat=Category.objects.get(slug=slug)
    posts=Post.objects.filter(category=cat)
    return render(request,"blog/Category.html",context={"cat":cat,"posts":posts,"category":category})
    
def MyBlog(request,slug):
    Auth=User.objects.get(username=slug)
    posts=Post.objects.filter(author=Auth)
    return render(request,"blog/My Blog.html",context={'posts':posts,'Auth':Auth})

def DraftBlog(request,slug):
    Auth=User.objects.get(username=slug)
    posts=Post.objects.filter(author=Auth,status='D')
    return render(request,"blog/My Blog.html",context={'posts':posts,'Auth':Auth})

def PublishedBlog(request,slug):
    Auth=User.objects.get(username=slug)
    posts=Post.objects.filter(author=Auth,status='P')
    return render(request,"blog/My Blog.html",context={'posts':posts,'Auth':Auth})

def thank_you(request):
    return render(request,'blog/Thank You Page.html')

class ContactUsFormView(FormView):
    form_class = ContactUsForm
    success_url=reverse_lazy("Thank You")
    template_name="blog/Contact Us.html"


class PostCreateView(LoginRequiredMixin,PermissionRequiredMixin,generic.CreateView):
    permission_required='blog.add_post'
    login_url=reverse_lazy('login')
    model = Post
    form_class=PostCreateForm
    template_name="blog/Blog Create.html"
    success_url=reverse_lazy("Thank You")

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    permission_required='blog.change_post'
    login_url=reverse_lazy('login')
    model=Post
    form_class=PostUpdateForm
    template_name="blog/Blog Update.html"
    success_url=reverse_lazy("Thank You")

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self,*args, **kwargs):
        post=Post.objects.get(slug=self.kwargs.get('slug'))
        if post.author==self.request.user:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    permission_required='blog.delete_post'
    login_url=reverse_lazy('login')
    model=Post
    template_name="blog/Delete Blog.html"
    success_url=reverse_lazy("Thank You")

    def test_func(self,*args, **kwargs):
        post=Post.objects.get(slug=self.kwargs.get('slug'))
        if post.author==self.request.user:
            return True
        else:
            return False

# class ModelDeleteView(DeleteView):
#     model = Model
#     template_name = ".html"
