from django.shortcuts import render, get_object_or_404, redirect
from .models import Story, Scene, Answer, PsychotypeCharacteristic
from psychological_models.models import BasisOfPsychotype
from .forms import StoryForm, SceneForm, AnswerForm, PsychotypeCharacteristicForm
from django.contrib import auth

# Create your views here.

MAX_SCENE_VALUE = 228


def story_dev(request):

    if not auth.get_user(request).is_authenticated():
        return redirect('/')
    args = dict()
    args['username'] = auth.get_user(request).username

    if request.method == 'POST':
        story_id = request.POST.get('delete', '')
        Answer.objects.filter(story=story_id).delete()
        Scene.objects.filter(story=story_id).delete()
        Story.objects.get(id=story_id).delete()
        print("id = " + story_id)

    args['panel_group'] = Story.objects.all()
    print('Run portal/story_dev script')
    return render(request, 'portal/story_dev/story_dev.html', args)


def editing_story(request, story_id=None):

    if not auth.get_user(request).is_authenticated():
        return redirect('/')

    args = dict()
    args['username'] = auth.get_user(request).username

    if request.method == 'POST':
        edited_form = StoryForm(request.POST or None)
        if edited_form.is_valid():
            print('---------------------------------------------------')
            print(edited_form.cleaned_data)
            bases = edited_form.cleaned_data['bases']
            del edited_form.cleaned_data['bases']
            print(edited_form.cleaned_data)
            print(bases)
            print('---------------------------------------------------')

            Story.objects.filter(id=story_id).update(**(edited_form.cleaned_data))
            print(len(bases))
            Story.objects.get(id=story_id).bases.clear()
            for basis in bases:
                Story.objects.get(id=story_id).bases.add(basis)

        scene_id = request.POST.get('delete', '')
        if scene_id != '':
            Answer.objects.filter(scene=scene_id).delete()
            Scene.objects.filter(id=scene_id).delete()

    item = get_object_or_404(Story, id=story_id)

    args['edited_form'] = StoryForm(instance=item)
    args['panel_group'] = Scene.objects.filter(story=story_id).order_by('scene_order')
    return render(request, 'portal/story_dev/editing_story.html', args)


def new_story(request):

    if not auth.get_user(request).is_authenticated():
        return redirect('/')
    print('Run portal/new_story script')
    args = dict()
    args['username'] = auth.get_user(request).username

    instance = Story.objects.create()

    return redirect('/portal/story_dev/{}/'.format(instance.id), args)


def editing_scene(request, story_id=None, scene_id=None):

    if not auth.get_user(request).is_authenticated():
        return redirect('/')

    args = dict()
    args['username'] = auth.get_user(request).username

    if request.method == 'POST':
        edited_form = SceneForm(request.POST or None)
        if edited_form.is_valid():
            print(edited_form.cleaned_data)
            Scene.objects.filter(id=scene_id).update(**(edited_form.cleaned_data))

        answer_id = request.POST.get('delete', '')
        if answer_id != '':
            Answer.objects.filter(id=answer_id).delete()

    item = get_object_or_404(Scene, id=scene_id)

    args['edited_form'] = SceneForm(instance=item)
    args['panel_group'] = Answer.objects.filter(scene=scene_id)
    return render(request, 'portal/story_dev/editing_scene.html', args)


def new_scene(request, story_id=None):

    if not auth.get_user(request).is_authenticated():
        return redirect('/')
    print('Run new_scene script')
    args = dict()
    args['username'] = auth.get_user(request).username

    instance = Scene.objects.create(story_id=story_id)

    return redirect('/portal/story_dev/{}/{}/'.format(story_id, instance.id), args)


def editing_answer(request, story_id=None, scene_id=None, answer_id=None):

    if not auth.get_user(request).is_authenticated():
        return redirect('/')

    args = dict()
    args['username'] = auth.get_user(request).username

    if request.method == 'POST':
        edited_form = AnswerForm(request.POST or None)
        if edited_form.is_valid():
            print(edited_form.cleaned_data)
            Answer.objects.filter(id=answer_id).update(**(edited_form.cleaned_data))

    item = get_object_or_404(Answer, id=answer_id)
    bases = BasisOfPsychotype.objects.all()

    for basis in bases:
        exist_flag = PsychotypeCharacteristic.objects.filter(answer=answer_id).filter(basis=basis.id).exists()
        if not exist_flag:
            PsychotypeCharacteristic.objects.create(answer=Answer.objects.get(id=answer_id), basis=basis)

    args['edited_form'] = AnswerForm(instance=item)
    basis_set = Story.objects.get(id=story_id).bases.all()
    args['set_characteristic_group'] = list()
    args['unset_characteristic_group'] = list()
    for basis in bases:
        if basis not in basis_set:
            args['unset_characteristic_group'].append(PsychotypeCharacteristic.objects.filter(answer=answer_id).get(basis=basis.id))
        else:
            args['set_characteristic_group'].append(PsychotypeCharacteristic.objects.filter(answer=answer_id).get(basis=basis.id))

    return render(request, 'portal/story_dev/editing_answer.html', args)


def new_answer(request, story_id=None, scene_id=None):

    if not auth.get_user(request).is_authenticated():
        return redirect('/')
    print('Run new_answer script')
    args = dict()
    args['username'] = auth.get_user(request).username

    instance = Answer.objects.create(story=Story.objects.get(id=story_id), scene=Scene.objects.get(id=scene_id))

    return redirect('/portal/story_dev/{}/{}/{}/'.format(story_id, scene_id, instance.id), args)


def editing_psy_char(request, story_id=None, scene_id=None, answer_id=None, psy_char_id=None):

    if not auth.get_user(request).is_authenticated():
        return redirect('/')

    args = dict()
    args['username'] = auth.get_user(request).username

    if request.method == 'POST':
        edited_form = PsychotypeCharacteristicForm(request.POST or None)
        if edited_form.is_valid():
            print(edited_form.cleaned_data)
            PsychotypeCharacteristic.objects.filter(id=psy_char_id).update(**(edited_form.cleaned_data))

    item = get_object_or_404(PsychotypeCharacteristic, id=psy_char_id)
    args['edited_form'] = PsychotypeCharacteristicForm(instance=item)
    args['basis'] = BasisOfPsychotype.objects.get(id=item.basis.id)

    return render(request, 'portal/story_dev/editing_psy_char.html', args)

