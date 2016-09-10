from django.http import HttpResponse
from django.shortcuts import render

from .models import Course

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    # render(<request object>, <template path>, <context dictionary>)
    return render(request, 'courses/course_list.html', {'courses': courses})

#  pk come from the url and represents the primary key for a given course
def course_detail(request, pk):
    #  django automatically knows that pk is out primary key and applies to the appropriate field in the course table
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

