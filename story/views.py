from django.shortcuts import render
from development_of_story.models import Story, Scene, Answer
from django.contrib import auth

# Create your views here.

MAX_SCENE_VALUE = 228


def story(request):

    args = dict()
    args['username'] = auth.get_user(request).username
    args['panel_group'] = Story.objects.all()
    print('Run story script!')
    return render(request, 'story/story.html', args)


def scene(request, story_id=None, scene_order=None):

    args = dict()
    args['username'] = auth.get_user(request).username

    if (story_id is None) or (scene_order is None) or (not Scene.objects.filter(story=story_id).exists()):
        args['panel_group'] = Story.objects.all()
        return render(request, 'story/story.html', args)

    if int(scene_order) == MAX_SCENE_VALUE:
        return render(request, 'story/end.html', args)

    (scene_data, next_scene_order) = get_scene_data(story_id, int(scene_order))

    args['story_id'] = story_id
    args['scene_data'] = scene_data
    args['next_scene_order'] = next_scene_order
    args['panel_group'] = Answer.objects.filter(scene=scene_data.id)
    return render(request, 'story/scene.html', args)


def get_scene_data(story_id=None, scene_order=None):

    scenes = Scene.objects.filter(story=story_id).order_by('scene_order')
    exist_flag = scenes.filter(scene_order=scene_order).exists()
    end_flag = scenes.reverse()[0].scene_order == scene_order
    first_scene_order = scenes[0].scene_order

    if not exist_flag:
        scene_order = first_scene_order
    next_scene_order = scene_order

    if end_flag:
        next_scene_order = MAX_SCENE_VALUE
    else:
        for pre_item, next_item in zip(scenes[:len(scenes)-1], scenes[1:]):
            if pre_item.scene_order == scene_order:
                next_scene_order = next_item.scene_order
                break

    scene_data = scenes.filter(scene_order=scene_order)[0]
    return scene_data, next_scene_order
