from django.db import models
from django.utils.text import slugify
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    email = models.EmailField(default='nama@web.com')
    alamat = models.CharField(max_length=100)
    waktu_posting = models.DateTimeField(auto_now_add=True)
    kategori = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()
        pass

    def __str__(self):
        return "{}. {}".format(self.id, self.title)
        pass
    pass
