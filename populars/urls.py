
from django.urls import path
from populars import views

urlpatterns = [
    path('populars/', views.PopularList.as_view()),
    path('populars/<int:pk>/', views.PopularDetail.as_view()),
]
