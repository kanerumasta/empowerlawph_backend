from rest_framework.serializers import ModelSerializer, CharField
from .models import Case

    # id = models.CharField(primary_key=True, max_length=50, editable=False)
    # title = models.CharField(max_length=255)
    # number = models.CharField(max_length = 255)
    # decision_date = models.DateField()
    
    # # legal_area = models.CharField(max_length = 255)
    # full_text = models.TextField()
    # # citations = models.ManyToManyField
    # ponente = models.CharField(max_length = 255)
    # division = models.CharField(max_length = 255)
class CaseSerializer(ModelSerializer):
    headline = CharField( read_only = True)
    class Meta:
        model = Case
        fields = ['id','title','number','decision_date','full_text','ponente','division','headline']
