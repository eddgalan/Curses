from django.shortcuts import render

# Create your views here.
def my_view(request):
    cars = [
        {"name": "BMW"},
        {"name": "Sonic"},
    ]

    context = {
        "car_list": cars
    }

    return render(request, 'my_first_app/car_list.html', context)
