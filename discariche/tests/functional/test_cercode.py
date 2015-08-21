from discariche.tests import *

class TestCercodeController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='cercode', action='index'))
        # Test response...
