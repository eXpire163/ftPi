import pytest
from mocks.MagicMock import patch, MagicMock

MockRPi = MagicMock()
modules = {
    "RPi": MockRPi,
    "RPi.GPIO": MockRPi.GPIO
}
patcher = patch.dict("sys.modules", modules)
patcher.start()


from cloningvat.hardware import Switch
import RPi.GPIO


class TestSwitch(unittest.TestCase):
    GPIO_NUM = 7
    SWITCH_NAME = "Test Switch"

    @patch("RPi.GPIO.setup")
    def test_switch_inits_gpio(self, patched_setup):
        self.switch = Switch(self.SWITCH_NAME, self.GPIO_NUM)
        patched_setup.assert_called_once_with(self.GPIO_NUM, RPi.GPIO.OUT)

    @patch("RPi.GPIO.output")
    def test_switch_without_scheduler_starts_disabled(self, patched_output):
        self.switch = Switch(self.SWITCH_NAME, self.GPIO_NUM)
        patched_output.assert_called_once_with(self.GPIO_NUM, RPi.GPIO.LOW)