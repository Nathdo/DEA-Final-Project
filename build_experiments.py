import pandas as pd 
import numpy as np
from dealib import dea
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from build import Year
from build import data_expense_income, data_staff
from experiments import Experience1, Experience2, Experience3, Experience4, Experience5

data = pd.read_excel('Data.xlsx', sheet_name = 'Fact_Academy')
data_original = data.copy()


## Prepare data for all Years
data_2014 = Year(data = data, year = 2014) 
data_2016 = Year(data = data, year = 2016) 
data_2021 = Year(data = data, year = 2021) 
data_2023 = Year(data = data, year = 2023) 

#------------------------------------------------------------------------------------------------------------------------------------------
## Experience 1 - Student Enrollment Efficiency

# Marketing Expenses
marketing_expenses = data_expense_income(column_name = 'Marketing_Expenses', expanse_code = 4)
# Administratif Staff
admin_staff = data_staff(column_name = 'Administratif_Staff', staff_code = 4)

#### Institute Data
# Institution Type
dim_institute = pd.read_excel('Data.xlsx', sheet_name = 'Dim_Institutions_YearCode')
# Institution Names 
institute_name = pd.read_excel('Data.xlsx', sheet_name = 'Dim_Institutions')
institute_name = institute_name.drop(['InstitutionOpenAlex_ID'], axis = 1)
final_institute = pd.merge(dim_institute, institute_name, on = ['Institution_Code'], how = 'inner')

exp1_2014 = Experience1(data = data_2014, marketing_expenses = marketing_expenses, admin_staff = admin_staff, final_institute = final_institute)
exp1_2016 = Experience1(data = data_2016, marketing_expenses = marketing_expenses, admin_staff = admin_staff, final_institute = final_institute)
exp1_2021 = Experience1(data = data_2021, marketing_expenses = marketing_expenses, admin_staff = admin_staff, final_institute = final_institute)
exp1_2023 = Experience1(data = data_2023, marketing_expenses = marketing_expenses, admin_staff = admin_staff, final_institute = final_institute)

#------------------------------------------------------------------------------------------------------------------------------------------
## Experience 2 - Research Efficiency

# Teaching and Research Expenses
teaching_reseach_expenses = data_expense_income(column_name = 'Teaching&Research_Expenses', expanse_code = 2)
# Senior Academic Staff
senior_staff = data_staff(column_name = 'Senior_Staff', staff_code = 1)
# Publications & Citations
mention = pd.read_excel('Data.xlsx', sheet_name = 'OpenAlex_Data').drop(['InstitutionOpenAlex_ID', 'Site_code'], axis = 1)


exp2_2014 = Experience2(data = data_2014, teaching_reseach_expenses = teaching_reseach_expenses, senior_staff = senior_staff, mention = mention,
                        final_institute = final_institute)
exp2_2016 = Experience2(data = data_2016, teaching_reseach_expenses = teaching_reseach_expenses, senior_staff = senior_staff, mention = mention,
                        final_institute = final_institute)
exp2_2021 = Experience2(data = data_2021, teaching_reseach_expenses = teaching_reseach_expenses, senior_staff = senior_staff, mention = mention,
                        final_institute = final_institute)
exp2_2023 = Experience2(data = data_2023, teaching_reseach_expenses = teaching_reseach_expenses, senior_staff = senior_staff, mention = mention,
                        final_institute = final_institute)

#------------------------------------------------------------------------------------------------------------------------------------------
## Experience 3 - Financial Efficiency

# Marketing Expenses
marketing_expenses = data_expense_income(column_name = 'Marketing_Expenses', expanse_code = 4)
# Administratif Staff
admin_staff = data_staff(column_name = 'Administratif_Staff', staff_code = 4)
# Incomes
income_data = data_expense_income(column_name = 'Incomes', expanse_code = 5)

exp3_2014 = Experience3(data = data_2014, marketing_expenses = marketing_expenses, admin_staff = admin_staff, income_data = income_data,
                        final_institute = final_institute)
exp3_2016 = Experience3(data = data_2016, marketing_expenses = marketing_expenses, admin_staff = admin_staff, income_data = income_data,
                         final_institute = final_institute)
exp3_2021 = Experience3(data = data_2021, marketing_expenses = marketing_expenses, admin_staff = admin_staff, income_data = income_data,
                         final_institute = final_institute)
exp3_2023 = Experience3(data = data_2023, marketing_expenses = marketing_expenses, admin_staff = admin_staff, income_data = income_data,
                         final_institute = final_institute)
#------------------------------------------------------------------------------------------------------------------------------------------
## Experience 4 - Global Performance Efficiency

exp4_2014 = Experience4(data = data_2014, marketing_expenses = marketing_expenses, admin_staff = admin_staff, senior_staff = senior_staff, 
                        mention = mention, final_institute = final_institute)
exp4_2016 = Experience4(data = data_2016, marketing_expenses = marketing_expenses, admin_staff = admin_staff, senior_staff = senior_staff, 
                        mention = mention, final_institute = final_institute)
exp4_2021 = Experience4(data = data_2021, marketing_expenses = marketing_expenses, admin_staff = admin_staff, senior_staff = senior_staff, 
                        mention = mention, final_institute = final_institute)
exp4_2023 = Experience4(data = data_2023, marketing_expenses = marketing_expenses, admin_staff = admin_staff, senior_staff = senior_staff, 
                        mention = mention, final_institute = final_institute)

#------------------------------------------------------------------------------------------------------------------------------------------
## Experience 5 -  Infrastructure Efficiency

### Shetah Data
shetah = pd.read_excel('Data.xlsx', sheet_name = 'Gross_Area')

exp5_2014 = Experience5(data = data_2014, shetah = shetah, mention = mention, final_institute = final_institute)
exp5_2016 = Experience5(data = data_2016, shetah = shetah, mention = mention, final_institute = final_institute)
exp5_2021 = Experience5(data = data_2021, shetah = shetah, mention = mention, final_institute = final_institute)
exp5_2023 = Experience5(data = data_2023, shetah = shetah, mention = mention, final_institute = final_institute)