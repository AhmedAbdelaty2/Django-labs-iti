from django.shortcuts import render, redirect, reverse
from .models import Actor
from .forms import ActorForm


def actors_list(request):
    actors = Actor.objects.all()
    return render(request, template_name='actor/actors_list.html', context={'actors': actors})


def actor_create(request):
    if request.method == 'GET':
        form = ActorForm()
        return render(request, template_name='actor/actor_create.html', context={'form': form})

    elif request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('actor:list'))


def actor_details(request, pk):
    actor = Actor.objects.get(pk=pk)
    return render(request, template_name='actor/actor_details.html', context={'actor_data': actor})


def actor_delete(request, pk):
    actor = Actor.objects.get(pk=pk)
    actor.delete()
    return redirect(reverse('actor:list'))


def actor_update(request, pk):
    actor = Actor.objects.get(pk=pk)
    if request.method == 'GET':
        form = ActorForm(instance=actor)
        return render(request, template_name='actor/actor_update.html', context={'form': form, 'actor': actor})

    elif request.method == 'POST':
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return redirect(reverse('actor:list'))
