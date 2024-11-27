from django.shortcuts import render, redirect, get_object_or_404

from .models import Digimon
from .forms import DigimonForm

def digimon_list(request):
  digimons = Digimon.objects.all()
  return render(request, 'Digimon/digimon_list.html', {'digimon_list' : digimons})

def digimon_detail(request, pk):
  digimon = get_object_or_404(Digimon, pk=pk)
  return render(request, 'Digimon/digimon_detail.html', {'digimon': digimon})

def digimon_new(request):
  if request.method == "POST":
    digimon = Digimon()
    form = DigimonForm(request.POST, instance=digimon)
    if form.is_valid():
      digimon = form.save()
      #digimon.save()
      #form.save_m2m()
      return redirect('digimon_detail', pk=digimon.pk)
  else:
    form = DigimonForm()
  return render(request, 'Digimon/digimon_edit.html', {'form': form})

def digimon_edit(request, pk):
  digimon = get_object_or_404(Digimon, pk=pk)
  if request.method == "POST":
    form = DigimonForm(request.POST, instance=digimon)
    if form.is_valid():
      digimon = form.save(commit=False)
      digimon.save()
      form.save_m2m()
      return redirect('digimon_detail', pk=digimon.pk)
  else:
    form = DigimonForm(instance=digimon)
  return render(request, 'Digimon/digimon_edit.html', {'form': form})

def digimon_delete(request, pk):
  digimon = get_object_or_404(Digimon, pk=pk)
  if request.method=='POST':
    digimon.delete()
    return redirect('digimon_list')
  return render(request, 'Digimon/digimon_detail.html', {'digimon': digimon})