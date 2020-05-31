from django.shortcuts import render
from django.http import HttpResponse
from .models import Map_List, predict_Map_List
from .forms import New_Map_List


# Create your views here.

def index(request):
    if request.method == "GET":
        city_list = Map_List.objects.all().values('location_name')
        predict_city_list = predict_Map_List.objects.all().values('location_name')
        map_location = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d21101.7937618636!2d144.55494060753412!3d-38.168077879974085!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad43ba8d1b8dcb7%3A0x1d04567609f51d80!2sDrysdale!5e0!3m2!1sen!2sin!4v1590561456858!5m2!1sen!2sin"
        return render(request, 'index.html', context={'city_list': city_list, 'map_location': map_location,
                                                      'predict_map_list': predict_city_list})
    elif request.method == "POST":
        var = request.POST['location_select']
        print("hello")
        City_value = Map_List.objects.get(location_name=var)
        print(City_value.map_coordinates_link)
        city_list = Map_List.objects.all().values('location_name')
        predict_city_list = predict_Map_List.objects.all().values('location_name')

        return render(request, 'index.html',
                      context={'city_list': city_list, 'map_location': City_value.map_coordinates_link.strip('"'),
                               'predict_map_list': predict_city_list,'selected_current_name':var})


def predit_map_load(request):
    if request.method == "GET":
        city_list = Map_List.objects.all().values('location_name')
        predict_city_value = predict_Map_List.objects.all().values('location_name')
        map_location = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d21101.7937618636!2d144.55494060753412!3d-38.168077879974085!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad43ba8d1b8dcb7%3A0x1d04567609f51d80!2sDrysdale!5e0!3m2!1sen!2sin!4v1590561456858!5m2!1sen!2sin"
        return render(request, 'index.html', context={'predict_map_list': predict_city_value, 'city_list': city_list,
                                                      'map_location': map_location})

    elif request.method == "POST":
        var = request.POST['predict_location_select']
        city_list = Map_List.objects.all().values('location_name')
        predict_city_value = predict_Map_List.objects.get(location_name=var)
        predict_city_list = predict_Map_List.objects.all().values('location_name')
        return render(request, 'index.html', context={'predict_map_list': predict_city_list,
                                                      'map_location': predict_city_value.map_coordinates_link.strip(
                                                          '"'), 'city_list': city_list,'selected_predict_name':var})


def add_map(request):
    if request.method == "GET":
        form = New_Map_List()
        return render(request, 'new_map.html', context={'form': form})
    if request.method == "POST":
        form = New_Map_List()
        print(f'"{request.POST["map_coordinates_link"]}"')
        save_data = New_Map_List(request.POST)
        if save_data.is_valid():
            save_data.save()
        return render(request, 'new_map.html', context={'form': form})
