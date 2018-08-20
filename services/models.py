from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
# Create your models here.

class ServiceModel(models.Model):
	Servicename		= models.CharField(max_length=100, null=False, blank=False)
	Description		= models.CharField(max_length=500, null=False, blank=False,)
	description_long		= models.CharField(max_length=3000, null=False, blank=False, default="IT should be long description")
	image 			= models.ImageField(upload_to='service/', null=True, blank=False, )
	image_big		= models.ImageField(upload_to='service/big', null=True, blank=False, )
	Point1			= models.CharField(max_length=254, null=True, blank=True)
	Description1	= models.CharField(max_length=500, null=True, blank=True, default="Description of above service")
	Point2			= models.CharField(max_length=254, null=True, blank=True)
	Description2	= models.CharField(max_length=500, null=True, blank=True, default="Description of above service")
	Point3			= models.CharField(max_length=254, null=True, blank=True)
	Description3	= models.CharField(max_length=500, null=True, blank=True, default="Description of above service")
	Point4			= models.CharField(max_length=254, null=True, blank=True)
	Description4	= models.CharField(max_length=500, null=True, blank=True, default="Description of above service")
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	slug			= models.SlugField(null=True, blank=True)
	def __str__(self):
		return self.Servicename

	class Meta:
		ordering = ['-updated', 'timestamp']


def Service_presave(sender, instance, *args, **kwargs ):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


pre_save.connect(Service_presave, sender=ServiceModel)