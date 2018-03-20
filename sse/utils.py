import json
import time

import datetime
import uuid

test_pipe = [item for item in range(0, 10)]

def get_next_message():
    try:
        return test_pipe.pop()
    except IndexError:
        return


def create_event(event_name, event_id, data):
    return f'event: {event_name}\n' \
           f'id: {event_id}\n' \
           f'data: {data}\n\n'


def get_event(last_event_id=None):
    while 1:
        print(last_event_id)
        time.sleep(1)
        next_msg = get_next_message()
        if next_msg:
            data = {
                'message': next_msg,
                'time': datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            }
            yield create_event(
                event_name='test',
                event_id=uuid.uuid4(),
                data=json.dumps(data)
            )
