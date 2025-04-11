from django.db import models
from .helpers import generate_unique_case_id


class PracticeArea(models.Model):
     name = models.CharField(max_length=100)


class Case(models.Model):
    id = models.CharField(primary_key=True, max_length=50, editable=False)
    title = models.CharField(max_length=255)
    number = models.CharField(max_length = 255)
    decision_date = models.DateField()
    full_text = models.TextField()
    ponente = models.CharField(max_length = 255)
    division = models.CharField(max_length = 255)
    practice_area = models.ManyToManyField(PracticeArea, blank=True)
    preceding_case = models.OneToOneField(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
            if not self.id:
                # Passing a function that checks for existing IDs
                self.id = generate_unique_case_id(
                    self.decision_date,
                    self.number,
                    case_exists_func=lambda case_id: Case.objects.filter(id=case_id).exists()
                )
            super().save(*args, **kwargs)


class Citation(models.Model):

     TREATMENT_CHOICES = [
          ('cited', 'CITED'),
          ('discussed','DISCUSSED'),
          ('criticized','CRITICIZED'),
          ('overruled by law', 'OVERRULED BY LAW'),
          ('overruled','OVERRULED')
     ]
     case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='citations')
     selected_text = models.TextField()
     external_link =  models.CharField(max_length=255, null=True, blank=True)
     jurisdiction = models.CharField(max_length=255, null=True, blank=True)
     pattern = models.CharField(max_length=255, blank=True, null=True)
     treatment = models.CharField(max_length=50, choices=TREATMENT_CHOICES)
