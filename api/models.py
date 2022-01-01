from typing_extensions import NotRequired
from django.db import models
import uuid

# Create your models here.
class Voterdb(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Voter_id= models.CharField(max_length=10)
    phone = models.CharField(max_length=13)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    voting_status = models.BooleanField(default=False)
    voter_address = models.CharField(max_length=45, blank=True)
    txn_hash = models.CharField(max_length=100, blank=True)


