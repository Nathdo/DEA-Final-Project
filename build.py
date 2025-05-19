import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

def Year(data, year):
    ''' 
    Return specific year.
    '''
    data = data[data.Year == year].reset_index(drop = True)
    return data

def data_expense_income(column_name, expanse_code):
    ''' 
    Return all differents expenses data (or income if expanse_code = 5). 
    '''
    expenses = pd.read_excel('Data.xlsx', sheet_name = 'Expanses_Orederd1')
    expenses = expenses[expenses.Expanse_Code == expanse_code].drop('Expanse_Code', axis = 1)
    expenses = expenses.rename(columns = {'Amount': column_name}).reset_index(drop = True)
    return expenses

def data_staff(column_name, staff_code):
    ''' 
    Return all differents staff data. 
    '''
    staff = pd.read_excel('Data.xlsx', sheet_name = 'Staff_Oredered1')
    staff = staff[staff.Staff_Type == staff_code].drop('Staff_Type', axis = 1)
    staff = staff.rename(columns = {'Staff_Amount': column_name}).reset_index(drop = True)
    return staff


<<<<<<< HEAD
def bar_plot(data, Institution_ID:int, year:int, exp_num:int, show:bool=False):
    ''' 
    Return Efficiency BarChart or store it for later display.

    args:
        data: Tuple (efficiency_scores, institution_names)
        Institution_ID: 1 for universities, 0 for colleges
        year: Year of the analysis
        show: If True, shows the plot immediately
    '''
    eff_scores, institution_names = data
    df_eff = pd.DataFrame({'Institution': institution_names, 'Efficiency Score': eff_scores})
    institute = 'Universities' if Institution_ID == 1 else 'Colleges'

    df_eff['Category'] = df_eff['Efficiency Score'].apply(lambda x: 'Reference' if x == 1.0 else 'Benchmarked')
    colors = {'Reference': 'royalblue', 'Benchmarked': 'skyblue'}

    if show:
        sns.set(style = "whitegrid")
        fig, ax = plt.subplots(figsize = (15, 5))
        ax = sns.barplot(data = df_eff, y = 'Institution', x = 'Efficiency Score', hue = 'Category', dodge = False, palette = colors)
        ax.set_xlim(0, 1.1)
        ax.set_title(f'DEA Efficiency Scores – Experiment {exp_num} - {institute} ({str(year)})', fontsize = 16)
        ax.bar_label(ax.containers[0], fmt = "%.2f", label_type = "edge", fontsize = 10)
        plt.legend(title = 'Institution Type', loc = 'lower right')
        plt.tight_layout()
        plt.show()
    else:
        'Turn show to True to see the graphic result.'


=======
>>>>>>> 254f8ad (Restored files from temp_safety)


