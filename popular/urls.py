from django.urls import path
from popular import views

urlpatterns = [
    path('popular/', views.PopularList.as_view()),
    path('popular/<int:pk>/', views.PopularDetail.as_view()),
]
