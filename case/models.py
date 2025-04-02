from django.db import models
from .helpers import generate_unique_case_id


class Case(models.Model):
    id = models.CharField(primary_key=True, max_length=50, editable=False)
    title = models.CharField(max_length=255)
    number = models.CharField(max_length = 255)
    decision_date = models.DateField()
    
    # legal_area = models.CharField(max_length = 255)
    full_text = models.TextField()
    # citations = models.ManyToManyField
    ponente = models.CharField(max_length = 255)
    division = models.CharField(max_length = 255)

    def save(self, *args, **kwargs):
            if not self.id:
                # Pass a function that checks for existing IDs
                self.id = generate_unique_case_id(
                    self.decision_date, 
                    self.number, 
                    case_exists_func=lambda case_id: Case.objects.filter(id=case_id).exists()
                )
            super().save(*args, **kwargs)

