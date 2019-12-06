from django.db import models

from django.utils.translation import gettext as _

class Sighting(models.Model):

    id = models.CharField(
        help_text=_('Squirrel ID'),
        max_length=255,
        primary_key=True,
    )
    
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
    )

    age = models.CharField(
        help_text=_('Squirel Age'),
        max_length=20,
        choices=AGE_CHOICES,
        blank = True,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
    )

    color = models.CharField(
        help_text=_('Squirrel Fur Color'),
        max_length=20,
        choices=COLOR_CHOICES,
        blank =True,

    )

    latitude = models.DecimalField(
        help_text=_('Latitude'),
        max_digits=19,
        decimal_places=15,
    )

    longitude = models.DecimalField(
        help_text=_('Longitude'),
        max_digits=19,
        decimal_places=15,
    )

    date = models.DateField(
        help_text=_('Sighting Date'),
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = (
        (GROUND_PLANE, 'Ground Plane'),
        (ABOVE_GROUND, 'Above Ground'),
    )

    location = models.CharField(
        help_text=_('Location'),
        max_length=20,
        choices=LOCATION_CHOICES,
        blank = True,
    )

    specific_location = models.CharField(
        help_text=_('Specific Location'),
        max_length=255,
        blank=True,
    )

    running = models.BooleanField(
        help_text=_('Running'),
        default=True,
    )

    chasing = models.BooleanField(
        help_text=_('Chasing'),
        default=True,
    )

    climbing = models.BooleanField(
        help_text=_('Climbing'),
        default=True,
    )

    eating = models.BooleanField(
        help_text=_('Eating'),
        default=True,
    )

    foraging = models.BooleanField(
        help_text=_('Foraging'),
        default=True,
    )

    other_activities = models.CharField(
        help_text=_('Other Activities'),
        max_length=255,
        blank=True,
    )

    kuks = models.BooleanField(
        help_text=_('Kuks'),
        default=True,
    )
   
    quaas = models.BooleanField(
        help_text=_('Quaas'),
        default=True,
    )

    moans = models.BooleanField(
        help_text=_('Moans'),
        default=True,
    )

    tail_flags = models.BooleanField(
        help_text=_('Tail flags'),
        default=True,
    )
   
    tail_twitches = models.BooleanField(
        help_text=_('Tail twitches'),
        default=True,
    )
   
    approaches = models.BooleanField(
        help_text=_('Approaches'),
        default=True,
    )

    indifferent = models.BooleanField(
        help_text=_('Indifferent'),
        default=True,
    )
   
    runs_from = models.BooleanField(
        help_text=_('Runs from'),
        default=True,
    )

    def __str__(self):
        return self.id

