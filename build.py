import pandas as pd
import numpy as np

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




