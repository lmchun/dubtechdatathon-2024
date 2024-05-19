# GOAL: Are there are any specific demographic groups (gender/sex/age) that are most affected by specific types of drug overdoses?
import pandas as pd

df = pd.read_csv("Drug_overdose_death_rates__by_drug_type__sex__age__race__and_Hispanic_origin__United_States_20240518.csv")
# print(df)
# untouched
total_df = df.loc[df["STUB_NAME"]== "Total"]

total_df_adjusted = df.loc[
    (df['STUB_NAME'] == 'Total') & 
    (df['UNIT'] == 'Deaths per 100,000 resident population, age-adjusted') &
    (df['PANEL'] != 'All drug overdose deaths')
]
# -------------------------------
filtered_heroin_df = df.loc[
    (df['PANEL'] == 'Drug overdose deaths involving heroin') & 
    (df['UNIT'] == 'Deaths per 100,000 resident population, age-adjusted')
]
filtered_methadone_df = df.loc[
    (df['PANEL'] == 'Drug overdose deaths involving methadone') & 
    (df['UNIT'] == 'Deaths per 100,000 resident population, age-adjusted')
]
filtered_anyopioid_df = df.loc[
    (df['PANEL'] == 'Drug overdose deaths involving any opioid') & 
    (df['UNIT'] == 'Deaths per 100,000 resident population, age-adjusted')
]
filtered_nat_syn_opi_df = df.loc[
    (df['PANEL'] == 'Drug overdose deaths involving natural and semisynthetic opioids') & 
    (df['UNIT'] == 'Deaths per 100,000 resident population, age-adjusted')
]
filtered_syn_non_meth_opi_df = df.loc[
    (df['PANEL'] == 'Drug overdose deaths involving other synthetic opioids (other than methadone)') & 
    (df['UNIT'] == 'Deaths per 100,000 resident population, age-adjusted')
]
# ----------------------------
# compare certain demographics to the total

fr_ml_hn_df = filtered_heroin_df.loc[
 (filtered_heroin_df['STUB_NAME'] == 'Sex') & 
    (filtered_heroin_df['STUB_LABEL'] == 'Male')
]
# mean_fr_ml_hn = fr_ml_hn_df['ESTIMATE'].mean()

fr_fml_hn_df = filtered_heroin_df.loc[
 (filtered_heroin_df['STUB_NAME'] == 'Sex') & 
    (filtered_heroin_df['STUB_LABEL'] == 'Female')
]
# mean_fr_fml_hn = fr_fml_hn_df['ESTIMATE'].mean()

tot_hn_df= filtered_heroin_df.loc[ (filtered_heroin_df['STUB_NAME'] == 'Total')
]

# mean_total_hn = tot_hn_df['ESTIMATE'].mean()

