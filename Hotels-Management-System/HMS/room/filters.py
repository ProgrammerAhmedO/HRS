import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class RoomFilter(django_filters.FilterSet):
	price = DateFilter(field_name="price", lookup_expr='gte')
	roomType = DateFilter(field_name="roomType", lookup_expr='icontains')
	hotel_name = CharFilter(field_name='hotel', lookup_expr='icontains')


	class Meta:
		model = Room
		fields = '__all__'
		exclude = ['price', 'roomType', 'hotel_name']