from django.db import models

class DataFrame(models.Model):
    csv_file = models.FileField(upload_to='csvs/')
    filename = models.CharField(max_length=255)
    num_rows = models.IntegerField()
    num_columns = models.IntegerField()

