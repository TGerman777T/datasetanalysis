# -*- coding: utf-8 -*-
"""supersetproj.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/193EGVv6BUTrsWktLoJJiqFVyQTowT0O8
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#from mpl_toolkits.mplot3d import Axes3D
import datetime as dt
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff


#база данных
df = pd.read_csv("powerconsumption.csv")
df1 = pd.read_excel("pow1.xlsx")
