# GOAL: Are there are any specific demographic groups (gender/sex/age) that are most affected by specific types of drug overdoses?
import pandas as pd

df = pd.read_csv("Drug_overdose_death_rates__by_drug_type__sex__age__race__and_Hispanic_origin__United_States_20240518.csv")
# print(df)
# untouched
total_df = df.loc[df["STUB_NAME"]== "Total"]
total_df= total_df[["INDICATOR", "PANEL_NUM", "UNIT_NUM", "YEAR_NUM", "AGE_NUM","ESTIMATE"]]
total_df = total_df.rename(columns={'ESTIMATE':"TOTAL_ESTIMATE"})

df = df.loc[df["STUB_NAME"]!= "Total"]
df2= pd.merge(df,total_df, on=["INDICATOR", "PANEL_NUM", "UNIT_NUM", "YEAR_NUM", "AGE_NUM"], how="inner")
print(df2.columns)

df2.to_csv("cleaned_drug_data.csv")