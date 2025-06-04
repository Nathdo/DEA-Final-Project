# Effectiveness - How an institution has evolved over time
import pandas as pd 
import numpy as np
from dealib import dea
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from build import bar_plot

from build_experiments import (
    exp1_2014, exp1_2016, exp1_2021, exp1_2023,
    exp2_2014, exp2_2016, exp2_2021, exp2_2023,
    exp3_2014, exp3_2016, exp3_2021, exp3_2023,
    exp4_2014, exp4_2016, exp4_2021, exp4_2023,
    exp5_2014, exp5_2016, exp5_2021, exp5_2023)

# Concatenate all years for all experiement
exp1_all_years = pd.concat([exp1_2014, exp1_2016, exp1_2021, exp1_2023], ignore_index = True)
exp2_all_years = pd.concat([exp2_2014, exp2_2016, exp2_2021, exp2_2023], ignore_index = True)
exp3_all_years = pd.concat([exp3_2014, exp3_2016, exp3_2021, exp3_2023], ignore_index = True)
exp4_all_years = pd.concat([exp4_2014, exp4_2016, exp4_2021, exp4_2023], ignore_index = True)
exp5_all_years = pd.concat([exp5_2014, exp5_2016, exp5_2021, exp5_2023], ignore_index = True)


def run_temporal_dea(data, input_vars, output_vars, exp_num = 1, institution_type = 1, show = True, figsize:tuple = (18, 7)):
    """
    Run DEA treating each institution-year pair as a separate DMU (temporal analysis).

    Args:
        data (DataFrame): Full dataset across years for one experiment.
        input_vars (list): List of input column names.
        output_vars (list): List of output column names.
        exp_num (int): Experiment number for title purposes.
        institution_type (int): 1 = universities, 2 = colleges, 0 = all types.
        show (bool): If True, display the plots.

    Returns:
        tuple: (efficiency_scores, dmu_names)
    """
    data = data.copy()

    # Ensure Institution_TypeID is numeric
    data['Institution_TypeID'] = data['Institution_TypeID'].astype(int)

    # Filter by institution type
    if institution_type in [1, 2]:
        data = data[data['Institution_TypeID'] == institution_type]

    # Create DMU names
    data['DMU_Name'] = data['Institution_Name'] + " (" + data['Year'].astype(str) + ")"
    data = data.sort_values(['Institution_Name', 'Year'])

    # Prepare inputs, outputs, and names
    inputs = data[input_vars].to_numpy()
    outputs = data[output_vars].to_numpy()
    dmu_names = data['DMU_Name'].tolist()

    # Run DEA
    dea_model = dea(inputs, outputs, rts='crs', orientation='input')
    eff_scores = dea_model.eff

    if show:
        bar_plot(
            data = (eff_scores, dmu_names, np.zeros_like(eff_scores)),  # dummy for lambdas
            Institution_ID = institution_type,
            year = 999,
            exp_num = exp_num,
            show=True,
            lambdas=False, figsize = figsize)

        eff_df = pd.DataFrame({
            'Institution': [name.split(' (')[0] for name in dmu_names],
            'Year': [int(name.split('(')[1].replace(')', '')) for name in dmu_names],
            'Efficiency': eff_scores})
        pivot_df = eff_df.pivot(index='Institution', columns='Year', values='Efficiency').sort_index()

        plt.figure(figsize = figsize)
        palette = sns.color_palette('tab10', n_colors=len(pivot_df.index))
        for i, inst in enumerate(pivot_df.index):
            plt.plot(
                pivot_df.columns,
                pivot_df.loc[inst],
                marker='D',
                linestyle='-',
                linewidth=2,
                label=inst,
                color=palette[i % len(palette)])
            for year, val in pivot_df.loc[inst].items():
                plt.text(year, val + 0.02, f"{val:.2f}", ha='center', va='bottom', fontsize = 8)

        plt.title(f"Efficiency Evolution Over Time – Experiment {exp_num}", fontsize = 16)
        plt.xlabel("Year")
        plt.ylabel("Efficiency Score")
        plt.ylim(0, 1.1)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), title = "Institution")
        plt.tight_layout()
        plt.show()

    return eff_scores, dmu_names
