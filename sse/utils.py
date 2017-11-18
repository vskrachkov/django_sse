def create_event(eventname, evntid, data):
    return 'event: {eventname}\n' \
           'id: {evntid}\n' \
           'data: {data}\n\n'.format(
        eventname=eventname, evntid=evntid, data=data)
