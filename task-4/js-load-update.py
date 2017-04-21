class SecurityCheck(object):

    def __init__(self, pause_duration, rampup_duration,
                 steady_duration):

        self._pause_duration = pause_duration
        self._rampup_duration = rampup_duration
        self._steady_duration = steady_duration

class BandwidthTest(object):

    def __init__(self, start_at, steady_at, duration):

        self._start_at = start_at
        self._steady_at = steady_at
        self._duration = duration

class LoadTest(object):

    def __init__(self, delay, duration):

        self._start_at = start_at
        self._steady_at = steady_at
        self._duration = duration

class TestImplementator(object):

    def show(self, widget):
        pass
    def onTrigerMove(self, widget):
        pass
    def save(self, widget):
        pass


class BandwidthTestCheckImplementator(
        TestImplementator, BandwidthTest):

    config_code = "badwidth"

    def get_pretty_coordinates(self):

        trigger1_coord = self._start_at / self._duration
        trigger2_coord = self._steady_at / self._duration

        return trigger1_coord, trigger2_coord

    def onTriggerMove(self, trigger1_coord, trigger2_coord):
        return trigger1_coord < trigger2_coord

    def update_coordinates(self, trigger1_coord, trigger2_coord):
        self._start_at = trigger1_coord * self._duration
        self._steady_at = trigger2_coord * self._duration

class SecurityCheckImplementator(TestImplementator, SecurityCheck):

    config_code = "security"

    def get_pretty_coordinates(self):

        duration = self._pause_duration + self._rampup_duration \
                   + self._steady_duration
        trigger1_coord = self._pause_duration / duration
        trigger2_coord = (self._pause_duration + \
                          self._rampup_duration) / duration

        return trigger1_coord, trigger2_coord

    def onTriggerMove(self, trigger1_coord, trigger2_coord):
        return trigger1_coord < trigger2_coord

    def update_coordinates(self, trigger1_coord, trigger2_coord):

        duration = self._pause_duration + self._rampup_duration \
                   + self._steady_duration
        self._pause_duration = trigger1_coord * duration
        self._rampup_duration = trigger2_coord * duration \
                                - self._pause_duration
        self._steady_duration = duration - self._pause_duration \
                                - self._rampup_duration


class LoadTestAdapter(TestAdapter, LoadTest):

    config_code = "load"

    def get_pretty_coordinates(self):

        trigger1_coord = self._delay / self._duration)
        trigger2_coord = None

        return trigger1_coord, trigger2_coord

    def onTriggerMove(self, **args):
        return True

    def update_coodinates(self, trigger1_coord, **args):
        self._delay = trigger1_coord * self._duration;

class WidgetController(object):

    _test = None
    ...

    def find(self):
        pass

    def show(self, config):

        """
        Get subclass of TestAdapter with matched configuration code
        from json config file
        """

        test_cls = [cls for cls in TestAdapter.__subclasses__()
                    if cls.config_code == config.type][0]

        """
        Initialize object of matched class
        """
        self._test = test_cls()

        for i, trigger_coord in \
            self._test.get_pretty_coordinates().enumerate():

            if trigger_coord == None:
                self.find('.trigger%d' %i).position = None
                self.find('.trigger%d' %i).toggle(True)
            else:
                self.find('.trigger%d' %i).goAt(trigger_coord)

    def onTriggerMove(self):
        self._test.onTriggerMove(
            self.find('.trigger1').position,
            self.find('.trigger2').position)

    def save(self):
        self._test.update_coodinates(
            self.find('.trigger1').position,
            self.find('.trigger2').position)
