
import uuid
import random

from django.db.models.deletion import ProtectedError
from django.db import transaction
from django.http.response import HttpResponse, JsonResponse

from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser

from rest_framework_condition import etag

from . import models
from . import serializers


def rocket_model_etag(request, pk, *args, **kwargs):
    model = models.RocketModel.objects.filter(model=pk).first()
    return model.hash() if model else None


def booster_etag(request, pk, *args, **kwargs):
    model = models.Booster.objects.filter(code=pk).first()
    return model.hash() if model else None


def launch_platform_etag(request, pk, *args, **kwargs):
    model = models.LaunchPlatform.objects.filter(code=pk).first()
    return model.hash() if model else None


def payload_etag(request, pk, *args, **kwargs):
    model = models.Payload.objects.filter(id=pk).first()
    return model.hash() if model else None


def launch_etag(request, pk, *args, **kwargs):
    model = models.Launch.objects.filter(id=pk).first()
    return model.hash() if model else None


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


def check_precondition(request, model) -> HttpResponse:
    e = request.headers['If-Match'] if 'If-Match' in request.headers.keys() else None
    if not e:
        return HttpResponse(status=status.HTTP_403_FORBIDDEN)

    if not model:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if model.hash() != e:
        return HttpResponse(status=status.HTTP_412_PRECONDITION_FAILED)

    return None


class RocketModelList(generics.ListCreateAPIView):
    queryset = models.RocketModel.objects.all()
    serializer_class = serializers.RocketModelSerializer
    pagination_class = StandardResultsSetPagination


class RocketModelDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = models.RocketModel.objects.all()
    serializer_class = serializers.RocketModelSerializer

    @ etag(rocket_model_etag)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        model = models.RocketModel.objects.filter(model=pk).first()
        precondition = check_precondition(request, model)
        if precondition:
            return precondition

        return self.update(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        model = models.RocketModel.objects.filter(model=pk).first()
        precondition = check_precondition(request, model)
        if precondition:
            return precondition

        try:
            model.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BoosterList(generics.ListCreateAPIView):
    queryset = models.Booster.objects.all()
    serializer_class = serializers.BoosterSerializer
    pagination_class = StandardResultsSetPagination


class BoosterDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = models.Booster.objects.all()
    serializer_class = serializers.BoosterSerializer

    @ etag(booster_etag)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        model = models.Booster.objects.filter(code=pk).first()
        precondition = check_precondition(request, model)
        if precondition:
            return precondition

        return self.update(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        model = models.Booster.objects.filter(code=pk).first()
        precondition = check_precondition(request, model)
        if precondition:
            return precondition

        try:
            model.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LaunchPlatformList(generics.ListCreateAPIView):
    queryset = models.LaunchPlatform.objects.all()
    serializer_class = serializers.LaunchPlatformSerializer
    pagination_class = StandardResultsSetPagination


class LaunchPlatformDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = models.LaunchPlatform.objects.all()
    serializer_class = serializers.LaunchPlatformSerializer

    @ etag(launch_platform_etag)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        model = models.LaunchPlatform.objects.filter(code=pk).first()
        precondition = check_precondition(request, model)
        if precondition:
            return precondition

        return self.update(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        model = models.LaunchPlatform.objects.filter(code=pk).first()
        precondition = check_precondition(request, model)
        if precondition:
            return precondition

        try:
            model.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PayloadList(generics.ListCreateAPIView):
    queryset = models.Payload.objects.all()
    serializer_class = serializers.PayloadSerializer
    pagination_class = StandardResultsSetPagination


class PayloadDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = models.Payload.objects.all()
    serializer_class = serializers.PayloadSerializer

    @ etag(payload_etag)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        model = models.Payload.objects.filter(id=pk).first()
        precondition = check_precondition(request, model)
        if precondition:
            return precondition

        return self.update(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        model = models.Payload.objects.filter(id=pk).first()
        precondition = check_precondition(request, model)
        if precondition:
            return precondition

        try:
            model.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LaunchList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = models.Launch.objects.all()
    serializer_class = serializers.LaunchSerializer
    pagination_class = StandardResultsSetPagination
    parser_classes = (MultiPartParser, )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        token = request.headers['Token'] if 'Token' in request.headers else None
        if not token:
            return JsonResponse({"error": "Token is not present"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        t = models.Token.objects.filter(token=token).first()
        if not t:
            return JsonResponse({"error": "Invalid Token"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        serializer = serializers.LaunchSerializer(data=request.data)
        if serializer.is_valid():
            booster = models.Booster.objects.get(code=request.data['booster'])
            if booster.expended:
                return JsonResponse({"error": "booster is expended"}, status=status.HTTP_400_BAD_REQUEST)

            model = booster.model
            if not model.reusable or random.random() > 0.90:
                booster.expended = True
            booster.launches_count += 1

            payload = models.Payload.objects.get(id=request.data['payload'])
            if payload.delivered:
                return JsonResponse({"error": "payload is already delivered"}, status=status.HTTP_400_BAD_REQUEST)
            payload.delivered = True

            with transaction.atomic():
                t.delete()
                payload.save()
                booster.save()
                serializer.save()

            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class LaunchDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = models.Launch.objects.all()
    serializer_class = serializers.LaunchSerializer

    @ etag(launch_etag)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        model = models.Launch.objects.filter(id=pk).first()
        precondition = check_precondition(request, model)
        if precondition:
            return precondition

        return self.update(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        model = models.Launch.objects.filter(id=pk).first()
        precondition = check_precondition(request, model)
        if precondition:
            return precondition

        try:
            model.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TokenList(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = models.Token.objects.all()
    serializer_class = serializers.TokenSerializer

    def post(self, request, *args, **kwargs):
        t = models.Token.objects.create(token=uuid.uuid4())
        s = serializers.TokenSerializer(t)
        return JsonResponse(s.data, status=status.HTTP_201_CREATED)
