from django import forms
from web.models.receipt import InsertReceipt


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = InsertReceipt
        fields = ['mba', 'item_id', 'container_id', 'ic_date', 'ic_code', 'from_mba',
                  'mdc', 'obl_code', 'to_mba', 'no_of_items', 'elt_code', 'uo2_wf',
                  'elt_wf', 'enr', 'iso_code', 'iso_wf', 'burnup', 'mb', 'product_images']
        widgets = {
            'ic_date': forms.DateInput(attrs={'type': 'date'}),
            'product_images': forms.ClearableFileInput(attrs={'multiple': True}),
        }
