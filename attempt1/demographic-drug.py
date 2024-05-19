# GOAL: Are there are any specific demographic groups (gender/sex/age) that are most affected by specific types of drug overdoses?
import pandas as pd

df = pd.read_csv("Drug_overdose_death_rates__by_drug_type__sex__age__race__and_Hispanic_origin__United_States_20240518.csv")
print(df)

stubname_level = df.groupby("STUB_NAME",level=None)
help(stubname_level).agg

# storing the filtered results into variables that show the filtered view of the data that has certain types
total_df = df.loc[df["STUB_NAME"]== "Total"]
# sexrace_df = df.loc[df["STUB_NAME"]== "Age"]
# this does not work because it does not include the rest of the string of and ____
df=df.loc[df["STUB_NAME"]!= "Total"]

df_c = pd.merge(df, total_df,
         how='left',
        on=["PANEL_NUM", "STUB_NAME_NUM", "YEAR_NUM"])


# to delete a variable
# del sex_df



# take stubname and filter all the ones that say 
# Total, Sex, Age, Hispanic origin (single race), race
# and make them all different columns in the table


# what do i need to do after?
# split the strings that have AND in the values


# THEN filter out the death rates
# THEN filter out drug overdose types

# THEN COMPARE THEM to find the information 