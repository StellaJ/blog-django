from django.shortcuts import render
from django.core.urlresolvers import reverse
import blog.views
import stelka.views 

def home(request):
	lista = {'blog' : reverse(blog.views.post_list), 'stelka' : reverse(stelka.views.something), 'admin' : reverse('admin:index')}
	lista2 = sorted(lista.items())
	return render(request, 'blog/home.html', {'lista' : lista2})
