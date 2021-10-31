import django_filters
from django_filters import filters
from .models import Product, Category
from django import forms
def filter_not_empty(queryset, name, value):
    lookup = '__'.join([name, 'isnull'])
    return queryset.filter(**{lookup: False})

class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    ordering = filters.OrderingFilter(
                fields=(
            ('price', 'price'),
            ('name', 'name'),
        ),
)
    name = django_filters.CharFilter(lookup_expr='icontains')
    old_price = django_filters.BooleanFilter(field_name='old_price', method=filter_not_empty)
    # category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),
    #     widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Product
        fields = ['name', 'category', 'new', 'price', 'gamme',  'reference','tag']

