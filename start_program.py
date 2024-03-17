from event_scheduler import EventScheduler  # Import the custom EventScheduler class
from datetime import datetime
import re

# Function to get a valid date from the user
def get_date():
    while True:
        date = input("Enter the event date (YYYY-MM-DD): ")
        # Check if the date matches the required format
        if not re.match(r'\d{4}-\d{2}-\d{2}', date):
            print("Error: The date must be in the format YYYY-MM-DD.")
            continue
        try:
            # Try to convert the date string to a datetime object
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            # Check if the date is in the past
            if date_obj < datetime.now():
                print("Error: The date cannot be in the past.")
                continue
            return date
        except ValueError:
            print("Error: Invalid date.")

# Function to get a non-empty title from the user
def get_title():
    while True:
        title = input("Enter the event title: ")
        # Check if the title is empty
        if not title:
            print("Error: The title cannot be empty.")
            continue
        return title

# Function to start the event scheduler
def start():
    scheduler = EventScheduler()  # Create an instance of EventScheduler
    while True:
        # Print the menu options
        print("1: Add event")
        print("2: Remove event")
        print("3: List events")
        print("4: Exit")
        choice = input("Choose an option: ")

        # Perform the chosen action
        if choice == '1':
            title = get_title()
            date = get_date()
            description = input("Enter the event description (optional): ")
            scheduler.add_event(title, date, description)
        elif choice == '2':
            title = get_title()
            scheduler.remove_event(title)
        elif choice == '3':
            scheduler.list_events()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

# Start the event scheduler
start()
