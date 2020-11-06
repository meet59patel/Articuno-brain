import torch
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cdist

model = SentenceTransformer('bert-base-nli-mean-tokens')


def compare(text1, text2, model=model):
    sent1 = text1.split('. ')
    sent2 = text2.split('. ')
    og_score = None
    for s in sent1:
        # print(model.encode(s))
        if og_score:
            # print(og_score)
            og_score = np.add(model.encode(s), og_score)
        else:
            og_score = model.encode(s)

    new_score = None
    for s in sent2:
        if new_score:
            # print(og_score)
            new_score = np.add(model.encode(s), new_score)
        else:
            new_score = model.encode(s)
    return 1 - cdist(og_score.reshape(1, og_score.shape[0]), new_score.reshape(1, og_score.shape[0]), "cosine")[0]
