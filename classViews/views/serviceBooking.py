from django.contrib.auth.models import User
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
def get_service_booking(request):
    # user = request.user.id
    service_booking = models.ServiceBooking.objects.all()
    serializer = ser.ServiceBookingSerializer(service_booking, many=True)
    return JsonResponse({'service_bookings': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def add_service_booking(request):
    payload = json.loads(request.body)
    # user = request.user
    # import pdb;pdb.set_trace()
    try:
        # import pdb;pdb.set_trace()
        user = User.objects.get(id=payload['user'])
        service = models.CompanyService.objects.get(id=payload["service"])
        service_booking = models.ServiceBooking.objects.create(
            user=user,
            service=service,
            status=payload['status']

        )
        serializer = ser.ServiceBookingSerializer(service_booking)
        return JsonResponse({'service_booking': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def update_service_booking(request, service_booking_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        company_item = models.ServiceBooking.objects.filter(id=service_booking_id)
        # returns 1 or 0
        company_item.update(**payload)
        service_booking = models.ServiceBooking.objects.get(id=service_booking_id)
        serializer = ser.ServiceBookingSerializer(service_booking)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def delete_service_booking(request, service_booking_id):
    # user = request.user.id
    try:
        service_booking = models.ServiceBooking.objects.get( id=service_booking_id)
        service_booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
