from django.urls import path, include

from . import views

urlpatterns = [
    path('rocket-models/', views.RocketModelList.as_view()),
    path('rocket-models/<str:pk>/', views.RocketModelDetail.as_view()),
    path('boosters/', views.BoosterList.as_view()),
    path('boosters/<str:pk>/', views.BoosterDetail.as_view()),
    path('launch-platforms/', views.LaunchPlatformList.as_view()),
    path('launch-platforms/<str:pk>/', views.LaunchPlatformDetail.as_view()),
    path('payloads/', views.PayloadList.as_view()),
    path('payloads/<int:pk>/', views.PayloadDetail.as_view()),
    path('launches/', views.LaunchList.as_view()),
    path('launches/<int:pk>/', views.LaunchList.as_view()),
    path('token/', views.TokenList.as_view()),
    path('decomissions/', views.DecomissionList.as_view()),
]
