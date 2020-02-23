from django.urls import path

from . import views

app_name = "demoapp"

urlpatterns = [
    path('', views.PostListView.as_view(), name="list"),
    path('<int:pk>/', views.PostDetailView.as_view(), name="detail"),
]
