from discariche.tests import *

class TestCerController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='cer', action='index'))
        # Test response...
