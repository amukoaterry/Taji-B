from django.db import models

class ScanEvent(models.Model):
    scan_id= models.PositiveSmallIntegerField()
    drug_name = models.CharField(max_length=40)
    batch_number= models.CharField(max_length=30)
    pharmacy_id= models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.scan_id} {self.drug_name}"