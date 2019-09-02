#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:29:05 2019

@author: jaketoruk
"""

import pandas as pd
import numpy as np

df_user = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/airbnb-recruiting-new-user-bookings/train_users_2.csv')
df_country = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/airbnb-recruiting-new-user-bookings/countries.csv')
df_a_g = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/airbnb-recruiting-new-user-bookings/age_gender_bkts.csv')
df_seccion = pd.read_csv('/home/jaketoruk/Documents/Kaggle_Competition/airbnb/airbnb-recruiting-new-user-bookings/sessions.csv')

pd.options.display.max_columns = 50
###___________________
# estudio del dataframe user

df_user.isnull().sum()
df_user.shape
df_user.head()
df_user.date_first_booking.value_counts()
df_user.country_destination.value_counts()

###____________________
# estudio del dataframe country

df_country.isnull().sum()
df_country.shape
df_country.head(10)

###_____________________
# estudio del dataframe a_g

df_a_g.isnull().sum()
df_a_g.shape
df_a_g.head()


###______________________
# estudio del dataframe seccion
df_seccion.isnull().sum()
df_seccion.shape
df_seccion.action_type.value_counts()

df_seccion.action_detail.value_counts()

df_seccion.secs_elapsed.value_counts()

df_seccion.action.value_counts()

###______________________
# unir dataframe user con seccion

unidas = df_seccion.merge(df_user, left_on='user_id', right_on='id')

unidas = unidas.drop('id', axis = 1)
unidas.isnull().sum()