from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from blogs.models import Post
from .form import *
from .models import UserProfile

class RegisterView(CreateView):
    template_name="users/register.html"

    form_class=RegisterForm

    def get_success_url(self):

        return reverse("users:login")

class UserLogin(LoginView):
    template_name="users/login.html"


class UserLogout(LogoutView):
    template_name="users/login.html"   

@method_decorator(login_required(login_url="users/login"),name="dispatch")
class UserProfileUpdateView(UpdateView):
    model=UserProfile
    template_name="users/profile_update.html"
    form_class=UserProfileForm

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(UserProfileUpdateView,self).form_valid(form)
    def get_success_url(self):

        return reverse("users:update_profile",kwargs={"slug":self.object.slug})

    def get(self,request,*args,**kwargs):
        self.object=self.get_object()

        if self.object.user != request.user:
            return HttpResponseRedirect("/")

        return super(UserProfileUpdateView,self).get(request,*args,**kwargs)

@method_decorator(login_required(login_url="users/login"),name="dispatch")
class UserProfileView(ListView):
    template_name="users/my_profile.html"
    model=Post
    context_object_name="userposts"
    paginate_by=5

    def get_context_data(self,**kwargs):
        context=super(UserProfileView,self).get_context_data(**kwargs)
        context["userprofile"]=UserProfile.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by("-id")    

class UserListView(ListView):
    template_name="users/user_list.html"