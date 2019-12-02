import numpy as np
from annoy import AnnoyIndex
import os
import re


class _Annoy:

    def __init__(self, annoy_path):
        self.annoy_path = annoy_path
        self.annoy = 0

    def save_to_annoy(self, n_trees=1000, embs_path='CelebsEmbeddings/', metrica='euclidean'):
        """
        Метод переводит сохраненные эмбендинги в .ann
        :param n_trees:
        :param embs_path:
        :param metrica:
        :return:
        """
        dict_of_files = {}
        new_filelist = []
        for name in os.listdir(embs_path):
            dict_of_files[int(re.match('[0-9]+', name).group(0))] = name
        for el in sorted(dict_of_files.items()):
            new_filelist.append(el[1])

        annoy = AnnoyIndex(128, metrica)

        for file in new_filelist:
            data = np.load(embs_path+file)
            embedding, index = data['arr_0'], data['arr_1']
            for idx in range(index.shape[0]):
                annoy.add_item(index[idx], embedding[idx])

        annoy.build(n_trees)
        annoy.save(self.annoy_path)
        print('saved correctly at {}'.format(self.annoy_path))

    def load_annoy(self, metrica='euclidean'):
        """
        Загрузка модели annoy
        :param metrica:
        :return:
        """
        self.annoy = AnnoyIndex(128, metrica)
        print('Loading annoy...')
        self.annoy.load(self.annoy_path)

    def get_nns(self, embedding, n_neighbors=3):
        """
        Поиск ближайших эмбендингов (фото звезд)
        :param embedding:
        :param n_neighbors:
        :return: indexes of neighbors celebrities
        """
        indexes = self.annoy.get_nns_by_vector(embedding, n_neighbors)
        return indexes