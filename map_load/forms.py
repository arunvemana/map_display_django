from django.forms import ModelForm
from .models import Map_List

class New_Map_List(ModelForm):
    class Meta:
        model = Map_List
        fields = ['location_name','map_coordinates_link']