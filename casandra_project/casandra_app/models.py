from django.db import models

import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.columns import *
from django_cassandra_engine.models import DjangoCassandraModel
 

class ExampleModel(DjangoCassandraModel):
    example_id  = columns.UUID(primary_key=True, default=uuid.uuid4)
    name	   	= columns.Text(required=False)
    fname	   	= columns.Text(required=False)
    description = columns.Text(required=False)

    def __str__(self):
    	return self.name


class Exampledata(DjangoCassandraModel):
    example_id  = columns.UUID(primary_key=True, default=uuid.uuid4)
    name	   	= columns.Text(required=False)
    fname	   	= columns.Text(required=False)
    description = columns.Text(required=False)


    def __str__(self):
    	return self.name


class bat(DjangoCassandraModel):
    pk 			= columns.UUID(primary_key=True, default=uuid.uuid4)
    lavel	   	= columns.Text(required=False)
    valuea	   	= columns.Text(required=False)
    valueb	   	= columns.Text(required=False)
    valuec 		= columns.Text(required=False)

    def __str__(self):
    	return self.lavel

    # def delete(self, *args, **kwargs):
    # 	self.pk.delete()
    # 	super().delete(*args, **kwargs)