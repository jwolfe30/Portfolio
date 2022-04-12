# Enron Email Spam Filtering Using a Naive Bayes Classification Method
# By Josh Wolfe

# Setup environment

import random
import os
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, movie_reviews
from nltk.metrics import precision, recall, ConfusionMatrix
from collections import Counter
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression, SGDClassifier

vec = DictVectorizer(sparse=False)

# Read in ham (not spam) and spam email files
# Turns txt files into latin character based strings
# Strings broken into word units (features) using tokenize
# features are later used to train Naive Bayes

# non-spam email
ham = []
ham_count = 0
ham_emails = []

# spam email
spam = []
spam_count = 0
spam_emails = []


# function turns words into features set to TRUE
# TRUE words in each dictionary for spam and ham allows NB to compare word count for spam/ham


def features(words):
    feature_dictionary = dict([(word, True) for word in words])
    return feature_dictionary


# for loop loops through the file structure to get ham and spam txt files
# sorts those txt files into the ham and spam lists
# tokenizes the strings into words for Naive Bayes learning
for directories, subdirectories, files in os.walk(wd):
    if (os.path.split(directories)[1] == 'ham'):
        for filename in files:
            with open(os.path.join(directories, filename), encoding="latin-1") as file:
                data = file.read()
                words = word_tokenize(data)
                ham_emails.append(data)
                ham.append((features(words), "ham"))
                ham_count += 1

    if (os.path.split(directories)[1] == 'spam'):
        for filename in files:
            with open(os.path.join(directories, filename), encoding="latin-1") as file:
                data = file.read()
                words = word_tokenize(data)
                spam_emails.append(data)
                spam.append((features(words), "spam"))
                spam_count += 1

# Organize data for training and test sets

# Concatenate both lists into one big dataset
ham_spam = ham + spam

# shuffles the tuples so that the dataset is not split on ham/spam
# allows split to catch both ham and spam
random.shuffle(ham_spam)

# Set train/test split
# 10% train 90% test
split = int(len(ham_spam) * 0.01)

X_train = ham_spam[:split]
X_test = ham_spam[split:]

# Train models

NBclf = NaiveBayesClassifier.train(X_train)
print("Original Naive Bayes Classification Accuracy : ", (nltk.classify.accuracy(NBclf, X_test)) * 100)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(X_train)
print("Multinomial Naive Bayes Classification Accuracy : ", (nltk.classify.accuracy(MNB_classifier, X_test)) * 100)

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(X_train)
print("Bernoulli Naive Bayes Classification Accuracy : ", (nltk.classify.accuracy(BNB_classifier, X_test)) * 100)

SGDC_classifier = SklearnClassifier(SGDClassifier(max_iter=1000))
SGDC_classifier.train(X_train)
print("Stochastic Gradient Descent (SGDC) Classification Accuracy: ",
      (nltk.classify.accuracy(SGDC_classifier, X_test)) * 100)

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(X_train)
print("Support Vector Classification Accuracy : ", (nltk.classify.accuracy(SVC_classifier, X_test)) * 100)

NuSVC_classifier = SklearnClassifier(NuSVC(max_iter=1000))
NuSVC_classifier.train(X_train)
print("Nu Support Vector Classification Accuracy : ", (nltk.classify.accuracy(NuSVC_classifier, X_test)) * 100)

LinearSVC_classifier = SklearnClassifier(LinearSVC(max_iter=1000))
LinearSVC_classifier.train(X_train)
print("Linear Support Vector Classification Accuracy : ", (nltk.classify.accuracy(LinearSVC_classifier, X_test)) * 100)

LogReg_classifier = SklearnClassifier(LogisticRegression(max_iter=1000))
LogReg_classifier.train(X_train)
print("Logistic Regression Classification Accuracy : ", (nltk.classify.accuracy(LogReg_classifier, X_test)) * 100)

# Test cases

test_mess = "Hey Alex! Would you like to buy a new car? I look forward to seeing you this weekend for our big sale!"
words = word_tokenize(test_mess)
feats = features(words)
print("According to Naive Bayes Test message is :", NBclf.classify(feats))
