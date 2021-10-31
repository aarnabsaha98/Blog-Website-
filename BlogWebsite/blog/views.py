from django.shortcuts import render , get_object_or_404
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView)
from .models import Post , Comment
from django.urls import reverse_lazy
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
# Create your views here.
#https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-editing/


class ReplyUserListView(ListView):
	model = Comment
	template_name = 'blog/leave_reply.html'
	#fields = ['author','date_posted','text_comment']
	context_object_name = 'comment'
	# comment  = Comment.objects.all()
	ordering = ['-date_posted']
class ReplyCreateView(LoginRequiredMixin,CreateView):
	# template_name = 'blog/leave_reply.html'
	model = Comment
	fields = ['text_comment']
	success_url =  '/leave-reply/'
	def form_valid(self,form):
	# This method is called when valid form data has been POSTed.
       # It should return an HttpResponse.
		form.instance.author = self.request.user
		return super().form_valid(form) 
# this is for post view
class PostListView(ListView):
	model = Post
	 # <app>/<model>_<viewtype>.html
	template_name = 'blog/home.html'

	# now as this will give us a listObject and our templates named as 
	# posts !    so our app wont render a single post for this
	# so we create a variable >>> context_object_name
	context_object_name = 'posts'

	# To change the ordering of the posts > latest post are on the top 
	# and old ones are bottom >>
	ordering = ['-date_posted']
	paginate_by = 5
	
class UserPostListView(ListView):
	model = Post
	 # <app>/<model>_<viewtype>.html
	template_name = 'blog/user_post.html'

	# now as this will give us a listObject and our templates named as 
	# posts !    so our app wont render a single post for this
	# so we create a variable >>> context_object_name
	context_object_name = 'posts'

	# To change the ordering of the posts > latest post are on the top 
	# and old ones are bottom >>
	ordering = ['-date_posted']
	paginate_by = 5

	#Reverse for 'user_posts' with no arguments not found. 1 pattern(s) tried: ['user/(?P<username>[^/]+)$']
		# to  over write this error 
	def get_queryset(self):
		# this will fetch out the user name form the url
		user = get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('date_posted')

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','content']
	success_url = '/'
	# as of now we dont have the author specifed with the create post
	# form , so we need to validate the form and set the author request to the foem
	# instace of author
	def form_valid(self,form):
	# This method is called when valid form data has been POSTed.
       # It should return an HttpResponse.
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
	model = Post
	fields = ['title','content']
	# as of now we dont have the author specifed with the create post
	# form , so we need to validate the form and set the author request to the foem
	# instace of author
	def form_valid(self,form):
	# This method is called when valid form data has been POSTed.
       # It should return an HttpResponse.
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
	return render(request ,'blog/about.html',{'title' : 'About'})


def topic(request):
	return HttpResponse('<h1>hello </h1>')


# CREATE - UPDATE - DELETE

