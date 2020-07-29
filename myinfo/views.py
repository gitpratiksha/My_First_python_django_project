from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Pratiksha Shivaji Indalkar\nStarted Career in python django\nyippee....",content_type="text/plain")

