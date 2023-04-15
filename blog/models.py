from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse


class Author(models.Model):
    author = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    discription = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name='Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('blog:author-pictures', kwargs={'author_slug': self.slug})

class Epoch(models.Model):
    epoch = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    discription = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name='Epoch'
        verbose_name_plural = 'Epoches'

    def __str__(self):
        return self.epoch

    def get_absolute_url(self):
        return reverse('blog:epoch-pictures', kwargs={'epoch_slug': self.slug})


class Picture(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=200, db_index=True)
    slug  = models.SlugField(max_length=200, db_index=True)
    author = models.ForeignKey(Author, related_name='%(class)s', on_delete=models.CASCADE)
    epoch = models.ForeignKey(Epoch, related_name='%(class)s', on_delete=models.CASCADE)
    # year = models.IntegerField()
    year = models.CharField(max_length=200, db_index=True, blank=True)
    country = models.CharField(max_length=200, db_index=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    height = models.IntegerField(blank=True)
    length = models.IntegerField(blank=True)
    created  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail-picture', args=[self.slug])


    