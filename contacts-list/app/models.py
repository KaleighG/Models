from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    is_favorite = models.BooleanField(default=False)

def __str__(self):
    return self.name, self.email, self.phone, self.is_favorite

def create_contact(name, email, phone, is_favorite):
    contact = Contact(name=name, email=email, phone=phone, is_favorite=is_favorite)
    contact.save()
    return contact

def all_contacts():
    return Contact.objects.all()

def find_contact_by_name(name):
    try:
        return Contact.objects.get(name=name)
    except ObjectDoesNotExist:
        return None

def favorite_contacts():
    return Contact.objects.filter(is_favorite=True)

def update_contact_email(name, email):
    contact = find_contact_by_name(name)
    contact.email = email
    contact.save()

def delete_contact(name):
    contact = find_contact_by_name(name)
    contact.delete()
    