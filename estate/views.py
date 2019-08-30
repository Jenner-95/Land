from django.shortcuts import render, HttpResponse
from users.models import User
from estate.models import Estate, Plot, Tree
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib import messages

# Create your views here.


def estate_detail(request, user_id):
    context = {
        'estates': Estate.objects.all(),
        'user_id': user_id,
        'user': User.objects.get(id=user_id),
    }
    return render(request, 'estate/estate_detail.html', context)


def create_estate_form(request, user_id):
    if request.method == 'POST':
        new_estate = Estate(
            name=request.POST['name'],
            country=request.POST['country'],
            departament=request.POST['departament'],
            image=request.FILES['image']
        )
        new_estate.save()
        return HttpResponseRedirect(reverse('estate:estate_detail', kwargs={'user_id': user_id}))
    elif request.method == 'GET':
        template = 'estate/create_estate_form.html'
        context = {
            'user_id': user_id,
        }
        return render(request, template, context)
    return HttpResponse('Error: metodo no permitido.')


def edit_estate_form(request, estate_id, user_id):
    if request.method == 'POST':
        updated_estate = Estate.objects.get(pk=estate_id)
        updated_estate.name = request.POST['name']
        updated_estate.country = request.POST['country']
        updated_estate.departament = request.POST['departament']
        if len(request.FILES) > 0:
            updated_estate.image = request.FILES['image']
        updated_estate.save()

        return HttpResponseRedirect(reverse('estate:estate_detail', kwargs={'user_id': user_id}))
    elif request.method == 'GET':
        template = 'estate/edit_estate_form.html'
        context = {
            'estate_id': estate_id,
            'user_id': user_id,
            'estate': Estate.objects.get(id=estate_id),

        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def delete_estate(request, estate_id, user_id):
    deleted_estate = Estate.objects.get(pk=estate_id)
    deleted_estate.delete()

    return HttpResponseRedirect(reverse('estate:estate_detail', kwargs={'user_id': user_id}))


def plot_detail(request, estate_id, user_id):
    context = {
        'user_id': user_id,
        'estate_id': estate_id,
        'plots': Plot.objects.filter(estate=estate_id),
        'user': User.objects.get(id=user_id),
    }
    return render(request, 'estate/plot_detail.html', context)


def create_plot_form(request, estate_id, user_id):
    if request.method == 'POST':
        new_plot = Plot(
            estate=Estate.objects.get(pk=request.POST['estate']),
            name=request.POST['name'],
            latitude=request.POST['latitude'],
            longitude=request.POST['longitude'],
        )
        new_plot.save()

        return HttpResponseRedirect(reverse('estate:plot_detail', kwargs={'estate_id': request.POST['estate'], 'user_id': user_id}))
    elif request.method == 'GET':
        template = 'estate/create_plot_form.html'
        estate = Estate.objects.filter(id=estate_id).values('name')
        estates = Estate.objects.filter(name__in=estate)
        context = {
            'estate_id': estate_id,
            'estates': estates,
            'user_id': user_id,
        }

        return render(request, template, context)
    return HttpResponse('Error: metodo no permitido.')


def edit_plot_form(request, plot_id, user_id):
    if request.method == 'POST':
        updated_plot = Plot.objects.get(pk=plot_id)
        updated_plot.estate = Estate.objects.get(pk=request.POST['estate'])
        updated_plot.name = request.POST['name']
        updated_plot.latitude = request.POST['latitude']
        updated_plot.longitude = request.POST['longitude']
        updated_plot.save()

        return HttpResponseRedirect(reverse('estate:plot_detail', kwargs={'estate_id': request.POST['estate'], 'user_id': user_id}))
    elif request.method == 'GET':
        template = 'estate/edit_plot_form.html'
        context = {
            'plot_id': plot_id,
            'user_id': user_id,
            'estates': Estate.objects.all(),
            'plot': Plot.objects.get(id=plot_id),
        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def delete_plot(request, plot_id, estate_id, user_id):
    deleted_plot = Plot.objects.get(pk=plot_id)
    print(delete_plot)
    deleted_plot.delete()

    return HttpResponseRedirect(reverse('estate:plot_detail', kwargs={'estate_id': estate_id,  'user_id': user_id}))


def tree_detail(request, plot_id, user_id):
    context = {
        'user_id': user_id,
        'plot_id': plot_id,
        'trees': Tree.objects.filter(plot=plot_id),
        'user': User.objects.get(id=user_id),
    }
    return render(request, 'estate/tree_detail.html', context)


def create_tree_form(request, plot_id, user_id):
    if request.method == 'POST':
        new_tree = Tree(
            plot=Plot.objects.get(pk=request.POST['plot']),
            diameter=request.POST['diameter'],
            height=request.POST['height'],
            health=request.POST['health'],
            year=request.POST['year'],
        )
        new_tree.save()

        return HttpResponseRedirect(reverse('estate:tree_detail', kwargs={'plot_id': request.POST['plot'], 'user_id': user_id}))
    elif request.method == 'GET':
        template = 'estate/create_tree_form.html'
        plot = Plot.objects.filter(id=plot_id).values('name')
        plots = Plot.objects.filter(name__in=plot)
        context = {
            'plot_id': plot_id,
            'plots': plots,
            'user_id': user_id,
        }
        return render(request, template, context)
    return HttpResponse('Error: metodo no permitido.')


def edit_tree_form(request, tree_id, user_id):
    if request.method == 'POST':
        updated_tree = Tree.objects.get(pk=tree_id)
        updated_tree.plot = Plot.objects.get(pk=request.POST['plot'])
        updated_tree.diameter = request.POST['diameter']
        updated_tree.height = request.POST['height']
        updated_tree.health = request.POST['health']
        updated_tree.year = request.POST['year']
        updated_tree.save()
        return HttpResponseRedirect(reverse('estate:tree_detail', kwargs={'plot_id': request.POST['plot'], 'user_id': user_id}))
    elif request.method == 'GET':
        template = 'estate/edit_tree_form.html'
        context = {
            'tree_id': tree_id,
            'user_id': user_id,
            'plots': Plot.objects.all(),
            'tree': Tree.objects.get(id=tree_id),
        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def delete_tree(request, tree_id, plot_id, user_id):
    deleted_tree = Tree.objects.get(pk=tree_id)
    deleted_tree.delete()

    messages.info(request, 'Successfully deleted tree.')
    return HttpResponseRedirect(reverse('estate:tree_detail', kwargs={'plot_id': plot_id,  'user_id': user_id}))
