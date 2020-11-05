from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
from database import models
from classViews import serializers as ser
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    content = {"message": "Welcome to the BookStore!"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def get_service_types(request):
    # user = request.user.id
    service_type = models.ServiceType.objects.all()
    serializer = ser.ServiceTypeSerializer(service_type, many=True)
    return JsonResponse({'services': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def add_service_type(request):
    # import pdb;pdb.set_trace()
    payload = json.loads(request.body)
    # user = request.user
    try:
        # serviceType = models.ServiceType.objects.get(id=payload["serviceType"])
        service_type = models.ServiceType.objects.create(
            name=payload["name"]
        )
        serializer = ser.ServiceTypeSerializer(service_type)
        return JsonResponse({'service_type': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def update_service_type(request, service_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        service_item = models.ServiceType.objects.filter(id=service_id)
        # returns 1 or 0
        service_item.update(**payload)
        service_type = models.ServiceType.objects.get(id=service_id)
        serializer = ser.ServiceTypeSerializer(service_type)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def delete_service_type(request, service_id):
    # user = request.user.id
    try:
        service_type = models.ServiceType.objects.get( id=service_id)
        service_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
