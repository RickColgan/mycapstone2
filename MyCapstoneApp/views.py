from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import School

# Create your views here.
def index(request):
    school_list = School.objects.order_by('name')
    context = {
        'school_list': school_list,
    }
    return render(request, 'MyCapstoneApp/index.html', context)

def school_detail(request, school_id):
    return HttpResponse('This is school %s.' % school_id)

def school_athletes(request, school_id):
    return HttpResponse('These athletes compete for %s:' % school_id)