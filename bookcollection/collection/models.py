from django.db import models
from django.urls import reverse

class Book(models.Model):
	name = models.CharField(max_length=300)
	author = models.CharField(max_length=300,null=True, blank=True)
	year = models.IntegerField(null=True, blank=True)

	class Meta:
		ordering = ['name', 'year']

	def get_absolute_url(self):
		return reverse('book_detail', kwargs={"pk": self.pk})
	
	def __str__(self):
		return self.name
