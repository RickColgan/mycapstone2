from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import School, Athletes

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'MyCapstoneApp/index.html'
    context_object_name = 'school_list'

    def get_queryset(self):
        """Return the schools in the list"""
        return School.objects.order_by('name')


class DetailView(generic.DetailView):
    model = School
    template_name = 'MyCapstoneApp/detail.html'


class AthletesView(generic.ListView):
    model = Athletes
    context_object_name = 'school_list'
    template_name = 'MyCapstoneApp/athletes.html'

    def get_queryset(self):
        """Return the athletes in the list"""
        return Athletes.objects.get(schoolid=1)