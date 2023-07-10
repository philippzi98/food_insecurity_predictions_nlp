import pandas as pd
import datetime as dt
from datetime import datetime
import numpy as np
from sklearn.preprocessing import StandardScaler
import stattools
import re
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk import Tree
from nltk.stem import PorterStemmer

from argparse import ArgumentParser

arguments = ArgumentParser()
arguments.add_argument('--level', type=str, default="country")
arguments.add_argument('--use_news', type=int, default=True)
arguments.add_argument('--use_ipc', type=int, default=True)
arguments.add_argument('--algorithm', type=str, default="Lasso")
arguments.add_argument('--k_cluster', type=int, default=3)
args = arguments.parse_args()

tag = 'word2vec-expanded'

def get_cause_by_country(k, writer):
    return {'niger': [[u'war',
		   u'conflict',
		   u'fighting',
		   u'struggle',
		   u'fight',
		   u'wars',
		   u'iraq',
		   u'continuing',
		   u'conflicts',
		   u'battles'],
		  [u'weather',
		   u'climate',
		   u'conditions',
		   u'drought',
		   u'impact',
		   u'winter',
		   u'rainy',
		   u'rain',
		   u'warming',
		   u'storms'],
		  [u'bringing',
		   u'efforts',
		   u'continuing',
		   u'country',
		   u'aid',
		   u'government',
		   u'continue',
		   u'support',
		   u'concern',
		   u'concerned'],
		  [u'migration',
		   u'refugee',
		   u'refugees',
		   u'displacement',
		   u'displaced',
		   u'exodus',
		   u'influx',
		   u'emigration',
		   u'camps',
		   u'repatriation'],
		  [u'pests',
		   u'crops',
		   u'crop',
		   u'pest',
		   u'epidemics',
		   u'outbreaks',
		   u'susceptible',
		   u'insect',
		   u'infestation',
		   u'livestock']],
		 'somalia': [[u'war',
		   u'conflict',
		   u'fighting',
		   u'struggle',
		   u'fight',
		   u'wars',
		   u'iraq',
		   u'continuing',
		   u'conflicts',
		   u'battles'],
		  [u'weather',
		   u'climate',
		   u'conditions',
		   u'drought',
		   u'impact',
		   u'winter',
		   u'rainy',
		   u'rain',
		   u'warming',
		   u'storms'],
		  [u'bringing',
		   u'efforts',
		   u'continuing',
		   u'country',
		   u'aid',
		   u'government',
		   u'continue',
		   u'support',
		   u'concern',
		   u'concerned'],
		  [u'migration',
		   u'refugee',
		   u'refugees',
		   u'displacement',
		   u'displaced',
		   u'exodus',
		   u'influx',
		   u'emigration',
		   u'camps',
		   u'repatriation'],
		  [u'pests',
		   u'crops',
		   u'crop',
		   u'pest',
		   u'epidemics',
		   u'outbreaks',
		   u'susceptible',
		   u'insect',
		   u'infestation',
		   u'livestock']],
		 'sousudan': [[u'war',
		   u'conflict',
		   u'fighting',
		   u'struggle',
		   u'fight',
		   u'wars',
		   u'iraq',
		   u'continuing',
		   u'conflicts',
		   u'battles'],
		  [u'weather',
		   u'climate',
		   u'conditions',
		   u'drought',
		   u'impact',
		   u'winter',
		   u'rainy',
		   u'rain',
		   u'warming',
		   u'storms'],
		  [u'bringing',
		   u'efforts',
		   u'continuing',
		   u'country',
		   u'aid',
		   u'government',
		   u'continue',
		   u'support',
		   u'concern',
		   u'concerned'],
		  [u'migration',
		   u'refugee',
		   u'refugees',
		   u'displacement',
		   u'displaced',
		   u'exodus',
		   u'influx',
		   u'emigration',
		   u'camps',
		   u'repatriation'],
		  [u'pests',
		   u'crops',
		   u'crop',
		   u'pest',
		   u'epidemics',
		   u'outbreaks',
		   u'susceptible',
		   u'insect',
		   u'infestation',
		   u'livestock']]}


# countries = ["afghanistan", "angola", "ethiopia", "haiti", "kenya", "malawi",
#              "niger", "rwanda", "sousudan", "sudan", "tanzania",
#              "uganda", "yemen", "zambia", "zimbabwe", "somalia"]
countries = ["somalia", "sousudan", "niger"]

ipc_int_only = pd.read_csv('./ipc_int_only.csv')
output_type = 'FEWS'
levels = ['country', 'province', 'district']
combinations = [(True, False), (False, True), (True, True)]
algorithms = ['Lasso'] #['OLS', 'Lasso', 'Lasso-Residual', 'GLM', 'GLM-Residual']
level = args.level
k_cluster = args.k_cluster
writer = pd.ExcelWriter('Seeded_Cluster_Counts.xlsx')
cause_by_country = get_cause_by_country(k_cluster, writer)
algo = args.algorithm
use_news = args.use_news
use_ipc = args.use_ipc
country_district_years = pd.read_csv('../3. Fig3_prediction/famine-country-province-district-years-CS.csv', encoding = 'utf-8')
results = {}
all_vars_sc_mat = pd.DataFrame()
dirs = {'sousudan': ['8kwbnl5ra2', 'v2sfnyhw76', '00n9tddeof'], 'somalia': ['qxouljamf4', 'enkmxirlm7', 'cuyfxytf4c'], 'niger': ['etcyeobnwt', 'hgfwbzykjc', 'zjhlprqv9m']}
for country in countries:
    match = country
    if country == "sousudan":
        match = "south sudan"
    for district in np.unique(country_district_years[(country_district_years['country'].str.strip().apply(lambda x: x.lower()) == match)][level]):
        if district != district:
            continue
        all_vars = pd.DataFrame()
        if use_news:
            for words in np.unique(cause_by_country[country]):
                w_df = {'date': [], 'wc': []}
                def read_df():
                    for r in df.iterrows():
                        count = 0
                        for word in words:
                            if re.search(word, r[1]['body'], re.IGNORECASE): #and re.search(district, r[1]['body'], re.IGNORECASE):
                                count += 1
                        w_df['date'].append(r[1]['publication_datetime'])
                        w_df['wc'].append(count)
                for dir_name in dirs[country]:
                    df = pd.read_csv('./templates-v3/{}/{}/tmp0.csv'.format(country, dir_name))
                    read_df()
                for t in range(25):
                    df = pd.read_csv("./templates-v3/{}/tmp{}.csv".format(country, str(t).zfill(2)))
                    read_df()
                timelines = [dt.datetime.fromtimestamp(i/1000) for i in w_df['date']]
                wc_df = pd.DataFrame(np.array(w_df['wc']).transpose(), index=timelines, columns=['_'.join(words)])
                wc_df.index = pd.to_datetime(wc_df.index)
                wc_df = wc_df.resample('M').mean()
                wc_df.fillna(0, inplace=True)
                all_vars = pd.concat([all_vars, wc_df], axis=1)
#             all_vars.to_csv('news_variables_{}.csv'.format(country))
#             plt.plot(wc_df.resample('3M').mean(), label=word)

        if use_ipc:
            for c in ipc_int_only.columns.values:
                if c=='Country' or c=='Unnamed: 0' or c == 'IPC_Outcome':
                    continue
                i_df = ipc_int_only[ipc_int_only['Country'].str.strip().apply(lambda x: x.lower()) == match][c]
                i_df.index = pd.to_datetime(i_df.index)
                i_df = i_df.resample('M').mean().interpolate(axis=0)
                all_vars = pd.concat([all_vars, i_df], axis=1)

        if output_type == 'FEWS':
            cy = country_district_years[(country_district_years['country'].str.strip().apply(lambda x: x.lower()) == match) & (country_district_years[level] == district)]
            fews_timeline = pd.Series(cy['CS'].values, [datetime(year=y, month=m, day=1) for y,m in zip(cy['year'].values, cy['month'].values)])
            fews_timeline.index = pd.to_datetime(fews_timeline.index)
            fews_ts = fews_timeline.replace(99.0, 0.0).replace(66.0, 0.0).replace(88.0, 0.0).resample('M').mean()
#                             fews_ts = fews_ts.reset_index()
            fews_ts = fews_ts.interpolate(axis=0)
            all_vars = pd.concat([all_vars, fews_ts], axis=1)
        else:
            i_df = ipc_int_only[ipc_int_only['Country'].str.strip().apply(lambda x: x.lower()) == match]['IPC_Outcome']
            i_df.index = pd.to_datetime(i_df.index)
            i_df = i_df.resample('3M').mean().fillna(0)
            all_vars = pd.concat([all_vars, i_df], axis=1)

        s = [-1] + [i for i in range(len(all_vars.columns.values)-1)]
#         print (all_vars.columns.values[s])
        all_vars = all_vars[all_vars.columns.values[s]]
        features = all_vars.columns.values[1:]
        output_col = all_vars.columns.values[0]
        all_vars = all_vars.resample('M').mean() #.dropna(axis=0,how='all')
        all_vars = all_vars.interpolate(axis=0).fillna(method="pad", axis=0).fillna(method="backfill", axis=0)
        all_vars = all_vars.dropna(subset=[output_col], axis=0)
        all_vars = all_vars.fillna(0, axis=0)
        all_vars = all_vars['2009-07-01':'2017-10-01']
        if all_vars.isnull().values.any():
            print (all_vars)
        mat_scaled = StandardScaler()
        mat_sc = mat_scaled.fit_transform(all_vars[:] [features])
        all_vars_s = pd.DataFrame(mat_sc, columns=features)
        all_vars_mat = pd.concat([all_vars[:][output_col].reset_index()[output_col], all_vars_s], axis=1, ignore_index=True)
#         all_vars = all_vars.resample('3M').mean().fillna(0)

        if all_vars.shape[0] == 0:
            print ('No data found for {}, {}'.format(country, district))
            continue
        all_vars_sc_mat = pd.concat([all_vars_sc_mat, all_vars_mat], axis=0, ignore_index=True)

all_vars_sc = all_vars_sc_mat.fillna(0).as_matrix()
if algo == "Lasso":
	auc, error, coeff, best_vars, pred = stattools.grangercausalitytests(all_vars_sc, all_vars_sc, mxlg=3, alpha=5e-6)
elif algo == "OLS":
	auc, error, coeff, best_vars, pred = stattools.grangercausalitytests(all_vars_sc, all_vars_sc, mxlg=3, alpha=0)
elif algo == "GLM":
	auc, error, coeff, best_vars, pred = stattools.grangercausalitytests(all_vars_sc, all_vars_sc, mxlg=3, alpha=0, glm=True)

pred_df = pd.DataFrame(list(zip(fews_ts, pred)), columns=['actual', 'pred'])
pred_df.to_csv('{}-{}-{}-{}-{}-{}-{}.csv'.format(level, k_cluster, tag, algo, error, use_news, use_ipc))
print (level, k_cluster, tag, algo, error, use_news, use_ipc, np.shape(all_vars_sc))

# List of 167 news features selected based on non-zero coefficient.
print (coeff)

