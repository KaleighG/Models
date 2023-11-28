from django.test import TestCase
from .models import Anime
from app import models
# Create your tests here.
class TestAnime(TestCase):
    def test_anime_creation(self):
        anime = models.create_anime("Attack On Titan")
        self.assertEqual(len(Anime.objects.all()), 1)

    def test_all_anime(self):
        anime = models.create_anime("Attack On Titan")
        anime.save()
        animes = models.all_animes()
        self.assertEqual(len(animes), 1)

    def test_delete_anime(self):
        anime = models.create_anime("Attack On Titan")
        anime.save()
        anime = models.delete_anime("Attack On Titan")
        animes = Anime.objects.all()
        self.assertEqual(len(animes), 0)


    def test_update_anime(self):
        anime = models.create_anime("Attack On Titan")
        anime.save()
        new_anime = models.update_anime(anime.name, "AOT")
        self.assertEqual(new_anime.name, "AOT")

    def test_find_anime_by_name(self):
        anime = Anime.objects.create(name="Attack On Titan")
        anime.save() 
        anime_return = models.find_anime_by_name("Attack On Titan")
        self.assertEqual(anime_return.name, "Attack On Titan")

    def test_filtered_search(self):
        anime = Anime.objects.create(name="Attack On Titan")
        anime.save()
        anime_return = models.filter_anime("Attack On Titan")
        self.assertEqual(anime_return[0].name, "Attack On Titan")