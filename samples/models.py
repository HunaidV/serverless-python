from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

Category = [
	('contentwriting', 'Content Writing'),
	('webdevelopment', 'Web Development'),
	('graphicsdesigning' ,' Graphics Designing' ),
	('Architecturedesigning', ' Architecture Designing' ),
  ('Assignment Writing', 'Assignment Writing' ),

	] 
class SampleModel(models.Model):
	title	= models.CharField(max_length=60)
	category = models.CharField(max_length=50, choices=Category,default="Content Writing")
	content = models.CharField(max_length=254, null=True, blank=True)
	pdf		= models.FileField(upload_to="pdf/")
	timestamp = models.DateTimeField(auto_now_add=True)
	updated		= models.DateTimeField(auto_now=True)
	slug 		= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.title

def Sample_presave( sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(Sample_presave, sender=SampleModel)