#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:29:05 2019

@author: jaketoruk
"""

import pandas as pd
import numpy as np





###______________________
# unir dataframe user con seccion

unidas = df_seccion.merge(df_user, left_on='user_id', right_on='id')

unidas = unidas.drop('id', axis = 1)
unidas.isnull().sum()