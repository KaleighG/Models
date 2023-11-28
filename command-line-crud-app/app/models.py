from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Anime(models.Model):
    name = models.CharField(max_length=30)

def __str__(self):
    return self.name

def create_anime(name):
    anime = Anime(name=name)
    anime.save()
    return anime

def all_animes():
    return Anime.objects.all()

def filter_anime(name):
    try: 
        return Anime.objects.filter(name=name)
    except ObjectDoesNotExist:
        return None
    
def find_anime_by_name(name):
    try: 
        return Anime.objects.get(name=name)
    except ObjectDoesNotExist:
        return None
    
def update_anime(name, newname):
    anime = find_anime_by_name(name)
    anime.name = newname
    anime.save()
    return anime

def delete_anime(name):
    anime = find_anime_by_name(name)
    anime.delete()