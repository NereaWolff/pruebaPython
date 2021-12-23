from django.db import models
from django.shortcuts import render
from django.http import Http404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Patente
from pruebaPython.serializers import PatenteSerializers
import string
import itertools


# Create your views here.

#ID
rec = 0
def autoIncrement():
    global rec
    pStart = 1
    pInterval = 1
    if (rec == 0):
        rec = pStart
    else:
        rec += pInterval
    return rec


#PATENTE
def custom_seq(letter=4, digits=3):
    alpha = string.ascii_uppercase
    digit = string.digits
    alpha_list = [alpha]*letter
    digit_list = [digit]*digits
    for i in itertools.product(*alpha_list):
        for j in itertools.product(*digit_list):
            yield "".join(i + j)


def createReg(request):
    p=Patente.objects.create(id=autoIncrement(),pat=custom_seq())
    p.save()
    return render(request)


class buscarPatente(APIView):

    def get_object(self, paten):
        try:
            return Patente.objects.get(pat=paten)
        except Patente.DoesNotExist:
            raise Http404

    def get(self, request, paten, format=None):
        post = self.get_object(paten)
        serializer = PatenteSerializers(post)  
        return Response(serializer.data)



class buscarID(APIView):
    def get_object(self, pk):
        try:
            return Patente.objects.get(pk=pk)
        except Patente.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PatenteSerializers(post)  
        return Response(serializer.data)


