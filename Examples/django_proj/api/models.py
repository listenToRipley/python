from tastypie.resources import ModelResource
from shop.models import Category, Course

# Create your models here.

# END POINTS goals
# /api/categories/$id/
# /api/courses/$id/

# This class will providing to categories in the db
class CategoryResource(ModelResource):
  class Meta: # attributes for the resource
    queryset = Category.objects.all() # get content of model
    resource_name = 'categories' # what resource are we accessing?
    allowed_methods = ['get']# what can we do with that resource? (by html methods)


class CourseResource(ModelResource):
  class Meta:
    queryset = Course.objects.all()
    resource_name = 'course'
    allow_method = ['get', 'delete', 'post']