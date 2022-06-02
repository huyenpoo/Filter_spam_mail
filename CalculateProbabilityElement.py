import numpy as np

def createVector(documents, setBagOfWord):
    vectors = []
    for document in documents:
        vector = np.zeros(len(setBagOfWord))
        for i, word in enumerate(setBagOfWord):
            if word in document:
                vector[i] = 1
        vectors.append(vector)
    return vectors


def smoothing(a, b):
    if a == 0 or b == 0:
        return (float) (a + 0.000001) / (b + 0.000001)
    return (float) (a) / (b)


def getMailSpam(labels):
    spam = 0
    for label in labels:
        if label == 1:
            spam += 1
    return spam

def getMailNonSpam(labels):
    nonSpam = 0
    for label in labels:
        if label == 0:
            nonSpam += 1
    return nonSpam

def probabilityOfSpam(labels):
    return smoothing(getMailSpam(labels), len(labels))


def probabilityOfNonSpam(labels):
    return smoothing(getMailNonSpam(labels), len(labels))


def componentProbability(setBagOfWord, vectors, labels):
    bayesMatrix = np.zeros((len(setBagOfWord), 4))
    amountMailSpam = getMailSpam(labels)
    amountMailNoSpam = len(labels) - getMailSpam(labels)

    for i, word in enumerate(setBagOfWord):
        mailSpamContainWord = 0
        mailSpamNoContainWord = 0
        mailNoSpamContainWord = 0
        mailNoSpamNoContainWord = 0

        for k, vector in enumerate(vectors):
            if labels[k] == 1:
                if vector[i] == 1:
                    mailSpamContainWord += 1
                else:
                    mailSpamNoContainWord += 1
            else:
                if vector[i] == 1:
                    mailNoSpamContainWord += 1
                else:
                    mailNoSpamNoContainWord += 1

        bayesMatrix[i][0] = smoothing(mailSpamContainWord, amountMailSpam)
        bayesMatrix[i][1] = smoothing(mailSpamNoContainWord, amountMailSpam)
        bayesMatrix[i][2] = smoothing(mailNoSpamContainWord, amountMailNoSpam)
        bayesMatrix[i][3] = smoothing(mailNoSpamNoContainWord, amountMailNoSpam)

    return bayesMatrix