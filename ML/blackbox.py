import sys
sys.path.append("../")
from setup import keras_model_path, annoy_model_path
from keras.models import load_model
from annoy1 import load_annoy, get_nns
from image_preprocess import face2embedding, extract_face


class Blackbox:
    def __init__(self, n_neighbors):
        self.face = None
        self.n_neighbors = n_neighbors
        # load keras model
        self.model = load_model(keras_model_path, compile=False)
        # load annoy
        self.annoy = load_annoy(annoy_model_path)

    def send_picture(self, image):
        face = extract_face(image)
        if face is None:
            return
        self.face = face
        embedding = face2embedding(self.model, face)
        indexes = get_nns(self.annoy, embedding, self.n_neighbors)
        # return indexes
        return indexes, face
