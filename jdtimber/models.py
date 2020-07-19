from django.db import models

# Create your models here.
class InquiryModel(models.Model):
	name = models.CharField(max_length=200)
	business = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	logs = models.CharField(max_length=200)
	veneers = models.CharField(max_length=200)
	decking = models.CharField(max_length=200)
	boards = models.CharField(max_length=200)
	flooring = models.CharField(max_length=200)
	skirtings = models.CharField(max_length=200)

	def __str__(self):
		return self.name