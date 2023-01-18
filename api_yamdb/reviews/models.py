from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Review(models.Model):
    text = models.TextField(),
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'),
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='reviews'),
    score = models.IntegerField('рейтинг', validators=[MinValueValidator(0), MaxValueValidator[10]])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.text

class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'),

    def __str__(self):
        return self.text