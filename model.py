import pandas as pd  # For reading xlsx file
from Predict import *

def predict_a_mail(mail):
    # get mail
    xl = pd.ExcelFile('Mail Filter Dataset.xls')
    dfs = xl.parse()
    contentMails = []
    labels = []

    for contentMail in dfs.content_mail:
        contentMails.append(rawTextPreprocess(contentMail))
        # print(contentMails[len(contentMails)-1])
        # print("====================================")
    for label in dfs.label:
        labels.append(label)

    setBagOfWord = set()

    for contentMail in contentMails:
        words = contentMail.split(' ')
        for word in words:
            setBagOfWord.add(word)

    vectors = createVector(dfs.content_mail, setBagOfWord)
    bayesMatrix = componentProbability(setBagOfWord, vectors, labels)
    return predict(mail, setBagOfWord, labels, bayesMatrix)
    # print(setBagOfWord)
    # for i in range(len(bayesMatrix)):
    #     for j in range(len(bayesMatrix[i])):
    #         print("a[" + str(i) + "," + str(j) + "] = " + str(bayesMatrix[i][j]))
    #     print()

    # file = pd.ExcelFile('Book1.xls')
    # temp = file.parse("Sheet1")
    #
    #
    # for contentMail in temp.content_mail:
    #     print("***** CONTENTS OF MAIL *****")
    #     print(contentMail)
    #     if predict(contentMail, setBagOfWord, labels, bayesMatrix) == 1:
    #         print("===> Email spam")
    #     else:
    #         print("===> Email non spam")
    #     print("======================================================================")

