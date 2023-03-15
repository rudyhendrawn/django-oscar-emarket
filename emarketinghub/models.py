from django.db import models

# Create your models here.
class EmarketingHub(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)
	manager = models.CharField(max_length=255, blank=True, null=True)
	city = models.CharField(max_length=255, blank=True, null=True)

class Meta:
	app_label = 'emarketinghub'
