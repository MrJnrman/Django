from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Course, Step

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    email = 'questions@learning_site.com'
    # render(<request object>, <template path>, <context dictionary>)
    return render(request, 'courses/course_list.html', {'courses': courses, 'email': email})

#  pk come from the url and represents the primary key for a given course
def course_detail(request, pk):
    #  django automatically knows that pk is out primary key and applies to the appropriate field in the course table
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})

