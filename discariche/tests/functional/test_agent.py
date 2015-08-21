from discariche.tests import *

class TestAgentController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='agent', action='index'))
        # Test response...
