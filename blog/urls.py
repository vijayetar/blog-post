from django.urls import path
from .views import HomePageView, DetailBlogView

urlpatterns = [
	path("", HomePageView.as_view(), name = 'home'),
	path('blog_details/<int:pk>',DetailBlogView.as_view(), name='blog_details')
]
