from django import forms
from .models import Digimon,Group

# The `DigimonForm` class is a Django ModelForm for the `Digimon` model with fields for name, level,
# attribute, and a multiple choice field for selecting groups from the `Group` model.
class DigimonForm(forms.ModelForm):

  class Meta:
    model = Digimon
    fields = ('name', 'level', 'attribute', 'group')
    
  group = forms.ModelMultipleChoiceField(
    queryset=Group.objects.all(), 
    widget=forms.CheckboxSelectMultiple())
