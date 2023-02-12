from django.http import HttpResponse


def home_page(request):
    print("Home page")
    return HttpResponse("<h1>Welcome to Home Page </h1>")
