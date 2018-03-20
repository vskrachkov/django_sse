from django.http import StreamingHttpResponse
from django.shortcuts import render

from .utils import get_event


def index(request):
    return render(request, template_name='sse/index.html')

def events(request):
    last_event_id = request.META.get('HTTP_LAST_EVENT_ID')

    return StreamingHttpResponse(streaming_content=get_event(last_event_id),
                                 content_type='text/event-stream')
