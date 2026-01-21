"""
Assignment D: Questions 1, 2, 4, and 5
Energy Supply Security & Expertise Analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set display options
pd.set_option('display.max_colwidth', 150)
pd.set_option('display.max_rows', 100)

# Set plot style
plt.style.use('default')

print("="*70)
print("ASSIGNMENT D: QUESTIONS 1, 2, 4, AND 5")
print("="*70)
print()

# Load dataset
print("Loading dataset...")
df = pd.read_csv('../../data/Actor statement dataset.csv', dtype=str)
df = df.fillna('')

# Convert numeric columns
df['Year'] = df['Year'].replace('', pd.NA)
df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype(pd.Int64Dtype())
df['X'] = pd.to_numeric(df['X'], errors='coerce')
df['Y'] = pd.to_numeric(df['Y'], errors='coerce')
df['Size'] = pd.to_numeric(df['Size'], errors='coerce')

print(f'Dataset loaded: {len(df)} statements')
print()

# ============================================================================
# Q1: Find Alternative Formulations for "Energy Supply Security"
# ============================================================================
print("="*70)
print("Q1: ALTERNATIVE FORMULATIONS FOR 'ENERGY SUPPLY SECURITY'")
print("="*70)
print()

# Search 1: Direct supply security mentions
print("SEARCH 1: Direct 'supply security' mentions")
print("-" * 70)
condition1 = df['Statement'].str.contains(
    'supply security|security of supply',
    case=False, na=False
)
df1 = df[condition1].copy()
print(f'Found {len(df1)} statements')
print("\nSample statements (first 3):")
for i, (idx, row) in enumerate(df1.head(3).iterrows(), 1):
    print(f"\n{i}. [ID: {row['id']}] {row['Actor']}")
    stmt = row['Statement']
    print(f"   {stmt[:250]}..." if len(stmt) > 250 else f"   {stmt}")

# Search 2: Reliability and stability
print("\n" + "="*70)
print("SEARCH 2: Reliability and stability terms")
print("-" * 70)
condition2 = df['Statement'].str.contains(
    'reliable energy|reliable supply|stability|stable energy|stable supply',
    case=False, na=False
)
df2 = df[condition2].copy()
print(f'Found {len(df2)} statements')
print("\nSample statements (first 3):")
for i, (idx, row) in enumerate(df2.head(3).iterrows(), 1):
    print(f"\n{i}. [ID: {row['id']}] {row['Actor']}")
    stmt = row['Statement']
    print(f"   {stmt[:250]}..." if len(stmt) > 250 else f"   {stmt}")

# Search 3: Backup and intermittency
print("\n" + "="*70)
print("SEARCH 3: Backup and intermittency terms")
print("-" * 70)
condition3 = df['Statement'].str.contains(
    'backup|intermittent|fluctuat',
    case=False, na=False
)
df3 = df[condition3].copy()
print(f'Found {len(df3)} statements')
print("\nSample statements (first 3):")
for i, (idx, row) in enumerate(df3.head(3).iterrows(), 1):
    print(f"\n{i}. [ID: {row['id']}] {row['Actor']}")
    stmt = row['Statement']
    print(f"   {stmt[:250]}..." if len(stmt) > 250 else f"   {stmt}")

# Search 4: Issue 5 sample
print("\n" + "="*70)
print("SEARCH 4: Issue 5 ('Will we have a stable energy supply?') samples")
print("-" * 70)
condition_issue5 = df['Issue_5'] == 'TRUE'
df_issue5 = df[condition_issue5].copy()
print(f'Issue 5 contains {len(df_issue5)} statements ({len(df_issue5)/len(df)*100:.1f}%)')
print("\nRandom sample from Issue 5 (5 statements):")
for i, (idx, row) in enumerate(df_issue5.sample(5, random_state=42).iterrows(), 1):
    print(f"\n{i}. [ID: {row['id']}] {row['Actor']}")
    stmt = row['Statement']
    print(f"   {stmt[:250]}..." if len(stmt) > 250 else f"   {stmt}")

# ============================================================================
# Q2: Build Comprehensive Supply Security Query
# ============================================================================
print("\n\n" + "="*70)
print("Q2: COMPREHENSIVE SUPPLY SECURITY QUERY")
print("="*70)
print()

# Build comprehensive query
condition_supply_security = df['Statement'].str.contains(
    'supply security|security of supply|stable energy|energy stability|'
    'reliability|reliable energy|reliable supply|backup power|backup|'
    'resilience|resilient|intermittent|fluctuat|energy storage|'
    'stable supply|energy stability',
    case=False,
    na=False
)

df_supply_security = df[condition_supply_security].copy()
match_count = len(df_supply_security)

print('QUERY RESULTS')
print('-' * 70)
print(f'Total matches: {match_count} statements')
print(f'Percentage of corpus: {match_count/len(df)*100:.1f}%')

# Compare with Issue 5
overlap_with_issue5 = len(df_supply_security[df_supply_security['Issue_5'] == 'TRUE'])
print(f'\nOverlap with Issue 5: {overlap_with_issue5} statements')
print(f'Issue 5 has {len(df_issue5)} statements total')
print(f'Coverage of Issue 5: {overlap_with_issue5/len(df_issue5)*100:.1f}%')

# Distribution by year
print("\nDistribution by year:")
year_counts = df_supply_security['Year'].value_counts().sort_index()
for year, count in year_counts.items():
    print(f'  {year}: {count} statements')

# ============================================================================
# Q4: Identify Clusters for Supply Security
# ============================================================================
print("\n\n" + "="*70)
print("Q4: CLUSTER ANALYSIS FOR SUPPLY SECURITY")
print("="*70)
print()

cluster_counts = df_supply_security['Cluster'].value_counts().sort_values(ascending=False)

print('Statements by cluster:')
print('-' * 70)
for cluster, count in cluster_counts.items():
    percentage = count / len(df_supply_security) * 100
    print(f'Cluster {cluster}: {count} statements ({percentage:.1f}%)')

print('\nTop 3 clusters:')
for i, (cluster, count) in enumerate(cluster_counts.head(3).items(), 1):
    percentage = count / len(df_supply_security) * 100
    print(f'{i}. Cluster {cluster}: {count} statements ({percentage:.1f}%)')

# Sample from top cluster
top_cluster = cluster_counts.index[0]
print(f'\nSample statements from Cluster {top_cluster} (top cluster):')
df_top_cluster = df_supply_security[df_supply_security['Cluster'] == top_cluster]
for i, (idx, row) in enumerate(df_top_cluster.head(3).iterrows(), 1):
    print(f"\n{i}. [ID: {row['id']}] {row['Actor']}")
    stmt = row['Statement']
    print(f"   {stmt[:250]}..." if len(stmt) > 250 else f"   {stmt}")

# ============================================================================
# Q5: Combined Query (Supply Security + Expertise)
# ============================================================================
print("\n\n" + "="*70)
print("Q5: COMBINED QUERY (Supply Security + Expertise)")
print("="*70)
print()

# Build expertise query
condition_expertise = df['Statement'].str.contains(
    'expert|expertise|analysis|analyze|recommend|recommendation|report|study|research|'
    'scientist|professor|consultant|analyst|assessment|evaluate|evaluation|'
    'agency|authority|institute|university|model|forecast|predict|estimate',
    case=False,
    na=False
)

print(f'Statements mentioning expertise: {condition_expertise.sum()}')
print(f'Statements about supply security: {condition_supply_security.sum()}')

# Combine with AND
condition_combined = condition_supply_security & condition_expertise
df_combined = df[condition_combined].copy()
match_count_combined = len(df_combined)

print()
print('COMBINED QUERY RESULTS')
print('-' * 70)
print(f'Total matches: {match_count_combined} statements')
if match_count_combined >= 15:
    print(f'Requirement (>=15): MET')
else:
    print(f'Requirement (>=15): NOT MET')
print()

# Display all matching statements
print('ALL MATCHING STATEMENTS:')
print('-' * 70)
for i, (idx, row) in enumerate(df_combined.iterrows(), 1):
    print(f'\n{i}. [ID: {row["id"]}] {row["Actor"]}')
    if row['Representative of']:
        print(f'   Representative of: {row["Representative of"]}')
    print(f'   Source: {row["Source name"]} ({row["Date of publication"]})')
    print(f'   Cluster: {row["Cluster"]}')
    stmt = row['Statement']
    if len(stmt) > 300:
        print(f'   Statement: {stmt[:300]}...')
    else:
        print(f'   Statement: {stmt}')

# Top actors
print('\n' + '-' * 70)
print('Top actors in combined query:')
actor_counts = df_combined['Actor'].value_counts().head(10)
for actor, count in actor_counts.items():
    print(f'  {actor}: {count} statements')

# Distribution by cluster
print('\nDistribution by cluster:')
cluster_combined = df_combined['Cluster'].value_counts().sort_values(ascending=False)
for cluster, count in cluster_combined.items():
    print(f'  Cluster {cluster}: {count} statements')

# Distribution by year
print('\nDistribution by year:')
year_combined = df_combined['Year'].value_counts().sort_index()
for year, count in year_combined.items():
    print(f'  {year}: {count} statements')

print("\n" + "="*70)
print("ANALYSIS COMPLETE")
print("="*70)
