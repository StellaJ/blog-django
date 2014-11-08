from django.shortcuts import render

def something(request):

    return render(request, 'stelka/something.html', {})
# Create your views here.
