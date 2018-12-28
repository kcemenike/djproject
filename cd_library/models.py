from django.db import models

# Create your models here.

GENRE_CHOICES = (
    ('R', 'Rock'),
    ('B', 'Blues'),
    ('J', 'Jazz'),
    ('P', 'Pop'),
    )

class CD(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True) # make description field optional
    artist = models.CharField(max_length=40)
    date = models.DateField()
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    # CharField requires max_length argument to be set
    # If you want to store the time too, use DateTimeField instead


    def __unicode__(self):
        # this property defines its string representation
        return "%s by %s, %s" %(self.title, self.artist, self.date)
