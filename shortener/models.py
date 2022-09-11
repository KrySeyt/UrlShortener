from django.db import models


class Url(models.Model):
    full_url = models.URLField()
    short_url_key = models.CharField(max_length=16, primary_key=True)
