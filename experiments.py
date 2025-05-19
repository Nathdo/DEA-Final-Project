import pandas as pd
import numpy as np 

def Experience1(data, marketing_expenses, admin_staff, final_institute):
    ''' 
    Experience 1 - Student Enrollment Efficiency
    inputs == Marketing Expenses, Administrative Staff 
    outputs == Students
    '''
    data = data[['Institution_YearCode', 'Year', 'Students']]
    data = pd.merge(data, marketing_expenses, on = ['Institution_YearCode', 'Year'], how = 'inner')
    data = pd.merge(data, admin_staff, on = ['Institution_YearCode', 'Year'], how = 'inner')
    data = pd.merge(data, final_institute, on = ['Institution_YearCode'], how = 'inner')
    data = data.drop(columns = ['Institution_Code'], axis = 1)
    return data


def Experience2(data, teaching_reseach_expenses, senior_staff, mention, final_institute):
    ''' 
    Experience 2  - Research Efficiency
    inputs == Teaching_reseach_expenses, Senior Staff
    outputs == Citation & Publication
    '''
    data = data[['Institution_YearCode', 'Year']]
    data = pd.merge(data, teaching_reseach_expenses, on = ['Institution_YearCode', 'Year'], how = 'inner')
    data = pd.merge(data, senior_staff, on = ['Institution_YearCode', 'Year'], how = 'inner')
    data = pd.merge(data, mention, on = ['Institution_YearCode'], how = 'inner')
    data = pd.merge(data, final_institute, on = ['Institution_YearCode'], how = 'inner')
    data = data.drop(columns = ['Institution_Code'], axis = 1)
    return data


def Experience3(data, marketing_expenses, admin_staff, income_data, final_institute):
    ''' 
    Experience 3 - Financial Efficiency
    inputs == Marketing Expenses, Administrative Staff 
    outputs == Incomes
    '''
    data = data[['Institution_YearCode', 'Year']]
    data = pd.merge(data, marketing_expenses, on = ['Institution_YearCode', 'Year'], how = 'inner')
    data = pd.merge(data, admin_staff, on = ['Institution_YearCode', 'Year'], how = 'inner')
    data = pd.merge(data, income_data, on = ['Institution_YearCode', 'Year'], how = 'inner')
    data = pd.merge(data, final_institute, on = ['Institution_YearCode'], how = 'inner')
    data = data.drop(columns = ['Institution_Code'], axis = 1)
    return data


def Experience4(data, marketing_expenses, admin_staff, senior_staff, mention, final_institute):
    ''' 
    Experience 4 - Global Performance Efficiency
    inputs == Administratif_Staff, Senior Staff, Marketing Expenses
    outputs == Students, Citations Count
    '''
    data = data[['Institution_YearCode', 'Year', 'Students']]
    data = pd.merge(data, marketing_expenses, on = ['Institution_YearCode', 'Year'], how = 'inner')
    data = pd.merge(data, admin_staff, on = ['Institution_YearCode', 'Year'], how = 'inner')
    data = pd.merge(data, senior_staff, on = ['Institution_YearCode', 'Year'], how = 'inner')
    data = pd.merge(data, final_institute, on = ['Institution_YearCode'], how = 'inner')
    data = pd.merge(data, mention, on = ['Institution_YearCode'], how = 'inner')
    data = data.drop(columns = ['Institution_Code', 'Publications Count'], axis = 1)
    return data


def Experience5(data, shetah, mention, admin_staff, final_institute):
    ''' 
    Experience 5 -  Infrastructure Efficiency
    inputs ==  Gross_area, Administrative Staff
    outputs == Students, Publications Count
    '''
    data = data[['Institution_YearCode', 'Year', 'Students']]
    data = pd.merge(data, final_institute, on = ['Institution_YearCode'], how = 'inner')
    data = pd.merge(data, shetah, on = ['Institution_Code'], how = 'inner')
    data = pd.merge(data, admin_staff, on = ['Institution_YearCode', 'Year'], how = 'inner')
    data = pd.merge(data, mention, on = ['Institution_YearCode'], how = 'inner')
    data = data.drop(columns = ['Institution_Code', 'Citations Count'], axis = 1)
    return data


