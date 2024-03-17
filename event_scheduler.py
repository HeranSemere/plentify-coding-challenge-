import json
from datetime import datetime

# Define a class for an event
class Event:
    def __init__(self, title, date, description=None):
        self.title = title  # The title of the event
        # Convert the date string to a datetime object and format it as 'YYYY-MM-DD'
        self.date = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')
        self.description = description  # The description of the event

# Define a class for an event scheduler
class EventScheduler:
    def __init__(self, filename='events.json'):
        self.filename = filename  # The filename where events are stored
        try:
            # Try to open the file and load the events
            with open(self.filename, 'r') as f:
                self.events = json.load(f)
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty list of events
            self.events = []

    # Method to add an event
    def add_event(self, title, date, description=None):
        event = Event(title, date, description)  # Create a new event
        self.events.append(event.__dict__)  # Add the event to the list
        # Sort the events by date
        self.events.sort(key=lambda x: x['date'])
        self.save_events()  # Save the events to the file
        print("Event saved")

    # Method to remove an event
    def remove_event(self, title):
        # Store the original number of events
        original_length = len(self.events)
        # Remove the event from the list if the title matches
        self.events = [event for event in self.events if event['title'] != title]
        # Check if an event was removed by comparing the lengths
        if len(self.events) < original_length:
            print(f"Event '{title}' was successfully removed.")
        else:
            print(f"Event '{title}' does not exist.")
        self.save_events()  # Save the events to the file


    # Method to list all events
    def list_events(self):
        for event in self.events:
            # Print the title, date, and description of each event
            print(f"Title: {event['title']}, Date: {event['date']}, Description: {event.get('description', '')}")
        if(len(self.events) == 0):
            print("No events scheduled")  # Print a message if there are no events

    # Method to save events to the file
    def save_events(self):
        with open(self.filename, 'w') as f:
            json.dump(self.events, f)  # Dump the events to the file in JSON format
