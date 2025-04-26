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
        data = [
            {
                'title': guestbook.title,
                'name': guestbook.name,
                'content': guestbook.content,
                'created': guestbook.created,
            }
            for guestbook in guestbooks
        ]
        return JsonResponse({'guestbooks': data}, status=200)
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

        return JsonResponse({'message': 'Guestbook entry created successfully'}, status=201)
    elif request.method == 'DELETE':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        password = body.get('password')

        try:
            guestbook = Guestbook.objects.get(password=password)
            guestbook.delete()
            return JsonResponse({'message': 'deleted successfully'}, status=200)
        except Guestbook.DoesNotExist:
            return JsonResponse({'error': 'incorrect password'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)        
        