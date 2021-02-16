import pandas as pd
emp_details = {'Employee':{'Dave':{'ID':'001','Salary':'2000','Designation':'Team Lead'},'Ava':{'ID':'002','Salary':'1000','Designation':'Associate'}}}
df = pd.DataFrame(emp_details['Employee'])
print(df)