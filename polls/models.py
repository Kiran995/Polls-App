from django.db import models

# Create your models here.

class Poll(models.Model):
    poll_name = models.CharField(max_length=10)

    def __str__(self):
        return '%s-%s' %(
            'Poll',
            self.poll_name
        )


class Question(models.Model):
    question = models.CharField(max_length=100)
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '%s-%s-%s' %(
            'Question',
            self.question,
            self.poll
        )

class Option(models.Model):
    description = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '%s-%s-%s-%s' %(
            'Option',
            self.description,
            self.count,
            self.question
        )

