from django.shortcuts import render, redirect
from django.views import View

from web.form import ReceiptForm


class ReceiptView(View):
    template_name = 'receipt.html'

    def get(self, request):
        form = ReceiptForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('receipt')
        return render(request, self.template_name, {'form': form})