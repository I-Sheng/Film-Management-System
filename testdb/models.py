from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, db_column='movie_title')
    file = models.BinaryField(editable=True)
    description = models.TextField(max_length=2000, default="A discription for the movie")

    class Meta:
        db_table = "movies"

    def __str__(self):
        return '%s' % (self.title)

