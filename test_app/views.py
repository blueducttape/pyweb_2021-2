from django.shortcuts import render
from datetime import datetime
from django.views import View
from django.http import HttpRequest, HttpResponse
from random import random


class DatetimeView(View):
    def get(self, request:HttpRequest) -> HttpResponse:
        now = f"{datetime.now()}"
        return HttpResponse(now)


class RandomNumberView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        random_number = random()
        return HttpResponse(random_number)

