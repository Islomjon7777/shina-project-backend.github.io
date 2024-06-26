from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Basket

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_basket(sender, instance, created, **kwargs):
    if created:
        Basket.objects.create(user=instance)
