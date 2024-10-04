from django.shortcuts import render
from django.views import View


class Chart(View):
    def get(self, request):
        return render(request, 'echartjs.html')