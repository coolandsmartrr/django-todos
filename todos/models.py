from django.db import models

# Create your models here.
class Todo(models.Model):
  task = models.CharField(max_length=50)
  is_done = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def __str__(self) -> str:
    return f"#{self.id}: {self.task}"