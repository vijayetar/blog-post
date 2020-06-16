from django.shortcuts import render
from .models import Post
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

class HomePageView(ListView):
	template_name = 'home.html'
	model = Post

class DetailBlogView(DetailView):
	template_name = 'details.html'
	model = Post