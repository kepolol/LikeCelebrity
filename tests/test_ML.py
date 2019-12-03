import sys
sys.path.append("ML/")
from blackbox import Blackbox

model = Blackbox(1)


def test_detection():
    assert model.send_picture('tests/_test.jpg')[0] == [7]
