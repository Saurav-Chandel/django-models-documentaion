from time import time
from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=10)
    age=models.CharField(max_length=100,db_column='age1',null=True,blank=True)

class Album(models.Model):
    name=models.CharField(max_length=100)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)    

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
   
    '''PROTECT¶
       Prevent deletion of the referenced object by raising ProtectedError, a subclass of django.db.IntegrityError.
    '''
    album = models.ForeignKey(Album, on_delete=models.PROTECT)

    '''
    RESTRICT¶
       Prevent deletion of the referenced object by raising RestrictedError (a subclass of django.db.IntegrityError). Unlike PROTECT, deletion of the referenced object is allowed if it also references a different object that is being deleted in the same operation, but via a CASCADE relationship.
    '''
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)


 #testing unique_for_date,unique_for_month,uniqu_for_year
from datetime import datetime, timedelta, timezone, tzinfo
import django
class Post(models.Model):
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('suspended', 'Suspended'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_year='publish')   
    status = models.CharField(max_length=15,
                              choices=STATUS_CHOICES,
                              default='draft')
    content = models.TextField(max_length=200000, blank=True)
    # dates
    created = models.DateTimeField(auto_now_add=True)     
    updated = models.DateTimeField(auto_now=True)    #when ever u updated your models time willbe change accordingly.
    publish = models.DateTimeField(default=django.utils.timezone.now)  #server time


# Field.validators¶
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
        if value % 2 != 0:
          raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

import uuid
class MyModel(models.Model):

    out = models.DateTimeField(null=True, help_text="When the cow went OUT TO Pasture.")
    _in = models.DateTimeField(null=True, help_text="When the cow got back IN FROM Pasture.")

    duration = models.DurationField(null=True,blank=True)
    # id = models.AutoField(primary_key=True)
    even_field = models.IntegerField(validators=[validate_even])
    uiid1=models.UUIDField(default=uuid.uuid4,primary_key=True)
    uiid2=models.UUIDField(default=uuid.uuid4)

    def save(self, *args, **kwargs):
        """
        Should set duration field to total time between out and in data.
        """
        self.duration = self._in - self.out
        super(MyModel, self).save(*args, **kwargs)