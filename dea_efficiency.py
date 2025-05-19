import pandas as pd 
import numpy as np
from dealib import dea
import warnings
warnings.filterwarnings('ignore')

def exp_dea(data, Institution_ID:list, inputs_columns:list, outputs_columns:list, method:str) -> list:
    ''' 
    Experiment Efficiency - DEA efficiency results

    args: 
        data: Experiment data year
        Institution_ID: List of the type of institutions (list of both if vrs method)
        method: 'crs' or 'vrs' method
    '''
    data = data[data.Institution_TypeID.isin(Institution_ID)]
    inputs = data[inputs_columns]
    outputs = data[outputs_columns]
    dmu = list(data['Institution_Name'])
    dea_model = dea(inputs, outputs, rts = method, orientation = "input")
    return dea_model.eff                             


#------------------------------------------------------------------------------------------------------------------------------------------
# Experiment 1
from build_experiments import exp1_2014, exp1_2016, exp1_2021, exp1_2023

# Experiment 1 - Universities
exp1_2014_uni = exp_dea(data = exp1_2014, Institution_ID = [1], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Students'], method = 'crs')
exp1_2016_uni = exp_dea(data = exp1_2016, Institution_ID = [1], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Students'], method = 'crs')
exp1_2021_uni = exp_dea(data = exp1_2021, Institution_ID = [1], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Students'], method = 'crs')
exp1_2023_uni = exp_dea(data = exp1_2023, Institution_ID = [1], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Students'], method = 'crs')

# Experiment 1 - Colleges 
exp1_2014_col = exp_dea(data = exp1_2014, Institution_ID = [2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Students'], method = 'crs')
exp1_2016_col = exp_dea(data = exp1_2016, Institution_ID = [2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Students'], method = 'crs')
exp1_2021_col = exp_dea(data = exp1_2021, Institution_ID = [2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Students'], method = 'crs')
exp1_2023_col = exp_dea(data = exp1_2023, Institution_ID = [2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Students'], method = 'crs')   

# Experiment 1 - Colleges & Universities
exp1_2014_col_uni = exp_dea(data = exp1_2014, Institution_ID = [1, 2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Students'], method = 'vrs')
exp1_2016_col_uni = exp_dea(data = exp1_2016, Institution_ID = [1, 2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Students'], method = 'vrs')
exp1_2021_col_uni = exp_dea(data = exp1_2021, Institution_ID = [1, 2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Students'], method = 'vrs')
exp1_2023_col_uni = exp_dea(data = exp1_2023, Institution_ID = [1, 2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Students'], method = 'vrs')     
#------------------------------------------------------------------------------------------------------------------------------------------
# Experiment 2
from build_experiments import exp2_2014, exp2_2016, exp2_2021, exp2_2023

# Experiment 2 - Universities
exp2_2014_uni = exp_dea(data = exp2_2014, Institution_ID = [1], inputs_columns = ['Teaching&Research_Expenses', 'Senior_Staff'] ,
                         outputs_columns = ['Publications Count', 'Citations Count'], method = 'crs')
exp2_2016_uni = exp_dea(data = exp2_2016, Institution_ID = [1], inputs_columns = ['Teaching&Research_Expenses', 'Senior_Staff'] ,
                         outputs_columns = ['Publications Count', 'Citations Count'], method = 'crs')
exp2_2021_uni = exp_dea(data = exp2_2021, Institution_ID = [1], inputs_columns = ['Teaching&Research_Expenses', 'Senior_Staff'] ,
                         outputs_columns = ['Publications Count', 'Citations Count'], method = 'crs')
exp2_2023_uni = exp_dea(data = exp2_2023, Institution_ID = [1], inputs_columns = ['Teaching&Research_Expenses', 'Senior_Staff'] ,
                         outputs_columns = ['Publications Count', 'Citations Count'], method = 'crs')

# Experiment 2 - Colleges
exp2_2014_col = exp_dea(data = exp2_2014, Institution_ID = [2], inputs_columns = ['Teaching&Research_Expenses', 'Senior_Staff'] ,
                         outputs_columns = ['Publications Count', 'Citations Count'], method = 'crs')
exp2_2016_col = exp_dea(data = exp2_2016, Institution_ID = [2], inputs_columns = ['Teaching&Research_Expenses', 'Senior_Staff'] ,
                         outputs_columns = ['Publications Count', 'Citations Count'], method = 'crs')
exp2_2021_col = exp_dea(data = exp2_2021, Institution_ID = [2], inputs_columns = ['Teaching&Research_Expenses', 'Senior_Staff'] ,
                         outputs_columns = ['Publications Count', 'Citations Count'], method = 'crs')
exp2_2023_col = exp_dea(data = exp2_2023, Institution_ID = [2], inputs_columns = ['Teaching&Research_Expenses', 'Senior_Staff'] ,
                         outputs_columns = ['Publications Count', 'Citations Count'], method = 'crs')

# Experiment 2 - Colleges & Universities
exp2_2014_col_uni = exp_dea(data = exp2_2014, Institution_ID = [1, 2], inputs_columns = ['Teaching&Research_Expenses', 'Senior_Staff'] ,
                         outputs_columns = ['Publications Count', 'Citations Count'], method = 'vrs')
exp2_2016_col_uni = exp_dea(data = exp2_2016, Institution_ID = [1, 2], inputs_columns = ['Teaching&Research_Expenses', 'Senior_Staff'] ,
                         outputs_columns = ['Publications Count', 'Citations Count'], method = 'vrs')
exp2_2021_col_uni = exp_dea(data = exp2_2021, Institution_ID = [1, 2], inputs_columns = ['Teaching&Research_Expenses', 'Senior_Staff'] ,
                         outputs_columns = ['Publications Count', 'Citations Count'], method = 'vrs')
exp2_2023_col_uni = exp_dea(data = exp2_2023, Institution_ID = [1, 2], inputs_columns = ['Teaching&Research_Expenses', 'Senior_Staff'] ,
                         outputs_columns = ['Publications Count', 'Citations Count'], method = 'vrs')
#------------------------------------------------------------------------------------------------------------------------------------------
# Experiment 3
from build_experiments import exp3_2014, exp3_2016, exp3_2021, exp3_2023

# Experiment 3 - Universities
exp3_2014_uni = exp_dea(data = exp3_2014, Institution_ID = [1], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Incomes'], method = 'crs')
exp3_2016_uni = exp_dea(data = exp3_2016, Institution_ID = [1], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Incomes'], method = 'crs')
exp3_2021_uni = exp_dea(data = exp3_2021, Institution_ID = [1], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Incomes'], method = 'crs')
exp3_2023_uni = exp_dea(data = exp3_2023, Institution_ID = [1], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Incomes'], method = 'crs')

# Experiment 3 - Universities
exp3_2014_col = exp_dea(data = exp3_2014, Institution_ID = [2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Incomes'], method = 'crs')
exp3_2016_col = exp_dea(data = exp3_2016, Institution_ID = [2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Incomes'], method = 'crs')
exp3_2021_col = exp_dea(data = exp3_2021, Institution_ID = [2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Incomes'], method = 'crs')
exp3_2023_col = exp_dea(data = exp3_2023, Institution_ID = [2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Incomes'], method = 'crs')

# Experiment 3 - Universities
exp3_2014_col_uni = exp_dea(data = exp3_2014, Institution_ID = [1, 2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Incomes'], method = 'vrs')
exp3_2016_col_uni = exp_dea(data = exp3_2016, Institution_ID = [1, 2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Incomes'], method = 'vrs')
exp3_2021_col_uni = exp_dea(data = exp3_2021, Institution_ID = [1, 2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Incomes'], method = 'vrs')
exp3_2023_col_uni = exp_dea(data = exp3_2023, Institution_ID = [1, 2], inputs_columns = ['Marketing_Expenses', 'Administratif_Staff'] ,
                         outputs_columns = ['Incomes'], method = 'vrs')
#------------------------------------------------------------------------------------------------------------------------------------------
# Experiment 4
from build_experiments import exp4_2014, exp4_2016, exp4_2021, exp4_2023

# Experiment 4 - Universities
exp4_2014_uni = exp_dea(data = exp4_2014, Institution_ID = [1], inputs_columns = ['Administratif_Staff', 'Senior_Staff', 'Marketing_Expenses'] ,
                         outputs_columns = ['Students', 'Citations Count'], method = 'crs')
exp4_2016_uni = exp_dea(data = exp4_2016, Institution_ID = [1], inputs_columns = ['Administratif_Staff', 'Senior_Staff', 'Marketing_Expenses'] ,
                         outputs_columns = ['Students', 'Citations Count'], method = 'crs')
exp4_2021_uni = exp_dea(data = exp4_2021, Institution_ID = [1], inputs_columns = ['Administratif_Staff', 'Senior_Staff', 'Marketing_Expenses'] ,
                         outputs_columns = ['Students', 'Citations Count'], method = 'crs')
exp4_2023_uni = exp_dea(data = exp4_2023, Institution_ID = [1], inputs_columns = ['Administratif_Staff', 'Senior_Staff', 'Marketing_Expenses'] ,
                         outputs_columns = ['Students', 'Citations Count'], method = 'crs')

# Experiment 4 - Colleges
exp4_2014_col = exp_dea(data = exp4_2014, Institution_ID = [2], inputs_columns = ['Administratif_Staff', 'Senior_Staff', 'Marketing_Expenses'] ,
                         outputs_columns = ['Students', 'Citations Count'], method = 'crs')
exp4_2016_col = exp_dea(data = exp4_2016, Institution_ID = [2], inputs_columns = ['Administratif_Staff', 'Senior_Staff', 'Marketing_Expenses'] ,
                         outputs_columns = ['Students', 'Citations Count'], method = 'crs')
exp4_2021_col = exp_dea(data = exp4_2021, Institution_ID = [2], inputs_columns = ['Administratif_Staff', 'Senior_Staff', 'Marketing_Expenses'] ,
                         outputs_columns = ['Students', 'Citations Count'], method = 'crs')
exp4_2023_col = exp_dea(data = exp4_2023, Institution_ID = [2], inputs_columns = ['Administratif_Staff', 'Senior_Staff', 'Marketing_Expenses'] ,
                         outputs_columns = ['Students', 'Citations Count'], method = 'crs')

# Experiment 4 - Colleges & Universities
exp4_2014_col_uni = exp_dea(data = exp4_2014, Institution_ID = [1, 2], inputs_columns = ['Administratif_Staff', 'Senior_Staff', 'Marketing_Expenses'] ,
                         outputs_columns = ['Students', 'Citations Count'], method = 'vrs')
exp4_2016_col_uni = exp_dea(data = exp4_2016, Institution_ID = [1, 2], inputs_columns = ['Administratif_Staff', 'Senior_Staff', 'Marketing_Expenses'] ,
                         outputs_columns = ['Students', 'Citations Count'], method = 'vrs')
exp4_2021_col_uni = exp_dea(data = exp4_2021, Institution_ID = [1, 2], inputs_columns = ['Administratif_Staff', 'Senior_Staff', 'Marketing_Expenses'] ,
                         outputs_columns = ['Students', 'Citations Count'], method = 'vrs')
exp4_2023_col_uni = exp_dea(data = exp4_2023, Institution_ID = [1, 2], inputs_columns = ['Administratif_Staff', 'Senior_Staff', 'Marketing_Expenses'] ,
                         outputs_columns = ['Students', 'Citations Count'], method = 'vrs')
#------------------------------------------------------------------------------------------------------------------------------------------
# Experiment 5
from build_experiments import exp5_2014, exp5_2016, exp5_2021, exp5_2023

# Experiment 5 - Universities
exp5_2014_uni = exp_dea(data = exp5_2014, Institution_ID = [1], inputs_columns = ['Administratif_Staff', 'Gross Area_2023'] ,
                         outputs_columns = ['Students', 'Publications Count'], method = 'crs')
exp5_2016_uni = exp_dea(data = exp5_2016, Institution_ID = [1], inputs_columns = ['Administratif_Staff', 'Gross Area_2023'] ,
                         outputs_columns = ['Students', 'Publications Count'], method = 'crs')
exp5_2021_uni = exp_dea(data = exp5_2021, Institution_ID = [1], inputs_columns = ['Administratif_Staff', 'Gross Area_2023'] ,
                         outputs_columns = ['Students', 'Publications Count'], method = 'crs')
exp5_2023_uni = exp_dea(data = exp5_2023, Institution_ID = [1], inputs_columns = ['Administratif_Staff', 'Gross Area_2023'] ,
                         outputs_columns = ['Students', 'Publications Count'], method = 'crs')

# Experiment 5 - Colleges
exp5_2014_col = exp_dea(data = exp5_2014, Institution_ID = [2], inputs_columns = ['Administratif_Staff', 'Gross Area_2023'] ,
                         outputs_columns = ['Students', 'Publications Count'], method = 'crs')
exp5_2016_col = exp_dea(data = exp5_2016, Institution_ID = [2], inputs_columns = ['Administratif_Staff', 'Gross Area_2023'] ,
                         outputs_columns = ['Students', 'Publications Count'], method = 'crs')
exp5_2021_col = exp_dea(data = exp5_2021, Institution_ID = [2], inputs_columns = ['Administratif_Staff', 'Gross Area_2023'] ,
                         outputs_columns = ['Students', 'Publications Count'], method = 'crs')
exp5_2023_col = exp_dea(data = exp5_2023, Institution_ID = [2],inputs_columns = ['Administratif_Staff', 'Gross Area_2023'] ,
                         outputs_columns = ['Students', 'Publications Count'], method = 'crs')

# Experiment 5 - Colleges & Universities
exp5_2014_col_uni = exp_dea(data = exp5_2014, Institution_ID = [1, 2], inputs_columns = ['Administratif_Staff', 'Gross Area_2023'] ,
                         outputs_columns = ['Students', 'Publications Count'], method = 'vrs')
exp5_2016_col_uni = exp_dea(data = exp5_2016, Institution_ID = [1, 2], inputs_columns = ['Administratif_Staff', 'Gross Area_2023'] ,
                         outputs_columns = ['Students', 'Publications Count'], method = 'vrs')
exp5_2021_col_uni = exp_dea(data = exp5_2021, Institution_ID = [1, 2], inputs_columns = ['Administratif_Staff', 'Gross Area_2023'] ,
                         outputs_columns = ['Students', 'Publications Count'], method = 'vrs')
exp5_2023_col_uni = exp_dea(data = exp5_2023, Institution_ID = [1, 2], inputs_columns = ['Administratif_Staff', 'Gross Area_2023'] ,
                         outputs_columns = ['Students', 'Publications Count'], method = 'vrs')
#------------------------------------------------------------------------------------------------------------------------------------------