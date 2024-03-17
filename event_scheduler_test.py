import unittest
from event_scheduler import EventScheduler
import os

# remove old json file to start a new test
if os.path.exists("test_events.json"):
  os.remove("test_events.json")

class TestEventScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = EventScheduler(filename='test_events.json')

    def test_event_scheduler(self):
        # Test adding an event
        self.scheduler.add_event('Test Event', '2024-03-17', 'This is a test event.')
        self.assertEqual(len(self.scheduler.events), 1)
        self.assertEqual(self.scheduler.events[0]['title'], 'Test Event')
        self.assertEqual(self.scheduler.events[0]['date'], '2024-03-17')
        self.assertEqual(self.scheduler.events[0]['description'], 'This is a test event.')

        # Test removing an event
        self.scheduler.remove_event('Test Event')
        self.assertEqual(len(self.scheduler.events), 0)

        # Test listing events
        self.scheduler.add_event('Test Event 1', '2024-03-17', 'This is a test event.')
        self.scheduler.add_event('Test Event 2', '2024-03-18', 'This is another test event.')
        self.scheduler.events.sort(key=lambda x: x['date'])
        self.assertEqual(self.scheduler.events[0]['title'], 'Test Event 1')
        self.assertEqual(self.scheduler.events[1]['title'], 'Test Event 2')

if __name__ == '__main__':
    unittest.main()
