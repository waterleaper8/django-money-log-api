# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers, viewsets
from rest_framework import generics
from .serializers import BillSerializer, UserSerializer, GetUserSerializer, PocketSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import permissions
from .models import Bill, User, Pocket
from django.http import HttpResponse
from rest_framework.response import Response

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetUserSerializer
    queryset = User.objects.all()
    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

class BillViewSet(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    queryset = Bill.objects.order_by('-date' ,'-created_at').all()

    def get_queryset(self):
        return self.queryset.filter(create_user=self.request.user)

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.create_user=self.request.user
        qryset.save()
        print(qryset)
        return HttpResponse('FormValid')


class PocketViewSet(viewsets.ModelViewSet):
    serializer_class = PocketSerializer
    queryset = Pocket.objects.all()

    def get_queryset(self):
        return self.queryset.filter(create_user=self.request.user)

    def form_valid(self, form):
        qryset = form.save(commit=False)
        qryset.create_user=self.request.user
        qryset.save()
        print(qryset)
        return HttpResponse('FormValid')

    def list(self, request):
        queryset = Pocket.objects.all()
        serializer = PocketSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)
