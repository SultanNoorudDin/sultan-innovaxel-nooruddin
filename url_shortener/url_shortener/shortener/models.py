import string, random
from django.db import models
from django.utils.timezone import now

def generate_shortcode():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortURL(models.Model):
    url = models.URLField()
    shortCode = models.CharField(max_length=10, unique=True, default=generate_shortcode)
    createdAt = models.DateTimeField(default=now)
    updatedAt = models.DateTimeField(auto_now=True)
    accessCount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.shortCode
