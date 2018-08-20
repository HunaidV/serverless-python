from django.db import models
from django.db.models.signals import pre_save
# Create your models here.
from .utils import unique_slug_generator
class BLOGMODEL(models.Model):
	Category	= models.CharField(max_length=30)
	title		= models.CharField(max_length=254)
	authorname  = models.CharField(max_length=25, default="Divya")
	content		= models.TextField(max_length=5999, null=True, blank=True)
	image 		= models.ImageField(upload_to='blog/', null=True, blank=True, )
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated		= models.DateTimeField(auto_now=True)
	slug		= models.SlugField(max_length=255,null=True, blank=True)

	def __str__(self):
		return self.title

	

def Slug_pre_save(sender, instance, *args, **kwargs ):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


pre_save.connect(Slug_pre_save, sender=BLOGMODEL)