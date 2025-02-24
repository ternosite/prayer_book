from django.db import models
from django.urls import reverse


class Prayer(models. Model):
    name = models.CharField(max_length=200, verbose_name="Назва молитви")
    text = models.TextField(verbose_name="Текст молитви",
                            error_messages={'blank': 'Це поле обов"язкове для заповнення.'}
                            )
    

    def get_absolute_url(self):
        return reverse('texty:prayer_detail', args=[self.pk])
    
    class Meta:
        verbose_name = "Молитва"
        verbose_name_plural = "Молитви"


    def __str__(self):
        return self.name