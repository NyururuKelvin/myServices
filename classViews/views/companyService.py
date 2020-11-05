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
def get_company_services(request):
    # user = request.user.id
    company_service = models.CompanyService.objects.all()
    serializer = ser.CompanyServiceSerializer(company_service, many=True)
    return JsonResponse({'companies': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def add_company_service(request):
    payload = json.loads(request.body)
    # user = request.user
    # import pdb;pdb.set_trace()
    try:
        service = models.Service.objects.get(id=payload["service"])
        company = models.Company.objects.get(id=payload['company'])
        company_service = models.CompanyService.objects.create(
            price=payload["price"],
            description=payload['description'],
            service=service,
            company=company
        )
        serializer = ser.CompanyServiceSerializer(company_service)
        return JsonResponse({'company_service': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def update_company_service(request, company_service_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        company_item = models.CompanyService.objects.filter(id=company_service_id)

        company_item.update(**payload)
        company_service = models.CompanyService.objects.get(id=company_service_id)
        serializer = ser.CompanyServiceSerializer(company_service)
        return JsonResponse({'company_service': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def delete_company_service(request, company_service_id):
    # user = request.user.id
    try:
        company_service = models.CompanyService.objects.get( id=company_service_id)
        company_service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
