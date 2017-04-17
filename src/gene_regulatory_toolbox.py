"""
Created on Tue Jan 20 16:11:18 2017
@author: The Gene Regulatory Network dev team
"""
import os
import pandas as pd 
import numpy as np

import knpackage.toolbox as kn
from sklearn.linear_model import Lasso
from sklearn.linear_model import LassoCV
from sklearn.grid_search import GridSearchCV

def algo_lasso(X_train, Y_train, param_dict):

    lasso_model = LassoCV(
        n_alphas=param_dict['n_alphas'], fit_intercept=param_dict['fit_intercept'],
        normalize=param_dict['normalize'], max_iter=param_dict['max_iter'],
        cv=param_dict['cv'])

    lasso_model.fit(X_train, Y_train)

    return lasso_model

def run_GRN_lasso(run_parameters):
	"""
	"""
	spreadsheet = kn.get_spreadsheet_df(run_parameters['spreadsheet_name_full_path'])
	gene_list = spreadsheet.index
	tf_idx = range(int(spreadsheet.shape[0]*0.2))
	tf_spreadsheet = spreadsheet.iloc[tf_idx, :]
	
	result_df = pd.DataFrame(index=gene_list, columns=tf_spreadsheet.index)
	param_dict = {'n_alphas': 1000, 'fit_intercept': run_parameters['fit_intercept'],
     'normalize': run_parameters['normalize'], 'max_iter': 2000, 'cv': 5}

	for i in range(spreadsheet.shape[0]):
		# curr_response = spreadsheet.values[i, :].reshape(-1,1)
		curr_response = spreadsheet.values[i, :].ravel()
		curr_model = algo_lasso(tf_spreadsheet.values.T, curr_response, param_dict)
		coef = curr_model.coef_.ravel()
		 # (x-min(x))/(max(x)-min(x))
		result_df.loc[gene_list[i], :] = (coef-min(coef))/(max(coef)-min(coef))

	
	file_path = os.path.join(
		run_parameters['results_directory'], 'GRN_coefficient_result.tsv')
	result_df.to_csv(file_path, header=True, index=True, sep='\t')


    


