from django.shortcuts import render, get_object_or_404, redirect
from .models import BasisOfPsychotype, BasisMetric
from development_of_story.models import PsychotypeCharacteristic
from .forms import BasisOfPsychotypeForm
from django.contrib import auth

# Create your views here.


def psy_dev(request):

    if not auth.get_user(request).is_authenticated():
        return redirect('/')
    args = dict()
    args['username'] = auth.get_user(request).username

    if request.method == 'POST':
        psy_bas_id = request.POST.get('delete', '')
        PsychotypeCharacteristic.objects.filter(basis=psy_bas_id).delete()
        BasisOfPsychotype.objects.get(id=psy_bas_id).delete()
        print("id = " + psy_bas_id)

    args['panel_group'] = BasisOfPsychotype.objects.all()
    print('Run portal/psy_dev script')
    return render(request, 'portal/psy_dev/psy_dev.html', args)


def editing_psy_bas(request, psy_bas_id=None):

    if not auth.get_user(request).is_authenticated():
        return redirect('/')

    args = dict()
    args['username'] = auth.get_user(request).username

    if request.method == 'POST':
        edited_form = BasisOfPsychotypeForm(request.POST or None)
        if edited_form.is_valid():
            BasisOfPsychotype.objects.filter(id=psy_bas_id).update(**(edited_form.cleaned_data))

    item = get_object_or_404(BasisOfPsychotype, id=psy_bas_id)

    args['edited_form'] = BasisOfPsychotypeForm(instance=item)
    return render(request, 'portal/psy_dev/editing_psy_dev.html', args)


def new_psy_bas(request):

    if not auth.get_user(request).is_authenticated():
        return redirect('/')
    print('Run portal/new_story script')
    args = dict()
    args['username'] = auth.get_user(request).username

    instance = BasisOfPsychotype.objects.create(metric=BasisMetric.objects.all()[0])

    return redirect('/portal/psy_dev/{}/'.format(instance.id), args)
