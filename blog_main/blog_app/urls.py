from django.urls import path
from .import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:post_id>/", views.post_detail, name="post_detail"),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]
