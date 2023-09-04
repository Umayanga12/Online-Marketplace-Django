from django.db import models
from django.contrib.auth.models import User
from item.models import items

class conversation(models.Model):
    item = models.ForeignKey(items, related_name='conversation', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversation')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(conversation, related_name='message', on_delete=models.CASCADE)
    contact = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_message', on_delete=models.CASCADE)