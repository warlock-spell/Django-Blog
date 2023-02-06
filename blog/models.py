from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=300)
    date = models.DateField()
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.title
