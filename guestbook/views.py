from django.shortcuts import render, redirect
from .models import Guestbook
from django.utils import timezone
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def guestbook_main(request):
    if request.method == 'GET':
        guestbooks = Guestbook.objects.all().order_by('-created')
        guestbooks = []
        for guestbook in Guestbook.objects.all().order_by('-created'):
            guestbooks.append({
                'title': guestbook.title,
                'name': guestbook.name,
                'content': guestbook.content,
                'created': guestbook.created,
            })
        return JsonResponse({
                
                'status': 200,
                'message': 'Guestbook entries retrieved successfully',
                'data': guestbooks
        })
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        title = body.get('title')
        name = body.get('name')
        content = body.get('content')
        password = body.get('password')

        guestbook = Guestbook(
            title=title,
            name=name,
            content=content,
            created=timezone.now(),
            password=password
        )
        guestbook.save()

        return JsonResponse({
            'status': 200,
            'message': 'Guestbook entry created successfully',
            'data': {
               'title': guestbook.title,
               'name': guestbook.name,
               'content': guestbook.content,
               'created': guestbook.created
            }
        })

    
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        guestbook_id = body.get('id')
        password = body.get('password')

        try:
            guestbook = Guestbook.objects.get(id=guestbook_id, password=password)
            guestbook.delete()
            return JsonResponse({
                'status': 200,
                'message': 'deleted successfully'
,               'data' : None
            })
        except Guestbook.DoesNotExist:
            return JsonResponse({
                'status': 404,
                'error': 'incorrect password'
            })
    else:
        return JsonResponse({
            'status': 405,
            'error': 'Invalid request method'
        })        
        