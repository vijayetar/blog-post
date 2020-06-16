from django.shortcuts import render
from .models import Post
# Create your views here.
from django.views.generic import TemplateView, ListView

class HomePageView(ListView):
	template_name = 'home.html'
	model = Post
