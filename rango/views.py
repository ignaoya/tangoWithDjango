from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #construct a dictionary to pass to the template engine as its context.
    #Note the key boldmessage is the same as in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    #Return a rendered response to send to the client.
    #We make use of the shortcut function to make our lives easier.
    #Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    #construct a dictionary to pass to the template engine as its context.
    context_dict = {'introduction': "This tutorial has been put together by me."}

    #return a rendered response to send to the  client.
    return render(request, 'rango/about.html', context=context_dict)
