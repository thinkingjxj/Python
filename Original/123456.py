import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from scipy.stats import ks_2samp
from sklearn import preprocessing
from sklearn import metrics
from xgboost.sklearn import XGBRegressor
from sklearn import utils
from numpy import nan as NA
from sklearn.externals import joblib

if __name__ == '__main__':
    # data = pd.read_csv('C:\\Users\\Public\\ceshi\\xinyanbingjianzonghe.csv',encoding = 'ANSI')
    data = pd.read_csv('C:/Users/luna/Desktop/bsd/shandietest.csv',encoding = 'ANSI')