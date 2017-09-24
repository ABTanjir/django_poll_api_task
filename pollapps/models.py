from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length = 250)
    author = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.question + ' - ' + self.author
    

class  choice(models.Model):
    choice = models.ForeignKey(Poll, on_delete = models.CASCADE)
    answer = models.CharField(max_length = 250)
    votes = models.IntegerField()
    
    def __str__(self):
        return self.answer