from django.shortcuts import render

# Create your views here.
from django.views import View


class TesteView(View):
    def get(self, request):
        ctx = {

        }
        return render(request, 'teste.html', context=ctx)

