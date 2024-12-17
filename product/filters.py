from django import forms
import django_filters
from product.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        label="Nome",
        lookup_expr='icontains',
    )
    date = django_filters.DateFilter(
        label='Data',
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        lookup_expr='exact',
    )
    category = django_filters.ModelChoiceFilter(
        queryset=Product.objects.values_list('category', flat=True).distinct(),
        label='Categoria',
    )
    price = django_filters.RangeFilter(
        label="Preço",
        widget=django_filters.widgets.RangeWidget(attrs={'class': 'price-range'}),
    )
    available = django_filters.BooleanFilter(
        label="Disponível",
        widget=forms.CheckboxInput,
    )

    class Meta:
        model = Product
        fields = ['name', 'category', 'date', 'available', 'price']
