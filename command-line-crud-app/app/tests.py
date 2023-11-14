from django.test import TestCase
from .models import Anime

# Create your tests here.
class TestAnime(TestCase):
    def test_anime_creation(self):
        Anime.objects.create(name="Attack On Titan")
        self.assertEqual(len(Anime.objects.all()), 1)

    def test_all_anime(self):
        anime = Anime(name="Attack On Titan")
        anime.save()
        animes = Anime.objects.all()
        name = (Anime.name for anime in animes)
        self.assertEqual(len(animes), 1)

    def test_delete_anime(self):
        Anime.objects.create(name="Attack On Titan")
        Anime.objects.get(name="Attack On Titan").delete()
        animes = Anime.objects.all()
        self.assertEqual(len(animes), 0)


    def test_update_anime(self):
        anime = Anime.objects.create(name="Attack On Titan")
        self.assertEqual(anime.name, "Attack On Titan")
        anime.name = "AOT"
        self.assertEqual(Anime.objects.get(name="AOT").name, "AOT")

    def test_find_anime_by_name(self):
        anime = Anime.objects.create(name="Attack On Titan")
        anime.save() 
        anime_return = Anime.objects.get(name="Attack On Titan")
        self.assertEqual(anime_return.name, "Attack On Titan")

    def test_filtered_search(self):
        anime = Anime.objects.create(name="Attack On Titan")
        anime.save()
        anime_return = Anime.objects.filter(name="Attack On Titan")
        self.assertEqual(anime_return[0].name, "Attack On Titan")