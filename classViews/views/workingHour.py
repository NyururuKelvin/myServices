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
def get_working_hours(request):
    # user = request.user.id
    working_hour = models.WorkingHour.objects.all()
    serializer = ser.WorkingHourSerializer(working_hour, many=True)
    return JsonResponse({'working_hours': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def add_working_hour(request):
    payload = json.loads(request.body)
    # user = request.user
    # import pdb;pdb.set_trace()
    try:
        # companyType = models.ServiceType.objects.get(id=payload["companyType"])
        working_hour = models.WorkingHour.objects.create(
            name=payload["name"],
            email=payload["email"],
            description=payload['description'],
        )
        serializer = ser.WorkingHourSerializer(working_hour)
        return JsonResponse({'working_hour': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def update_working_hour(request, working_hour_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        company_item = models.WorkingHour.objects.filter(id=working_hour_id)
        # returns 1 or 0
        company_item.update(**payload)
        working_hour = models.WorkingHour.objects.get(id=working_hour_id)
        serializer = ser.WorkingHourSerializer(working_hour)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def delete_working_hour(request, working_hour_id):
    # user = request.user.id
    try:
        working_hour = models.WorkingHour.objects.get( id=working_hour_id)
        working_hour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
