from django.db import models


class Movie(models.Model):
    name = models.fields.CharField(verbose_name='Movie Name', max_length=50)

    watch_count = models.fields.IntegerField(default=0)

    actors = models.ManyToManyField('actor.actor')

    thumbnail = models.ImageField(upload_to='movie')

    def __str__(self):
        return self.name
