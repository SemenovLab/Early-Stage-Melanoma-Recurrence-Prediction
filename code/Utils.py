'''
Prediction of Early-Stage Melanoma Recurrence Using Clinical and Histopathologic Features

Guihong Wan, July/27/2022
Massachusetts General Hospital, Harvard Medical School
'''

import pandas as pd
import numpy as np

from sklearn.metrics import precision_score, recall_score, accuracy_score, confusion_matrix, roc_auc_score
import scipy.stats as st


def getmeanAndCI(target, name="", LOG=True):
    '''
       Compute the mean and 95% confidence interval of the input values.
       @target: a list of values

    '''
    CI = st.t.interval(alpha=0.95, 
              df=len(target)-1, 
              loc=np.mean(target), 
              scale=st.sem(target))
    mu = np.mean(target)
    if LOG: print(f"{name}:{round(mu, 3)}\n CI:{round(CI[0], 3)}-{round(CI[1], 3)}")
    return mu, CI

def get_specificity(ground_truth, predictions):
    tp, tn, fn, fp = 0.0,0.0,0.0,0.0
    for l,m in enumerate(ground_truth):        
        if m==predictions[l] and m==1:
            tp+=1
        if m==predictions[l] and m==0:
            tn+=1
        if m!=predictions[l] and m==1:
            fn+=1
        if m!=predictions[l] and m==0:
            fp+=1
    return tn/(tn+fp)

def get_TP(ground_truth, predictions):
    tp, tn, fn, fp = 0.0,0.0,0.0,0.0
    for l,m in enumerate(ground_truth):        
        if m==predictions[l] and m==1:
            tp+=1
        if m==predictions[l] and m==0:
            tn+=1
        if m!=predictions[l] and m==1:
            fn+=1
        if m!=predictions[l] and m==0:
            fp+=1
    return tp

def get_FP(ground_truth, predictions):
    tp, tn, fn, fp = 0.0,0.0,0.0,0.0
    for l,m in enumerate(ground_truth):        
        if m==predictions[l] and m==1:
            tp+=1
        if m==predictions[l] and m==0:
            tn+=1
        if m!=predictions[l] and m==1:
            fn+=1
        if m!=predictions[l] and m==0:
            fp+=1
    return fp


def baseline_fn(clf, X_train, X_test, y_train, y_test, name = '', LOG=False):
    '''
    @clf: the classifier to be trained and tested.
    @X_train: data for training
    @X_test: data for testing
    @y_train: label of training data
    @y_test: label of testing data
    '''
    
    clf.fit(X_train, y_train)
    

    # training performance
    y_train_pred = clf.predict(X_train)
    y_train_prob = clf.predict_proba(X_train)

    
    train_score = accuracy_score(y_train, y_train_pred)
    AUC = roc_auc_score(y_train, y_train_prob[:,1])
    if LOG: print("\nTrain:")
    if LOG: print(f"ACC ({name}): {round(train_score, 4)}")
    if LOG: print(f"AUC ({name}): {round(AUC, 4)}")
    
    # testing performance
    y_pred = clf.predict(X_test)
    y_prob = clf.predict_proba(X_test)
    
    test_score = accuracy_score(y_test, y_pred)
    AUC = roc_auc_score(y_test, y_prob[:,1])
    
    if LOG: print("\nTest:")
    if LOG:print(f"ACC ({name}): {round(test_score, 4)}")
    if LOG:print(f"AUC ({name}): {round(AUC, 4)}")
    
    if LOG: print(confusion_matrix(y_test, y_pred))
    
    
    sp = get_specificity(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    tp = get_TP(y_test, y_pred)
    fp = get_FP(y_test, y_pred)


    return clf, test_score, AUC, precision, recall, sp, tp, fp

