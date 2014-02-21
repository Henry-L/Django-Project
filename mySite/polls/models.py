import datetime
from django.utils import timezone
from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length = 200)
    publication_date = models.DateTimeField('Date Published')

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publication_date < now

    was_published_recently.admin_order_field = 'publication_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.choice_text
