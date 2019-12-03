from PIL import Image
from mtcnn.mtcnn import MTCNN
from numpy import asarray
from numpy import expand_dims


def face2embedding(model, data):
    emb = get_embedding(model, data)
    return asarray(emb)


def get_embedding(model, face_pixels):
    face_pixels = face_pixels.astype('float32')
    # standardize pixel values across channels (global)
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std
    # transform face into one sample
    # (160, 160, 3) -> (1, 160, 160, 3)
    samples = expand_dims(face_pixels, axis=0)
    yhat = model.predict(samples)
    return yhat[0]


def extract_face(filename, required_size=(160, 160)):
    image = Image.open(filename)
    image = image.convert('RGB')
    pixels = asarray(image)
    detector = MTCNN()
    # detect faces in the image
    results = detector.detect_faces(pixels)
    # extract the bounding box from the first face
    try:
        x1, y1, width, height = results[0]['box']
    except IndexError:
        print("There is no face on the photo!")
        return
    else:
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height
        # extract the face
        face = pixels[y1:y2, x1:x2]
        image = Image.fromarray(face)
        image = image.resize(required_size)
        return asarray(image)
