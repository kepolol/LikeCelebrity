import sys
sys.path.append("vkbot/")
from models import Feedback
sys.path.append("vkbot/")
from create_db import Session


def test_check_default_feedback_neg():
    session = Session()
    check = session.query(Feedback.negative).filter(Feedback.id_ == 1).first()[0]
    session.close()
    assert check == 0
