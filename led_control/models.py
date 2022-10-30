from django.db import models

class LED_STATUS(models.Model):
    status=models.CharField(max_length=3)

    def __str__(self):
        return f"{self.status}"


