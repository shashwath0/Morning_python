# import numpy as np
# arr1= np.array([[1,2],[3,4]])
# arr2= np.array([[1,2],[3,4]])
# res1= np.matmul(arr1,arr2)
# res2= arr1 * arr2
# print(res1)
# print(res2)

# import numpy as np
# arr1= np.array([[1,2,3],[4,5,6]])
# arr2= np.array([[1,2],[3,4],[5,6]])
# res1= np.matmul(arr1,arr2)
# print(res1)

# import numpy as np
# arr1=np.array([[1,2],[4,5]])
#
# res1=np.invert(arr1)
# print(res1)

# import numpy as np
# arr1=np.array([[1,2],[3,4]])
# arr2=np.transpose([[1,2],[3,4]])
# res1=np.invert(arr1)
# print(res1)

# import numpy as np
# arr = np.arange(10)
# print(arr)

# import numpy as np
# arr=np.arange(12)
# reshaped_arr=np.reshape(arr,(4,3))
# print(reshaped_arr)

# import numpy as np
# arr=np.array([[1,2,3],
#              [4,5,6]])
# row_mean=np.mean(arr,axis=0)
# col_mean=np.mean(arr,axis=1)
# print(row_mean)
# print(col_mean)

# import numpy as np
# arr=np.array([[1,2,3],
#               [4,5,6]])
# col_sum=np.sum(arr,axis=1)
# print(col_sum)

# import numpy as np
# arr=np.array([[1,2,3],
#               [4,5,6]])
# row_sum=np.sum(arr,axis=0)
# print(row_sum)

# import numpy as np
# rand_arr=np.random.rand(3)
# print(rand_arr)

# import pandas as pd
# data={
#     'Name': ['Alice','bob','Charlie'],
#     'Age': [25,23,21],
#     'City':['Border land','los angles','USA']
# }
# df=pd.DataFrame(data)
# print(df)
# df.to_csv('Employee.csv',index=False)
# df.to_json('Employee.json',orient='records')





# import pandas as pd
# data={
#     'emp_id': [1,2,3],
#     'emp_name': ['Bob','Rick','James'],
#     'emp_salary':[1500,2000,1800]
# }
# df=pd.DataFrame(data)
# print(df)
# df.to_csv('Emp.csv',index=False)
# df.to_json('Emp.json',orient='records')
# df_csv=pd.read_csv('Emp.csv')
# print(df_csv)
# df_json=pd.read_json('Emp.json')
# print(df_json)



# import pandas as pd
# data={
#     'Name': ['Alice','Bob','Charlie'],
#     'Age': [25,23,21],
#     'City':['Border land','los angles','USA']
# }
# df=pd.DataFrame(data)
# print(df)
# df.to_csv('Employee.csv',index=False)
# df.to_json('Employee.json',orient='records')
# new_data=pd.DataFrame([{'Name':'David','Age':25,'City':'San Francisco'}])
# df_csv=pd.read_csv('Employee.csv')
# df_csv=pd.concat([df_csv,new_data],ignore_index=True)
# df_csv.to_csv('Employee.csv',index=False)
# new_data_json=pd.DataFrame([{'Name':'David','Age':25,'City':'San Francisco'}])
# df_json=pd.read_json('Employee.json')
# df_json=pd.concat([df_json,new_data_json],ignore_index=True)
# df_json.to_json('Employee.json',orient='records')
# df_csv=pd.read_csv('Employee.csv')
# df_csv=df_csv[df_csv['Name']!='Bob']
# df_csv.to_csv('Employee.csv',index=False)
# df_json=pd.read_json('Employee.json')
# df_json=df_json[df_json['Name']!='Bob']
# df_json.to_json('Employee.json',orient='records')


# import pandas as pd
# data={
#     'Book_id':[123,456,789],
#     'Book_name':['Life','Death','Car'],
#     'Author':['asdf','fghj','zxcv'],
#     'Price':[1000,1500,2000]
# }
# df=pd.DataFrame(data)
# print(df)
# df.to_csv('books.csv',index=False)
# new_data=pd.DataFrame([{'Book_id':798,'Book_name':'Bike','Author':'lkjh','Price':5000}])
# df_csv=pd.read_csv('books.csv')
# df_csv=pd.concat([df_csv,new_data],ignore_index=True)
# df_csv.to_csv('books.csv',index=False)
# df_csv=pd.read_csv('books.csv')
# df_csv=df_csv[df_csv['Author']!='fghj']
# df_csv.to_csv('books.csv',index=False)


# import pandas as pd
# data={
#     'Book_id':[123,456,789],
#     'Book_name':['Life','Death','Car'],
#     'Author':['asdf','fghj','zxcv'],
#     'Price':[1000,1500,2000]
# }
# df=pd.DataFrame(data)
# print(df)
# df.to_json('books.json',orient='records')
# new_data_json=pd.DataFrame([{'Book_id':798,'Book_name':'Bike','Author':'lkjh','Price':5000}])
# df_json=pd.read_json('books.json')
# df_json=pd.concat([df_json,new_data_json],ignore_index=True)
# df_json.to_json('books.json',orient='records')
# df_json=pd.read_json('books.json')
# df_json=df_json[df_json['Author']!='fghj']
# df_json.to_json('books.json',orient='records')

# import pandas as pd
# import numpy as np
#
# data={
#     'Age':[25,30,np.nan,35,np.nan],
#     'Salary':[5000,5600,6400,np.nan,62000],
#     'Gender':['Male','Female',np.nan,'Female','Male'],
#     'Department':['HR',np.nan,'IT','Finance','IT'],
# }
# df=pd.DataFrame(data)
# print(df)
# print("\nCount of Missing Values in each column:\n",
# df.isnull().sum())
#
# df_dropped=df.dropna()
# print("\n")
# print("\nDataFrame sfter dropping rows with missing values:\n",df_dropped)
#
# # fill with mean
#
# df['Age'].fillna(df['Age'].mean(),inplace=True)
# print("\nDataFrame after Filling 'Age' with Mean:\n",df)