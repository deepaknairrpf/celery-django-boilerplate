from django.db import models

# Create your models here.
class Documents(models.Model):
    title = models.CharField(max_length=150)
    document_url = models.ImageField(null=False,blank=False)
    # owner = models.ForeignKey()   ## foreign key to user id
    # organisation_id = models.ForeignKey()  ## foreign key to organisations
