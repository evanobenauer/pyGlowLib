class Event:

    eventActions: list['EventAction']
    args: list

    def __init__(self):
        self.eventActions = []
        self.args = []


    def post(self, args: list):
        self.args = args

        try:
            for action in self.eventActions:
                action.action()
        except:
            pass


    def subscribeAction(self, action: 'EventAction'):
        self.eventActions.append(action)

    def unsubscribeAction(self, action: 'EventAction'):
        self.eventActions.remove(action)


class EventAction:

    event: Event
    subscribed: bool
    action = None

    def __init__(self, event: Event, action):
        self.event = event
        self.action = action
        self.subscribed = False


    def subscribe(self):
        self.event.subscribeAction(self)


    def unsubscribe(self):
        self.event.unsubscribeAction(self)
