from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# this is request handler function, not something the user can actually see

def say_hello(request):
# its possible to pull data from the data base
# transform data, send email, etc
# in this case will return a simple response

return HttpResponse('Hello World')



