from django.http import HttpResponse
from django.shortcuts import render

from .models import Course

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    # render(<request object>, <template path>, <context dictionary>)
    return render(request, 'courses/course_list.html', {'courses': courses})


