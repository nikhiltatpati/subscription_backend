from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SubscribeSerializer

from .models import Subscribe
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/subscribe-list/',
		'Detail View':'/subscribe-detail/<str:pk>/',
		'Create':'/subscribe-create/',
		'Update':'/subscribe-update/<str:pk>/',
		'Delete':'/subscribe-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def subscribeList(request):
	subscribes = Subscribe.objects.all().order_by('-id')
	serializer = SubscribeSerializer(subscribes, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def subscribeDetail(request, pk):
	subscribes = Subscribe.objects.get(id=pk)
	serializer = SubscribeSerializer(subscribes, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def subscribeCreate(request):
	serializer = SubscribeSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def subscribeUpdate(request, pk):
	subscribe = Subscribe.objects.get(id=pk)
	serializer = SubscribeSerializer(instance=subscribe, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def subscribeDelete(request, pk):
	Subscribe = Subscribe.objects.get(id=pk)
	Subscribe.delete()

	return Response('Item succsesfully delete!')



