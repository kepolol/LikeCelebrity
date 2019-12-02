from keras.models import load_model
from annoy import load_annoy, get_nns
from image_preprocess import face2embedding

class Blackbox:
    def __init__(n_neighbors):
        self.n_neighbors = n_neighbors
        # load keras model
        self.model = load_model('model/facenet_keras.h5')
        # load annoy
        self.annoy = load_annoy('annoy/stars_embeddings.ann')

    def send_picture(image):
        face = extract_face(image)
        if face is None:
            return
        embedding = face2embedding(self.model, faces)
        indexes = get_nns(embedding, self.n_neighbors)
        return indexes
