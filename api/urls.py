from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('subscribe-list/', views.subscribeList, name="subscribe-list"),
	path('subscribe-create/', views.subscribeCreate, name="subscribe-create"),
]
