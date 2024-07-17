# from django.shortcuts import render
from django.http import Http404
from .models import Course
from django.shortcuts import render

# Create your views here.

def index(request):
  courses = Course.objects.all()
  return render(request, 'courses.html', {'courses': courses})

def single_course(request, course_id):
  try:
    course = Course.objects.get(pk=course_id)
    return render(request, 'single_course.html', {'course': course})
  except Course.DoesNotExist:
    raise Http404