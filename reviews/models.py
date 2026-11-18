from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    author_name = models.CharField('Ваше Имя', max_length=150)
    rating = models.PositiveSmallIntegerField(
        'Оценка',
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    device_id = models.CharField('ID устройства', max_length=64, unique=True)
    text = models.TextField('Текст отзыва')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.author_name} ({self.rating}/5)'
