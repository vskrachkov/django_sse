import time
import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render

from sse.utils import create_event


def index(request):
    return render(request, template_name='sse/index.html')

def events(request):
    print('last event id: ', request.META.get('HTTP_LAST_EVENT_ID'))
    data = {
        'some': 'data',
        'another': 'data',
        'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    str_data = json.dumps(data)
    _id = time.time()
    content = create_event('test', _id, str_data)
    return HttpResponse(content=content, content_type='text/event-stream')
