#! /usr/bin/env python
# coding=utf-8

import tweepy
import os
from covid19_data import JHU
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

confirmed = (JHU.Brazil.confirmed)
deaths = (JHU.Brazil.deaths)
recovered = (JHU.Brazil.recovered)

mystring = f"""COVID-19 no Brasil

Casos confirmados: {confirmed:,}
Mortes: {deaths:,}
Recuperados: {recovered:,}

Fonte: https://systems.jhu.edu/research/public-health/ncov/"""

api.update_status(mystring)
