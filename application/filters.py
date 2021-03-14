import django_filters
from .models import Application


class AppFilter(django_filters.FilterSet):
    comment = django_filters.CharFilter(label='Комментарий', field_name='comment', lookup_expr='icontains')

    class Meta:
        model = Application
        fields = ('product', 'phone', 'decision', 'comment')
