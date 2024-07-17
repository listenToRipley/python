from django.urls import path
# import all views and this will allow access to all views started in that doc
from . import views 

urlpatterns = [
  # this first path is empty since this the root for this package
  path('',  views.index),
  path('<int:course_id>', views.single_course)
]