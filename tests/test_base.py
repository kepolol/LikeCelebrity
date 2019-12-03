import pytest
import sys
sys.path.append("vkbot/")
from models import Feedback
sys.path.append("vkbot/")
from create_db import init_db, Session


@pytest.fixture()
def init_base():
    init_db()

def test_check_defult_feedback(init_base):
    session = Session()
    check = session.query(Feedback.positive).filter(Feedback.id_ == 2).first()[0]
    assert check == 0
 