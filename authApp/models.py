from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# sale_choices = (
#     ('y', 'yes'),
#     ('n', 'no'),
# )
class Service(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField()
    rate = models.IntegerField()
    image = models.FileField(upload_to='service/')