from PreprocessText import *
from CalculateProbabilityElement import *

def predict(mail, setBagOfWord, labels, bayesMatrix):
    mail = rawTextPreprocess(mail)
    print("--> After preprocess:")
    print(mail)

    vector = np.zeros(len(setBagOfWord))
    for i, word in enumerate(setBagOfWord):
        if word in mail:
            vector[i] = 1
    log = np.zeros(2)

    predictSpam = probabilityOfSpam(labels)
    predictNonSpam = probabilityOfNonSpam(labels)

    for i, v in enumerate(vector):
        if v == 0:
            predictSpam *= bayesMatrix[i][1]
            predictNonSpam *= bayesMatrix[i][3]
        else:
            predictSpam *= bayesMatrix[i][0]
            predictNonSpam *= bayesMatrix[i][2]

        if predictSpam < 1e-10:
            predictSpam *= 1000
            log[0] += 1

        if predictNonSpam < 1e-10:
            predictNonSpam *= 1000
            log[1] += 1
    print("***** RESULT *****")
    print("+ predict spam = " + str(predictSpam))
    print("+ predict non spam = " + str(predictNonSpam))

    if compare(predictSpam, predictNonSpam, log):
        return 1
    return 0


def compare(predictSpam, predictNonSpam, log):
    while (log[0] > log[1]):
        predictSpam /= 1000
        log[0] -= 1
        # if predictSpam > predictNonSpam:
        #     return True

    while (log[1] > log[0]):
        predictNonSpam /= 1000
        log[1] -= 1
        # if predictNonSpam > predictSpam:
        #     return False

    if predictSpam > predictNonSpam:
        return True
    return False