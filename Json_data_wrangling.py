import json
import pandas as pd
from pandas.io.json import json_normalize
# define json string
data = [{'state': 'Florida',
         'shortname': 'FL',
         'info': {'governor': 'Rick Scott'},
         'counties': [{'name': 'Dade', 'population': 12345},
                      {'name': 'Broward', 'population': 40000},
                      {'name': 'Palm Beach', 'population': 60000}]},
        {'state': 'Ohio',
         'shortname': 'OH',
         'info': {'governor': 'John Kasich'},
         'counties': [{'name': 'Summit', 'population': 1234},
                      {'name': 'Cuyahoga', 'population': 1337}]}]

# use normalization to create tables from nested element
print(json_normalize(data, 'counties'))

# further populate tables created from nested element
print(json_normalize(data, 'counties', ['state', 'shortname', ['info', 'governor']]))

# load json as string
#json.load((open(r'https://raw.githubusercontent.com/springboard-curriculum/mec-mini-projects/master/mec-5.4.4-json-data-wrangling-mini-project/data/world_bank_projects_less.json')))

# load as Pandas dataframe
sample_json_df = pd.read_json(r'https://raw.githubusercontent.com/springboard-curriculum/mec-mini-projects/master/mec-5.4.4-json-data-wrangling-mini-project/data/world_bank_projects_less.json')
print(sample_json_df.head(10))
print(sample_json_df.info())
print(sample_json_df.describe())
print(sample_json_df.describe(include='O'))

# JSON exercise
#
# Using data in file 'data/world_bank_projects.json' and the techniques demonstrated above,
#     Find the 10 countries with most projects

#     In 2. above you will notice that some entries have only the code and the name is missing. Create a dataframe with the missing names filled in.

countries_with_most_projects = sample_json_df['countryshortname'].value_counts(sort=True, ascending=False)[:10]
print("Countries with most projects\n", countries_with_most_projects)

#     Find the top 10 major project themes (using column 'mjtheme_namecode')
top_10_major_project_themes = sample_json_df['mjtheme_namecode'].value_counts(sort=True,ascending=False)[:10]

# I#2. above you will notice that some entries have only the code and the name is missing.
# Create a dataframe with the missing names filled in.
countries_with_code_and_name_missing = sample_json_df.fillna( method='ffill', axis=1, inplace=False)
print(countries_with_code_and_name_missing.info())