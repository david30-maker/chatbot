from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data['message']
        response = {
            'message': message
        }
        return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        return HttpResponse('Invalid request')