from django.db import models
from case.models import Case
from accounts.models import User

class Highlight(models.Model):
    highlighted_text = models.TextField()
    start_offset = models.PositiveIntegerField()
    end_offset = models.PositiveIntegerField()
    note = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
