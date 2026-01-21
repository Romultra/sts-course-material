"""
Assignment D - Questions 7, 8, and 9
Generate visualizations for the Energy Islands controversy analysis
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Change to notebook directory for relative paths
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# SETTINGS
settings = {}
settings['statements_dataset'] = '../../data/Actor statement dataset.csv'
settings['year_first'] = 2019
settings['year_last'] = 2025
settings['plot_width'] = 12
settings['plot_height'] = 6

# Load dataset
print("Loading data...")
df = pd.read_csv(settings['statements_dataset'], dtype=str)
df = df.fillna('')

# Set 'Year' column to int
df['Year'] = df['Year'].replace('', pd.NA)
df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype(pd.Int64Dtype())

print(f'Data loaded: {len(df)} statements')

# ============================================================
# QUESTION 7: Statements MENTIONING the Danish Energy Agency
# ============================================================
print("\n" + "="*60)
print("QUESTION 7: Statements MENTIONING the Danish Energy Agency")
print("="*60)

condition_q7 = df['Statement'].str.contains('Energy Agency', case=False, na=False)
title_q7 = "Statements mentioning the Danish Energy Agency"

print(f"Total statements matching: {condition_q7.sum()}")

# Timeline visualization for Q7
df_ = df.copy()
df_['filtered'] = condition_q7

df_ = df_[df_['Year'] >= settings['year_first']]
df_ = df_[df_['Year'] <= settings['year_last']]

df_['Date of publication'] = pd.to_datetime(df_['Date of publication'], format='%Y-%m-%d', errors='coerce')
df_ = df_.dropna(subset=['Date of publication'])

monthly_statements = df_.groupby([pd.Grouper(key='Date of publication', freq='ME'), 'filtered'])['filtered'].count().unstack(fill_value=0)
monthly_statements_percentage = monthly_statements.div(monthly_statements.sum(axis=1), axis=0) * 100

if True in monthly_statements_percentage.columns:
    peak_month = monthly_statements_percentage[True].idxmax()
    peak_value = monthly_statements_percentage[True].max()
    print(f"Peak reached in {peak_month.strftime('%B %Y')} at {peak_value:.1f}%")

plt.figure(figsize=(settings['plot_width'], settings['plot_height']))
plt.xlim(pd.to_datetime(f'{settings["year_first"]-1}-12-01'), pd.to_datetime(f'{settings["year_last"]+1}-01-31'))

try:
    plt.bar(monthly_statements_percentage.index, monthly_statements_percentage[True], width=30, color='#00BBBD')
except:
    pass

if True in monthly_statements_percentage.columns:
    plt.annotate(
        f'Peak: {peak_value:.1f}%\n({peak_month.strftime("%b %Y")})',
        xy=(peak_month, peak_value),
        xytext=(peak_month + pd.DateOffset(months=6), peak_value + 3),
        ha='center', fontsize=9,
        arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
        bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', edgecolor='red', alpha=0.8)
    )

plt.xlabel('Date')
plt.ylabel('Percentage of Statements')
plt.title('Evolution of Statements per Month (Percentage) - ' + title_q7)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

filename = 'Q7_Timeline_Mentions.png'
plt.savefig(filename, dpi=300)
print(f"Figure saved as '{filename}'")
plt.close()

# ============================================================
# QUESTION 8: Statements AUTHORED BY the Danish Energy Agency
# ============================================================
print("\n" + "="*60)
print("QUESTION 8: Statements AUTHORED BY the Danish Energy Agency")
print("="*60)

condition_q8 = (
    (df['Actor'] == 'Danish Energy Agency') |
    (df['Representative of'] == 'The Danish Energy Agency')
)
title_q8 = "Statements authored by the Danish Energy Agency"

print(f"Total statements matching: {condition_q8.sum()}")

df_ = df.copy()
df_['filtered'] = condition_q8

df_ = df_[df_['Year'] >= settings['year_first']]
df_ = df_[df_['Year'] <= settings['year_last']]

df_['Date of publication'] = pd.to_datetime(df_['Date of publication'], format='%Y-%m-%d', errors='coerce')
df_ = df_.dropna(subset=['Date of publication'])

monthly_statements = df_.groupby([pd.Grouper(key='Date of publication', freq='ME'), 'filtered'])['filtered'].count().unstack(fill_value=0)
monthly_statements_percentage = monthly_statements.div(monthly_statements.sum(axis=1), axis=0) * 100

if True in monthly_statements_percentage.columns:
    peak_month = monthly_statements_percentage[True].idxmax()
    peak_value = monthly_statements_percentage[True].max()
    print(f"Peak reached in {peak_month.strftime('%B %Y')} at {peak_value:.1f}%")

plt.figure(figsize=(settings['plot_width'], settings['plot_height']))
plt.xlim(pd.to_datetime(f'{settings["year_first"]-1}-12-01'), pd.to_datetime(f'{settings["year_last"]+1}-01-31'))

try:
    plt.bar(monthly_statements_percentage.index, monthly_statements_percentage[True], width=30, color='#00BBBD')
except:
    pass

if True in monthly_statements_percentage.columns:
    plt.annotate(
        f'Peak: {peak_value:.1f}%\n({peak_month.strftime("%b %Y")})',
        xy=(peak_month, peak_value),
        xytext=(peak_month + pd.DateOffset(months=6), peak_value + 3),
        ha='center', fontsize=9,
        arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
        bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', edgecolor='red', alpha=0.8)
    )

plt.xlabel('Date')
plt.ylabel('Percentage of Statements')
plt.title('Evolution of Statements per Month (Percentage) - ' + title_q8)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

filename = 'Q8_Timeline_Authored.png'
plt.savefig(filename, dpi=300)
print(f"Figure saved as '{filename}'")
plt.close()

# ============================================================
# QUESTION 9: Source Types for Kraka Economics
# ============================================================
print("\n" + "="*60)
print("QUESTION 9: Kraka Economics statements mentioning Energy Agency")
print("="*60)

condition_q9 = (
    (df['Actor'] == 'Kraka Economics') &
    (df['Statement'].str.contains('Energy Agency', case=False, na=False))
)
title_q9 = "Kraka Economics statements mentioning Energy Agency"

print(f"Total statements matching: {condition_q9.sum()}")
print(f"\nSource types breakdown:")
print(df[condition_q9]['Source type'].value_counts())

attribute = 'Source type'

df_ = df.copy()
df_['filtered'] = condition_q9

source_counts = df_[df_['filtered'] == True][attribute].value_counts()

plt.figure(figsize=(settings['plot_width'], settings['plot_height']))

plt.barh(source_counts.index, source_counts.values, color='#00bbbd')

for i, v in enumerate(source_counts.values):
    plt.text(v + 0.1, i, f' {v}', va='center', color='black', fontweight='bold')

plt.xlabel('Count')
plt.ylabel(attribute)
plt.title(f'Distribution by {attribute} - {title_q9}')
plt.gca().invert_yaxis()
plt.tight_layout()

filename = 'Q9_Source_Types.png'
plt.savefig(filename, dpi=300)
print(f"Figure saved as '{filename}'")
plt.close()

print("\n" + "="*60)
print("DONE! All visualizations have been saved.")
print("="*60)
print("\nFiles generated:")
print("- Q7_Timeline_Mentions.png")
print("- Q8_Timeline_Authored.png")
print("- Q9_Source_Types.png")
