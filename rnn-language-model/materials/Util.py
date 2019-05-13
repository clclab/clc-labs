import numpy as np
from scipy import *

import matplotlib.pyplot as plt
from matplotlib import offsetbox
from sklearn import manifold,preprocessing

def softmax(mat):
    if len(mat.shape) == 1:
        e_mat = np.exp(mat - np.max(mat))
        return e_mat / np.sum(e_mat)
    if len(mat.shape) == 2:
        e_mat = np.exp(mat - mat.max(axis=1)[:, np.newaxis])
        return e_mat / e_mat.sum(axis=1)[:, np.newaxis]


# The Sigmoid function, which describes an S shaped curve.
# We pass the weighted sum of the inputs through this function to
# normalise them between 0 and 1.
def sigmoid(x):
        return 1 / (1 + np.exp(-x))

# The derivative of the Sigmoid function.
# This is the gradient of the Sigmoid curve.
# It indicates how confident we are about the existing weight.
def sigmoid_derivative(x):
    return x * (1 - x)


def softmax_derivative(mat):
    e_mat = np.exp(mat - mat.max(axis=1)[:, np.newaxis])
    others = e_mat.sum(axis=1)[:, np.newaxis] - e_mat
    return 1 / (2 + e_mat / others + others / e_mat)


def plot_embedding(features, classes, labels, title=None):
    x_min, x_max = np.min(features, 0), np.max(features, 0)
    features = (features - x_min) / (x_max - x_min)

    plt.figure()
    ax = plt.subplot(111)
    for i in range(features.shape[0]):
        plt.text(features[i, 0], features[i, 1], str(labels[i]),
                 color=plt.cm.Set1(float(classes[i]/60)),
                 fontdict={'weight': 'bold', 'size': 9})

    if hasattr(offsetbox, 'AnnotationBbox'):
        # only print thumbnails with matplotlib > 1.0
        shown_images = np.array([[1., 1.]])  # just something big
        for i in range(features.shape[0]):
            dist = np.sum((features[i] - shown_images) ** 2, 1)
            #if np.min(dist) < 4e-3:
                # don't show points that are too close
            #    continue
            shown_images = np.r_[shown_images, [features[i]]]
            """imagebox = offsetbox.AnnotationBbox(
                offsetbox.OffsetImage(digits.images[i], cmap=plt.cm.gray_r),
                X[i])
            ax.add_artist(imagebox)"""
    plt.xticks([]), plt.yticks([])
    if title is not None:
        plt.title(title)



def plot_distribution_t_SNE(activations, words, labels):
    print("Computing t-SNE embedding")

    x = np.asarray(activations)
    x = preprocessing.normalize(x, norm='l2')
    tsne = manifold.TSNE(n_components=2, init='pca', perplexity=2, n_iter=20000, early_exaggeration=10, learning_rate=300, method="exact")
    X_tsne = tsne.fit_transform(x)
    plot_embedding(X_tsne, np.asarray(words), labels)
    plt.show()

