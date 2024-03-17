# Event Scheduler

This project consists of three main scripts:

1. `event_scheduler.py`: This script defines the Event and EventScheduler classes. The Event class represents an event with a title, date, and optional description. The EventScheduler class provides functionalities to create, list, and delete events from a JSON file.

2. start_program.py: This script is used to interact with the user. It prompts the user for input and uses the EventScheduler class to create, list, or delete events based on the user's input.

3. event_scheduler_test.py: This script is used to test the functionality of the EventScheduler class. It uses the unittest module to define a test case for the EventScheduler. The test case includes tests for adding an event, removing an event, and listing events. Before each test, it sets up a new EventScheduler instance. It also ensures that any existing events file is removed before starting a new test.

## How to Run

To run the program, run the start_program.py script from the command line like so:

`python start_program.py`

This will start the program and prompt you for input.

To run the tests, you run the event_scheduler_test.py script:

`python event_scheduler_test.py`

## Design Decisions and Assumptions

The business logic and the "User Interface" were separately developed so that the testing would be easier and to promote code reusability.
An object-oriented approach was chosen because it allows describing real-world objects and all their behaviors in code.

An assumption made while developing this program is a user can not add a past date as an event and that two events can have the same name but should have different internal indexes. 
