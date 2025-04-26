from django.shortcuts import render, redirect
from .models import Guestbook
from django.utils import timezone
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# ��û�� POST�� ���� �����͸� �����ϰ�, GET�� ���� �����͸� ��ȸ�Ͽ� �����ִ� �� �Լ�
# guestbook_main �Լ��� GET ��û�� POST ��û�� ��� ó���մϴ�.
@csrf_exempt
def guestbook_main(request):
    if request.method == 'GET':
        # GET ��û�� ���� ��� GuestBook ��ü�� �����ͼ� ���ø��� �����մϴ�.
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
        # POST ��û�� ���� �� �����͸� �޾Ƽ� ���ο� GuestBook ��ü�� �����մϴ�.
        title = body.get('title')
        name = body.get('name')
        content = body.get('content')
        password = body.get('password')

        # ���ο� GuestBook ��ü�� �����ϰ� �����մϴ�.
        guestbook = Guestbook(
            title=title,
            name=name,
            content=content,
            created=timezone.now(),
            password=password
        )
        guestbook.save()

        return JsonResponse({'message': 'Guestbook entry created successfully'}, status=201)
    
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)        
        