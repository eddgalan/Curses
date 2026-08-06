from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView


class CarListView(TemplateView):
    template_name = 'my_first_app/car_list.html'

    def get_context_data(self):
        cars = [
            {"name": "BMW"},
            {"name": "Sonic"},
        ]

        return {
            "car_list": cars
        }

def my_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")