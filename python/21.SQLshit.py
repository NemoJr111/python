import re
def write_employee_info(myfile):
    with open(myfile, 'w') as file:
        file.write("EmpID, Name, Dept, Salary\n")
        file.write("101, John, DemoDept, 50000\n")
        file.write("102, Alice, HR, 60000\n")
        file.write("103, Bob, IT, 55000")

def retrieve_employee_info(myfile):
    empid_pattern = r'(\d+)'
    salary_pattern = r'(\d+)$'
    with open(myfile, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            match_empid = re.search(empid_pattern, line)
            match_salary = re.search(salary_pattern, line)
            if match_empid and match_salary:
                empid = match_empid.group(1)
                salary = match_salary.group(1)
                print(f'Employee ID: {empid}, Salary: {salary}')

myfile = 'employee_info.csv'
write_employee_info(myfile)
retrieve_employee_info(myfile)