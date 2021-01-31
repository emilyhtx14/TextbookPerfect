from django.db import models

# Create your models here.
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/my_sell/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}my_sell/'.format(settings.MEDIA_URL),
)

def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
    return u'picture/{0}'.format(filename)

class Account(models.Model):
    type = models.CharField(max_length=100, default='Checking')
    name = models.CharField(max_length=100, default='')
    rewards = models.DecimalField(decimal_places = 2, max_digits = 200, default=10000.00)
    balance = models.DecimalField(decimal_places = 2, max_digits = 200, default=10000.00)


class BookUpload(models.Model):
    user_id =  models.CharField(max_length=100, default='')
    title = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    price = models.DecimalField(decimal_places = 2, max_digits = 200)
    shipping = models.DecimalField(decimal_places = 2, max_digits = 200)
    picture = models.ImageField(upload_to=image_directory_path, storage=image_storage)

class BookDisplay(models.Model):
    name = models.CharField(max_length=100, default='')