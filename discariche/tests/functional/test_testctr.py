from discariche.tests import *

class TestTestctrController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='testctr', action='index'))
        # Test response...
