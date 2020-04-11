import pandas as pd
from sklearn.metrics import f1_score, confusion_matrix, precision_recall_fscore_support

def prf1_score_img(gt, pre):
    r, p, f, s = precision_recall_fscore_support(gt.flatten(),pre.flatten(),average=None)
    ndf = pd.DataFrame()
    ndf['Recall'] = r
    ndf['Precision'] = p
    ndf['F1'] = f
    ndf['Support'] = s
    return ndf

