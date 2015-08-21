from discariche.tests import *

class TestComuniController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='comuni', action='index'))
        # Test response...
