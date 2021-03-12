from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('subscribe-list/', views.subscribeList, name="subscribe-list"),
	path('subscribe-detail/<str:pk>/', views.subscribeDetail, name="subscribe-detail"),
	path('subscribe-create/', views.subscribeCreate, name="subscribe-create"),

	path('subscribe-update/<str:pk>/', views.subscribeUpdate, name="subscribe-update"),
	path('subscribe-delete/<str:pk>/', views.subscribeDelete, name="subscribe-delete"),
]
