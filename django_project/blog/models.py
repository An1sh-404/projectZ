from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class EmployeeData(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20,default="Unknown")
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length=20)
    province = models.CharField(max_length = 20)
    country = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __str__(self):
        return self.first_name
    
    def get_absolute_url(self):
        return reverse('record_detail', kwargs={'pk': self.pk})