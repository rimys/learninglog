from django.db import models

# Create your models here.



class Topic(models.Model):
    '''Тема которую изучаем'''
    text = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    #возвращает строковое представление модели
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(default='Enter text')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) < 50:
            hint = f'{self.text}'
        else:
            hint = f'{self.text[:50]}...'
        return hint