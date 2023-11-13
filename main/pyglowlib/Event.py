# Events are classes that can have multiple actions subscribed to them at a time. Events will execute all actions
# from their list wherever the post method is invoked
class Event:

    def __init__(self):
        self.eventActions: list['EventAction'] = []
        self.args: tuple = ()

    def post(self, *args):
        self.args = args

        try:
            for action in self.eventActions:
                action.action()
        except BaseException:
            pass

    def subscribeAction(self, action: 'EventAction'):
        if not self.eventActions.__contains__(action):
            self.eventActions.append(action)

    def unsubscribeAction(self, action: 'EventAction'):
        self.eventActions.remove(action)


# Event actions are classes that can be subscribed to an event and activated when posted
class EventAction:

    def __init__(self, event: Event, action):
        self.event: Event = event
        self.action = action  # Lambda Statement
        self.subscribed: bool = False

    def subscribe(self):
        self.event.subscribeAction(self)

    def unsubscribe(self):
        self.event.unsubscribeAction(self)
