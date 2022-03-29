# from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Question(models.Model):
  noun = models.CharField(max_length=50)
  case = models.CharField(max_length=15)
  number = models.CharField(max_length=10)
  gender = models.CharField(max_length=6)

class CustomUser(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  correct = models.IntegerField(default=0)
  incorrect = models.IntegerField(default=0)
  points = models.IntegerField(default=0)
  
  first_bon_incor = models.IntegerField(default=0)
  second_bon_incor = models.IntegerField(default=0)
  third_bon_incor = models.IntegerField(default=0)
  fourth_bon_incor = models.IntegerField(default=0)
  fifth_bon_incor = models.IntegerField(default=0)
  first_tris_incor = models.IntegerField(default=0)
  second_tris_incor = models.IntegerField(default=0)
  third_tris_incor = models.IntegerField(default=0)
  fourth_tris_incor = models.IntegerField(default=0)
  fifth_tris_incor = models.IntegerField(default=0)

  previous_question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
  
  def average(self):
    correct = self.correct
    incorrect = self.incorrect
    if correct != 0 or incorrect != 0:
      avg = (correct/(correct+incorrect)) * 100
    else:
      avg = 0
    return round(avg, 1)

  # def total(self):
  #   return self.correct + self.incorrect
  class Meta:
    permissions = [("check_students", "Can view student stats")]

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
