from discariche.tests import *

class TestDumptypeController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='dumptype', action='index'))
        # Test response...
