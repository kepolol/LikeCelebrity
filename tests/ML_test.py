import sys
sys.path.append("../ML")
from blackbox import Blackbox

model = Blackbox(1)


def face_detection():
    print(sys.path)
    assert model.send_picture('_test.jpg')[0] == [7]
