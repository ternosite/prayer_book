from django.db import models


class Prayer(models. Model):
    name = models.CharField(max_length=200, verbose_name="Назва молитви")
    text = models.TextField(verbose_name="Текст молитви",
                            error_messages={'blank': 'Це поле обов"язкове для заповнення.'}
                            )
    
    class Meta:
        verbose_name = "Молитва"
        verbose_name_plural = "Молитви"


    def __str__(self):
        return self.name