from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, db_column='move_title')
    file = models.BinaryField(editable=True)

    class Meta:
        db_table = "movies"

    def __str__(self):
        return '%s' % (self.title)

