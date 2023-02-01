from django import forms

from .models import Category


class ExpenseSearchForm(forms.Form):
    name = forms.CharField(required=False)
    fromdate = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)
    todate = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False)
    CHOICES = (('category', 'category'), ('date', 'date'),)
    order_by = forms.ChoiceField(choices=CHOICES, required=False)
    sort_descending = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False