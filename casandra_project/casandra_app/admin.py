from django.contrib import admin
import uuid
from cassandra.cqlengine.columns import *

from .models import ExampleModel,Exampledata,bat
# from .models import bat
from cassandra.cqlengine import columns

# Register your models here.
admin.site.register(ExampleModel)
admin.site.register(Exampledata)
admin.site.register(bat)


 