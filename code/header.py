'''
Prediction of Early-Stage Melanoma Recurrence Using Clinical and Histopathologic Features

Guihong Wan, July/27/2022
Massachusetts General Hospital, Harvard Medical School
'''

import pandas as pd
import numpy as np
import random

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score,confusion_matrix

import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import PrecisionRecallDisplay
from sklearn.metrics import precision_recall_curve

from imblearn import under_sampling, over_sampling
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

from sklearn.inspection import permutation_importance
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import Normalizer, StandardScaler, MinMaxScaler, PowerTransformer, MaxAbsScaler, LabelEncoder

import matplotlib
import math
from collections import Counter
import scipy.stats as st
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.metrics import make_scorer

from sksurv.metrics import concordance_index_censored
from sksurv.metrics import concordance_index_ipcw
from sksurv.metrics import cumulative_dynamic_auc
from sksurv.datasets import get_x_y

import eli5
from eli5.sklearn import PermutationImportance

import matplotlib.pyplot as plt

from sklearn import svm
from sklearn.metrics import auc
from sklearn.metrics import RocCurveDisplay

from sksurv.ensemble import GradientBoostingSurvivalAnalysis
from sksurv.linear_model import CoxnetSurvivalAnalysis
from sksurv.ensemble import RandomSurvivalForest
from sksurv.linear_model import CoxPHSurvivalAnalysis


import warnings
warnings.filterwarnings('ignore')

'''
35 extracted clinicopathologic features to be assessed for melanoma recurrence prediction.
Note that Melanomas with microsatellites present were excluded in this study.
'''
demographic_features = ["TrdxAgeAtDx", "GenderNm", "Race","Ethnicity","medianincome", 
                        "InsuranceType","MaritalStatus"] #7

medical_features = ['CCItotal_psuedoMedian',
                    "cmhistory",
                    'PNMSC', 'PSkin_situ_or_benigh', 'POther_cancer', 
                    'CAID_binary', 'SAID_binary'] #7

tumor_features = ["TrdxHistologyDesc", "TrdxSiteDesc",
                  "fstage",
                  "fthickness", "fAnatomicLevel",
                   "Laterality", 
                  # 
                  "newNODE",
                  "fUlceration", "fMitoses", 
                  "totalmargins", "margincheck",
                  "fTumorInfiltratingLymphocytes", "cTumorInfiltratingLymphocytes",
                  "fRadialGrowthPhase", "fVerticalGrowthPhase", "fVerticalGrowthType",
                  #
                 "fPrecursorLesion", "fPrecursortype",
                 "fMicrosatellites", "fRegression",
                 "fLymphovascularInvasion", "fPerineuralInvasion", 
                 ] # 21

# Categorical features
nomi_features = ['GenderNm', 'Race', 'Ethnicity',  'InsuranceType', 'MaritalStatus', 
                'fstage', 'TrdxSiteDesc', 'Laterality', 'TrdxHistologyDesc','fUlceration',
                'fPrecursorLesion', 'fPrecursortype', 'fRadialGrowthPhase', 'fVerticalGrowthPhase',
                'fVerticalGrowthType','fMicrosatellites', 'fRegression', 
                 'fTumorInfiltratingLymphocytes', 'cTumorInfiltratingLymphocytes',
                 'fLymphovascularInvasion','fPerineuralInvasion','margincheck',
                 'PNMSC', 'PSkin_situ_or_benigh', 'POther_cancer',
                 'CAID_binary', 'SAID_binary',
                 'newNODE'
                ]


