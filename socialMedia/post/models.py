from django.contrib.auth.models import User

from django.db import models

# class Post(models.Model):
#     content = models.TextField()
#     posted_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateField(auto_now=True)
#     created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    
#     class Meta:
#         ordering = ['-modified_at']

#     def __str__(self):
#         return self.created_by
    
    