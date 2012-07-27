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
    latitude = models.DecimalField(default=0)
    longitude = models.DecimalField()
    # Adding auto_now_add because it sets a date when it was created
    created_at = models.DateTimeField(auto_now_add=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")
    # Adding auto_now to this because it sets the date to the current time every time it's updated
    last_modified = models.DateTimeField(auto_now=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")
    description = models.TextField(help_text="The description of the attraction")
    # '_id' is automatically appended -> photo_id will be the key
    photo = models.ForeignKey('Photo')
    # Not sure how to do this
    attractiontype = models.ForeignKey('AttractionType')
    attractiondetail = models.ForeignKey('AttractionDetail', help_text="The details of the attraction (including address, state, etc.")
#    tags = TaggableManager()
    
    # The meta options We order by name. Get Latest by is when using 
    class Meta:
        get_latest_by = "created_at"
        ordering = ['name']
        verbose_name = "Attraction"
        verbose_name_plural = "Attractions"
    
#This class is the Attraction Types. This will be things like "Bar", or "Live Musics", etc
class AttractionType(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = "Attraction Type"
        ordering = ['name']

# Our custom fields for the User class
class UserProfile(models.Model):
    #Required. Maps this to the user
    user = models.OneToOneField(User)
    
    #Our custom fields
    photo = models.ForeignKey('Photo')
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
    
class AttractionDetail(models.Model):
    traveler_comment = models.ForeignKey('Comment', help_text="The comment that will be shown as a Travelers Comment.")
    local_comment = models.ForeignKey('Comment', help_text="The comment that will be shown as a Local's comment.")
    city = models.CharField(max_length=CITY_LENGTH)
    address = models.CharField(max_length=ADDRESS_LENGTH)
    zipcode = models.CharField(max_length=ZIP_LENGTH)
    state = models.CharField(max_length=STATE_LENGTH)
    upvote = models.IntegerField(blank=True, default=0)
    downvote = models.IntegerField(blank=True, default=0)
    
class Path(models.Model):
    user = models.ForeignKey(UserProfile)
    
class Comment(models.Model):
    user = models.ForeignKey(UserProfile, help_text="The user that made the comment")
    # The type can either be 0 = Traveler comment. Local Comment = 1
    type_id = models.IntegerField(default=0)
    comment = models.TextField()
    upvote = models.IntegerField(blank=True, default=0)
    downvote = models.IntegerField(blank=True, default=0)
    # Adding auto_now_add because it sets a date when it was created
    created_at = models.DateTimeField(auto_now_add=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")
    # Adding auto_now to this because it sets the date to the current time every time it's updated
    last_modified = models.DateTimeField(auto_now=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST")
    
class PathAttraction(models.Model):
    attraction_id = models.IntegerField()
    path_id = models.IntegerField()
    
    # This needs the attraction_id and the path_id to be unique. 
    class Meta:
        unique_together = ('attraction_id', 'path_id')
    
    
    
