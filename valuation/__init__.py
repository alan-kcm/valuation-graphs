#importing libraries 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pylab
import math
import itertools
import openpyxl 
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
pd.options.display.float_format = "{:,.1f}".format

from scipy import stats

import statsmodels.api as sm
from statsmodels.stats import diagnostic as diag
from statsmodels.stats.outliers_influence import variance_inflation_factor

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error 
