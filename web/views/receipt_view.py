from django.shortcuts import render, redirect
from django.views import View

from web.form.ReceiptForm import ReceiptForm


class Receipt(View):
    def get(self, request):
        form = ReceiptForm
        return render(request, 'receipt.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('conf:farhad')  # به صفحه‌ای هدایت می‌شوید پس از موفقیت
        return render(request, 'receipt.html', {'form': form})
