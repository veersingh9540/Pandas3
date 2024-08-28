import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    employees['bonus'] = 0 
    for i in range(len(employees)):
        Salary = employees['salary'][i]
        emp_id = employees['employee_id'][i]
        name = employees['name'][i]

        if (name.startswith("M")):
            employees['bonus'][i] = 0
        elif (emp_id %2 == 0):
            employees['bonus'][i] = 0 
        else: 
            employees['bonus'][i] = Salary

    return employees[['employee_id', 'bonus']].sort_values(['employee_id'])

