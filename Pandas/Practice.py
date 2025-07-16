import pandas as pd

# data = {
#     "product":["soap","shampoo","toothpaste","brush"],
#     "unit_sold":[10,5,8,12],
#     "price_per_unit":[20,120,45,20]
# }

# df = pd.DataFrame(data)
# df["Total_sale"] = df["unit_sold"] * df["price_per_unit"]

# grouped = df.groupby("product")["Total_sale"].sum().reset_index()

# max_sale_product = grouped.loc[grouped["Total_sale"].idxmax()]

# total_revenue = df["Total_sale"].sum()

# unique_product = df['product'].nunique()

# print("Sales summary by product:/n",grouped)

# print("\nProduct with height sales:\n",max_sale_product)

# print("\nTotal Revenue:",total_revenue)

# print("\nNumber od unique product:",unique_product)

Std_data = [
    ( 1 , "Varun" , 30 , "Male" , "Chandigrah"),
    ( 2 , "Ravi" , 31 , "Male" , "Delhi"),
    ( 3 , "preeti" , 29 , "Female" , "Jaipur"),
    ( 4 , "Amit" , 32 , "Male" , "Mumbai"),
    ( 5 , "Angel" , 28 , "Female" , "Banglore")
]
df = pd.DataFrame(Std_data , columns= ["stud_id","Name","Age","Gender","Location"])
print(df)     #    Print Table

print(df.head(2))      #   print top position
print(df.tail(1))      #   Print bottom position
print(df.shape)        #   Count how many no. of rows and column
print(df.columns)      #   print Columns name    ex.  name age nd all
print(df[["Age","Location"]])          #   print all values in age and location
print(df.size)         #   count how many values
print(df.dtypes)       #   data types in every values
# print(df.values)       #   
print(df.index)        #   Count how many rows 

print(df.loc[0])         #   Only 1st row are printed

print(df[df["Age"] > 29])

df.insert(3 , "phone_no" , [10,20,30,40,50])     #   insert phone no. column
print(df)

df = df.drop(columns= ["phone_no"])          #   Delete Column in phone no
print(df)

df = df.rename(columns= {"Age" : "Stud_age"})      # name change age to stud_name 
print(df)

df = df.drop(4)          #  drop 4th row for ex. Angle name is delete
print(df)
 
df.loc[4] = [ 5 , "Angel" , 28 , "Female" , "Banglore"]     #   Adding row
print(df)

df.loc[[ 0 , 2], "Location"] = ["Andaman" , "Nicobar"]       #    Update the values
print(df)