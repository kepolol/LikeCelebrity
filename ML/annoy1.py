import sys
sys.path.append("../")
import numpy as np
from gensim.similarities.index import AnnoyIndex
from setup import annoy_model_path
import os
import re

N_TREES = 1000
EMBEDDINGS_DIR = '/Users/mac/GIT/LikeCelebrity/CelebsEmbeddings/'

def save_to_annoy(n_trees=N_TREES, embs_path=EMBEDDINGS_DIR, ann_path=annoy_model_path, metrica='euclidean'):
    dict_of_files = {}
    ordered_npzs = []
    for name in os.listdir(embs_path):
        dict_of_files[int(re.match('[0-9]+', name).group(0))] = name
    for el in sorted(dict_of_files.items()):
        ordered_npzs.append(el[1])

    annoy = AnnoyIndex(128, metrica)
    
    for file in ordered_npzs:
        data = np.load(embs_path+file)
        embedding, index = data['arr_0'], data['arr_1']
        for idx in range(index.shape[0]):
            annoy.add_item(index[idx], embedding[idx])

    annoy.build(n_trees)
    annoy.save(ann_path)
    print('saved correctly at {}'.format(ann_path))
    

def load_annoy(ann_path=ANNOY_PATH, metrica='euclidean'):
    annoy = AnnoyIndex(128, metrica)
    print('Loading annoy...')
    annoy.load(ann_path)
    return annoy


def get_nns(annoy, embedding, n_neighbors):
    #annoy = load_from_annoy()
    index = annoy.get_nns_by_vector(embedding, n_neighbors)
    return index


if __name__ == '__main__':
    save_to_annoy()