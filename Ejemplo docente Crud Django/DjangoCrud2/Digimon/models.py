from django.db import models

# Create your models here.
# The Level class in Python defines a model with a name attribute of type CharField.
class Level(models.Model):
  name = models.CharField(max_length=25, null=False)

  def __str__(self):
    return self.name

# The `Attribute` class in Python defines a model with a `name` attribute of type `CharField`.
class Attribute(models.Model):
  name = models.CharField(max_length=25, null=False)

  def __str__(self):
    return self.name

# The `Group` class in Python defines a model with a name attribute of type CharField.
class Group(models.Model):
  name = models.CharField(max_length=25, null=False)

  def __str__(self):
    return self.name

# This Python class defines a Digimon model with attributes such as name, level, attribute, and a
# many-to-many relationship with a Group model.
class Digimon(models.Model):
  name = models.CharField(max_length=50, unique=True)
  level = models.ForeignKey(Level, on_delete=models.CASCADE, null=False)
  attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, null=False)
  group = models.ManyToManyField(to='Group', related_name='digimon_groups')

class Persona(models.Model):
  rut = models.BigIntegerField(primary_key=True)
  nombre = models.CharField(max_length=50)