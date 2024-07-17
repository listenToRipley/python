# from django.shortcuts import render
# from django.http import HttpRequest
from django.http import Http404
from .models import Course
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
  courses = Course.objects.all()
  return render(request, 'courses.html', {'courses': courses})

def single_course(request, course_id):
  #OPTION 1
  # try:
  #   course = Course.objects.get(pk=course_id)
  #   return render(request, 'single_course.html', {'course': course})
  # except Course.DoesNotExist:
  #   raise Http404
  
  # OPTION 2 - give context to error
  course = get_object_or_404(Course, pk=course_id)
  return render(request, 'single_course.html', {'course': course})