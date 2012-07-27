from django.db import models
from django.contrib.auth.models import User

# TODO - Implement tags. (look at db_info.doc)

# Constants for lengths used
ADDRESS_LENGTH = 100
CITY_LENGTH = 50
ZIP_LENGTH = 10
STATE_LENGTH = 20

#The attractions
class Attraction(models.Model):
    name = models.CharField("Attraction Name", max_length=90)
    latitude = models.DecimalField(max_digits=10, decimal_places=2)
    longitude = models.DecimalField(max_digits=10, decimal_places=2)
    # Adding auto_now_add because it sets a date when it was created
    created_at = models.DateTimeField(auto_now_add=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")
    # Adding auto_now to this because it sets the date to the current time every time it's updated
    last_modified = models.DateTimeField(auto_now=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")
    description = models.TextField(help_text="The description of the attraction")
    # Not sure how to do this
    attractiontype = models.ForeignKey('AttractionType')
    city = models.CharField(max_length=CITY_LENGTH)
    address = models.CharField(max_length=ADDRESS_LENGTH)
    zipcode = models.CharField(max_length=ZIP_LENGTH)
    state = models.CharField(max_length=STATE_LENGTH)
    upvote = models.IntegerField(blank=True, default=0)
    downvote = models.IntegerField(blank=True, default=0)
    
    #TODO Implement the taggit thing
#    tags = TaggableManager()
    
    # The meta options We order by name. Get Latest by is when using 
    class Meta:
        get_latest_by = "created_at"
        ordering = ['name']
        verbose_name = "Attraction"
        verbose_name_plural = "Attractions"
    
#This class is the Attraction Types. This will be things like "Bar", or "Live Musics", etc
class AttractionType(models.Model):
    # TODO Define the choices
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = "Attraction Type"
        ordering = ['name']

# Our custom fields for the User class
class UserProfile(models.Model):
    #Required. Maps this to the user
    user = models.OneToOneField(User)
    
    #Our custom fields
    city = models.CharField(max_length=CITY_LENGTH)
    address = models.CharField(max_length=ADDRESS_LENGTH)
    zipcode = models.CharField(max_length=ZIP_LENGTH)
    state = models.CharField(max_length=STATE_LENGTH)
    #Using an integer field for gender. 0 = male, 1 = female
    gender = models.IntegerField()
    reputation = models.IntegerField()
    #TODO  Interests...
    
class Photo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")
    last_modified = models.DateTimeField(auto_now=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")
    # Needed? 
    url = models.CharField(max_length=100)
    user = models.ForeignKey(UserProfile, blank=True)
    attraction = models.ForeignKey(Attraction, blank=True)
    
class Path(models.Model):
    user = models.ForeignKey(UserProfile)
    
class Comment(models.Model):
    user = models.ForeignKey(UserProfile, help_text="The user that made the comment")
    # The type can either be 0 = Traveler comment. Local Comment = 1
    type_id = models.IntegerField(default=0)
    comment = models.TextField()
    attraction = models.ForeignKey(Attraction, blank=True)
    upvote = models.IntegerField(blank=True, default=0)
    downvote = models.IntegerField(blank=True, default=0)
    # Adding auto_now_add because it sets a date when it was created
    created_at = models.DateTimeField(auto_now_add=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")
    # Adding auto_now to this because it sets the date to the current time every time it's updated
    last_modified = models.DateTimeField(auto_now=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")
    
# This links the Attractions and the Paths. 
class PathAttraction(models.Model):
    attraction_id = models.IntegerField()
    path_id = models.IntegerField()
    
    # This needs the attraction_id and the path_id to be unique. 
    class Meta:
        unique_together = ('attraction_id', 'path_id')
    
    
    
