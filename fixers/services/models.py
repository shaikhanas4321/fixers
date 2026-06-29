from django.db import models
from django.conf import settings
# Create your models here.
class skills(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class service_request(models.Model):
    customer=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE ,related_name="sent_requests")
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="received_requests")
    status_choices = [
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
    ('expired', 'Expired'),
]
    status = models.CharField(max_length=20,choices=status_choices,default="pending")
    created_at = models.DateTimeField(auto_now_add=True)