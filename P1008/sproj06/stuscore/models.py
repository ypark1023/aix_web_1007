from django.db import models

class Stu(models.Model):
    no = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    grade = models.IntegerField(default=0)
    stature = models.FloatField(default=0)
    kor = models.IntegerField(default=0)
    eng = models.IntegerField(default=0)
    math = models.IntegerField(default=0)
    sw = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.no},{self.name},{self.school},{self.grade},{self.stature},{self.kor},{self.eng},{self.math},{self.sw}'