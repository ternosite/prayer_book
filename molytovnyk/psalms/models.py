from django.db import models

class Psalm(models.Model):
    name = models.CharField(max_length=200, verbose_name='Назва псалму')
    text = models.TextField(verbose_name='Текст псалму', 
                            error_messages={'blank': 'Це поле обов"язкове для заповнення.'})


    class Meta:
        verbose_name = 'Псалом'
        verbose_name_plural = 'Псалми'


    def __str__(self):
        return self.name