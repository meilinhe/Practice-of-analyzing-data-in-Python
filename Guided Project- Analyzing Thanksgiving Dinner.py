
# coding: utf-8

# In[1]:

#Import data
import pandas as pd
data = pd.read_csv('thanksgiving.csv', encoding="Latin-1")
print(data.head())


# In[2]:

indexes = data.columns


# In[3]:

#Filtering Out Rows From A DataFrame

celeb_counts = data["Do you celebrate Thanksgiving?"].value_counts()
print(celeb_counts)
data_celeb = data[data["Do you celebrate Thanksgiving?"] == "Yes"]


#Using Value_counts To Explore Main Dishes

dish_counts = data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
data_Tofurkey = data[data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"]
Tofurkey_gravy = data_Tofurkey["Do you typically have gravy?"]
print(Tofurkey_gravy)


#Figuring Out How Many People Eat pies

apple_isnull = pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])
pumpkin_isnull = pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"])
pecan_isnull = pd.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"])
ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull
pies_count = ate_pies.value_counts()


# In[4]:

#Converting Age To Numeric
def age_convert(age_data):
    if pd.isnull(age_data) == True:
        return None
    else:
        age_list = age_data.split(" ")
        age = age_list[0].replace("+", "")
        age = int(age)
        return age
    
data["int_age"] = data["Age"].apply(age_convert)
print(data["int_age"].describe())


# It is **not** correct to count the first element in the range of age __only__

# In[5]:

#Converting Income To Numeric

import string

a_z = list(string.ascii_lowercase)
A_Z = list(string.ascii_uppercase)
chars = a_z + A_Z + ["$"] + [","]

def income_convert(income_data):
    if pd.isnull(income_data) == True:
        return None
    else:
        income_list = income_data.split(" ")
        income = income_list[0]
        if income == "Prefer":
            return None
        else:
            for ch in chars:
                income = income.replace(ch, "")
            income = int(income)
            return income
    print(income)
    
data["int_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(income_convert)
print(data["int_income"])

print(data["int_income"].describe())


# In[8]:

#Correlating Travel Distance And Income
##low income individuals
low_income_rows = data[data["int_income"] < 150000]
low_income_travel = low_income_rows["How far will you travel for Thanksgiving?"]
print(low_income_travel.value_counts())

##high income individuals
high_income_rows = data[data["int_income"] > 150000]
high_income_travel = high_income_rows["How far will you travel for Thanksgiving?"]
print(high_income_travel.value_counts())


# It's **hard** to determine wether the individuals with higher income would more likely to spend thanksgiving at their own house or not _only_ based on these results. Maybe we should **normalize** the results.

# In[20]:

#Linking Friendship And Age or income
import numpy
v_age = "int_age"
v_income = "int_income"
columns = ['Have you ever attended a "Friendsgiving?"']
index = ["Have you ever tried to meet up with hometown friends on Thanksgiving night?"]
friendship = pd.pivot_table(data, values = v_age, index = index, columns = columns)
friendship_avg = pd.pivot_table(data, values =v_income, index = index, columns = columns, aggfunc = numpy.mean)
print(friendship)
print(friendship_avg)


# In[21]:

#Figure out the most common dessert people eat
dessert_options = ["Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Apple cobbler", "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Blondies", "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Brownies", "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Carrot cake", "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cheesecake", "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cookies", "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Fudge", "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Ice cream", "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Peach cobbler", "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - None", "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Other (please specify)", "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Other (please specify) - specify"]
desserts_counts = {}
for option in dessert_options:
    option_isnull = pd.isnull(data[option])
    data_dessert_option_not_null = data[option_isnull == False]
    dessert_option_not_null = data_dessert_option_not_null[option]
    option_counts = dessert_option_not_null.value_counts()
    desserts_counts[option] = option_counts
print(desserts_counts)
most_common_dessert = max(desserts_counts, key=desserts_counts.get)



# In[22]:

#Figure out the most common complete meal people eat


# In[23]:

#Identify how many people work on Thanksgiving


# In[24]:

#Find regional patterns in the dinner menus


# In[ ]:

#Find age, gender, and income based patterns in dinner menus

