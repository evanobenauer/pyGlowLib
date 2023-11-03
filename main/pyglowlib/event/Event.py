# Events are classes that can have multiple actions subscribed to them at a time. Events will execute all actions
# from their list wherever the post method is invoked
class Event:
    eventActions: list['EventAction']
    args: tuple

    def __init__(self):
        self.eventActions = []
        self.args = ()

    def post(self, *args):
        self.args = args

        try:
            for action in self.eventActions:
                action.action()
        except BaseException:
            pass

    def subscribeAction(self, action: 'EventAction'):
        self.eventActions.append(action)

    def unsubscribeAction(self, action: 'EventAction'):
        self.eventActions.remove(action)


# Event actions are classes that can be subscribed to an event and activated when posted
class EventAction:
    event: Event
    subscribed: bool
    action = None #Lambda Statement

    def __init__(self, event: Event, action):
        self.event = event
        self.action = action
        self.subscribed = False

    def subscribe(self):
        self.event.subscribeAction(self)

    def unsubscribe(self):
        self.event.unsubscribeAction(self)
