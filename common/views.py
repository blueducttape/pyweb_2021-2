from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class HelloWorld(View):
    def get(self,request):
        return HttpResponse("""<h1>Hello, World</h1>""")


class IndexView(View):
    def get (self, request):
        return render(request, "common/index.html")