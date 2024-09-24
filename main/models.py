from django.db import models
from authentication.models import Customer_user

class Message(models.Model):
    original_text = models.TextField()
    edited_text = models.TextField(default = '', blank = True)
    send_date=models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(Customer_user, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return self.original_text
