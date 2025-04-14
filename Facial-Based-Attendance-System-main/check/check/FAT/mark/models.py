from django.db import models

# Create your models here.


class Attendance(models.Model):
    year = models.TextField(max_length=10)
    branch = models.TextField(max_length=10)
    section = models.CharField(max_length=10)
    date = models.DateField()
    period = models.IntegerField()
    R19R11A05B0 = models.TextField(default='absent')
    R19R11A05B1 = models.TextField(default='absent')
    R19R11A05B2 = models.TextField(default='absent')
    R19R11A05B3 = models.TextField(default='absent')
    R19R11A05B4 = models.TextField(default='absent')
    R19R11A05B5 = models.TextField(default='absent')
    R19R11A05B6 = models.TextField(default='absent')
    R19R11A05B7 = models.TextField(default='absent')
    R19R11A05B8 = models.TextField(default='absent')
    R19R11A05C9 = models.TextField(default='absent')
    R20R15A0513 = models.TextField(default='absent')
    R19R11A0516 = models.TextField(default='absent')
    R19R11A04C2 = models.TextField(default='absent')
    R160220735077 = models.TextField(default='absent')
    R160220735070 = models.TextField(default='absent')
    R160220735088 = models.TextField(default='absent')
    R160220735120 = models.TextField(default='absent')
    R160220735090 = models.TextField(default='absent')


# "teja":[9,"160220735077"],"charan":[10,"160220735070"],"nomitha":[11,"160220735088"],"vikram":[12,"160220735120"]}
