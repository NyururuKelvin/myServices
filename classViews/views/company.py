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
def get_companies(request):
    # user = request.user.id
    company = models.Company.objects.all()
    serializer = ser.CompanySerializer(company, many=True)
    return JsonResponse({'companies': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def add_company(request):
    payload = json.loads(request.body)
    # user = request.user
    # import pdb;pdb.set_trace()
    try:
        # companyType = models.ServiceType.objects.get(id=payload["companyType"])
        company = models.Company.objects.create(
            name=payload["name"],
            email=payload["email"],
            description=payload['description'],
        )
        serializer = ser.CompanySerializer(company)
        return JsonResponse({'company': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def update_company(request, company_id):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        company_item = models.Company.objects.filter(id=company_id)
        # returns 1 or 0
        company_item.update(**payload)
        company = models.Company.objects.get(id=company_id)
        serializer = ser.CompanySerializer(company)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def delete_company(request, company_id):
    # user = request.user.id
    try:
        company = models.Company.objects.get( id=company_id)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
