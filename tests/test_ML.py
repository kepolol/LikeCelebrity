import sys
import os
sys.path.append("ML/")
from blackbox import Blackbox
from annoy1 import save_to_annoy
from time import time

model = Blackbox(1)


def test_detection():
    assert model.send_picture('tests/1_test.jpg')[0] == [7]
    assert model.send_picture('tests/2_test.jpg') is None


def test_annoy_save():
    save_to_annoy(10, ann_path='tests/stars_embeddings.ann')
    assert time() - os.stat('tests/stars_embeddings.ann')[8] < 10
