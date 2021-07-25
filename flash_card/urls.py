from django.urls import path

from . import views

app_name = 'flash_card'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/editcard/', views.AddCardView.as_view(), name='editcard'),
]