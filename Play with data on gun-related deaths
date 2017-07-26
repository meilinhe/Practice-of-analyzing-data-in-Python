
# coding: utf-8

# In[1]:

import csv

f = open("guns.csv", "r")
guns = csv.reader(f)
data = list(guns)
print(data[0:5])


# In[2]:

headers = data[0]
data = data[1:]
print(headers)
print(data[0:5])


# In[3]:

year_counts = {}
for row in data:
    years = row[1]
    if years in year_counts:
        year_counts[years] += 1
    else:
        year_counts[years] = 1
print(year_counts)


# In[4]:

import datetime
dates = []
for row in data:
    date = datetime.datetime(year = int(row[1]), month = int(row[2]), day = 1)
    dates.append(date)
print(dates[0:5])

date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
print(date_counts)


# In[5]:

sex_counts = {}
for row in data:
    sex = row[5]
    if sex in sex_counts:
        sex_counts[sex] += 1
    else:
        sex_counts[sex] = 1
print(sex_counts)

race_counts = {}
for row in data:
    race = row[7]
    if race in race_counts:
        race_counts[race] += 1
    else:
        race_counts[race] = 1
print(race_counts)


# In[8]:

import csv
census = list(csv.reader(open("census.csv", "r")))
print(census)


# In[25]:

mapping = {}
mapping["Asian/Pacific Islander"] = int(census[1][14]) + int(census[1][15])
mapping["Black"] = int(census[1][12])
mapping["Hispanic"] = int(census[1][11])
mapping["Native American/Native Alaskan"] = int(census[1][13])
mapping["White"] = int(census[1][10])
print(mapping)

race_per_lundredk = {}
for key in race_counts:
    race_per_lundredk[key] = (race_counts[key]/mapping[key]) * 100000
print(race_per_lundredk)


# In[31]:

#create homicide_race list
intents = []
for row in data:
    intents.append(row[3])

races = []
for row in data:
    races.append(row[7])

homicide_race = {}
for i, race in enumerate(races):
    if intents[i] == "Homicide":
        if race not in homicide_race:
            homicide_race[race] = 1
        else:
            homicide_race[race] += 1

print(homicide_race)

#calculate rate
homicide_race_per_hundredk = {}
for key in homicide_race:
    homicide_race_per_hundredk[key] = (homicide_race[key]/mapping[key]) * 100000
print(homicide_race_per_hundredk)


# In[33]:

#I don't know how to use markdown
#totally forgot


# I've _finally_ remember **how to** use
# ### Markdown !
