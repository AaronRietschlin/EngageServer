import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'engage_server.settings'
from server.models import Attraction

a = Attraction()
a.name = "ajs hfadksfl "
a.description = "My house bitchets"
a.city = "Columbus"
a.state="OH"
a.zipcode = "43202"
a.address = "1212 Norwich"
upvote = 13
downvote = 1
a.save()