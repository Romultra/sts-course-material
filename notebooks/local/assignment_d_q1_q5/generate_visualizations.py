"""
Generate visualizations for Assignment D Questions 2, 4, and 5
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Use non-interactive backend
matplotlib.use('Agg')

# Set style
plt.style.use('default')
plt.rcParams['figure.dpi'] = 300  # High resolution for screenshots
plt.rcParams['font.size'] = 10

print("Loading dataset...")
df = pd.read_csv('../../data/Actor statement dataset.csv', dtype=str)
df = df.fillna('')

# Convert numeric columns
df['Year'] = df['Year'].replace('', pd.NA)
df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype(pd.Int64Dtype())

print(f"Dataset loaded: {len(df)} statements")

# ============================================================================
# Q2: Supply Security Query Results
# ============================================================================
print("\nGenerating Q2 visualization...")

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

# Create figure with query results
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Top panel: Query match count display
ax1.axis('off')
query_text = """QUERY:
df['Statement'].str.contains(
    'supply security|security of supply|stable energy|energy stability|
    reliability|reliable energy|reliable supply|backup power|backup|
    resilience|resilient|intermittent|fluctuat|energy storage|
    stable supply|energy stability',
    case=False, na=False
)"""

results_text = f"""
RESULTS:
Total matches: {match_count} statements
Percentage of corpus: {match_count/len(df)*100:.1f}%
"""

ax1.text(0.05, 0.95, 'Q2: Supply Security Query',
         fontsize=16, fontweight='bold', va='top', transform=ax1.transAxes)
ax1.text(0.05, 0.80, query_text,
         fontsize=9, family='monospace', va='top', transform=ax1.transAxes,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
ax1.text(0.05, 0.35, results_text,
         fontsize=12, fontweight='bold', va='top', transform=ax1.transAxes,
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))

# Bottom panel: Timeline visualization
year_counts = df_supply_security['Year'].value_counts().sort_index()
bars = ax2.bar(year_counts.index, year_counts.values, color='steelblue', alpha=0.7, edgecolor='navy')
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Number of Statements', fontsize=12, fontweight='bold')
ax2.set_title('Supply Security Statements Over Time', fontsize=13, fontweight='bold', pad=15)
ax2.grid(axis='y', alpha=0.3, linestyle='--')
ax2.set_axisbelow(True)

# Highlight peak year
peak_year = year_counts.idxmax()
peak_idx = list(year_counts.index).index(peak_year)
bars[peak_idx].set_color('darkred')
bars[peak_idx].set_alpha(0.8)

plt.tight_layout()
plt.savefig('Q2_Supply_Security_Query.png', dpi=300, bbox_inches='tight')
print(f"Saved: Q2_Supply_Security_Query.png")
plt.close()

# ============================================================================
# Q4: Cluster Analysis
# ============================================================================
print("\nGenerating Q4 visualization...")

import textwrap

cluster_counts = df_supply_security['Cluster'].value_counts().sort_values(ascending=True)

# Create figure
fig, ax = plt.subplots(figsize=(14, 8))

# Create horizontal bar chart
bars = ax.barh(range(len(cluster_counts)), cluster_counts.values,
               color='teal', alpha=0.7, edgecolor='darkslategray', linewidth=1.5)

# Highlight top 3 clusters
top3_colors = ['#c7522a', '#e5c185', '#74a892']
for i in range(min(3, len(bars))):
    bars[-(i+1)].set_color(top3_colors[i])
    bars[-(i+1)].set_alpha(0.8)

# Word wrap cluster names for better readability
def wrap_label(label, width=30):
    if label == '(None)':
        return 'No specific cluster'
    return '\n'.join(textwrap.wrap(label, width=width))

wrapped_labels = [wrap_label(c) for c in cluster_counts.index]

ax.set_yticks(range(len(cluster_counts)))
ax.set_yticklabels(wrapped_labels, fontsize=9)
ax.set_xlabel('Number of Statements', fontsize=12, fontweight='bold')
ax.set_title('Q4: Supply Security Statements by Semantic Cluster',
             fontsize=14, fontweight='bold', pad=20)
ax.grid(axis='x', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

# Add counts on bars
max_count = cluster_counts.max()
for i, (bar, count) in enumerate(zip(bars, cluster_counts.values)):
    percentage = count / len(df_supply_security) * 100
    ax.text(count + 2, i, f'{count} ({percentage:.1f}%)',
            va='center', fontsize=9, fontweight='bold')

# Extend x-axis to ensure labels don't spill outside
ax.set_xlim(0, max_count * 1.15)  # Add 15% padding on the right

# Add summary text
summary_text = f"""Total supply security statements: {len(df_supply_security)}
Top cluster: {cluster_counts.index[-1]} ({cluster_counts.iloc[-1]} statements, {cluster_counts.iloc[-1]/len(df_supply_security)*100:.1f}%)"""
ax.text(0.98, 0.02, summary_text, transform=ax.transAxes,
        fontsize=10, va='bottom', ha='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

plt.tight_layout()
plt.savefig('Q4_Cluster_Distribution.png', dpi=300, bbox_inches='tight')
print(f"Saved: Q4_Cluster_Distribution.png")
plt.close()

# ============================================================================
# Q5: Combined Query (Supply Security + Expertise)
# ============================================================================
print("\nGenerating Q5 visualization...")

condition_expertise = df['Statement'].str.contains(
    'expert|expertise|analysis|analyze|recommend|recommendation|report|study|research|'
    'scientist|professor|consultant|analyst|assessment|evaluate|evaluation|'
    'agency|authority|institute|university|model|forecast|predict|estimate',
    case=False,
    na=False
)

condition_combined = condition_supply_security & condition_expertise
df_combined = df[condition_combined].copy()
match_count_combined = len(df_combined)

# Create figure with query and results
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(3, 2, height_ratios=[1.5, 1, 1], hspace=0.4, wspace=0.3)

# Top panel: Query display (spans both columns)
ax_query = fig.add_subplot(gs[0, :])
ax_query.axis('off')

query_text1 = """SUPPLY SECURITY COMPONENT:
df['Statement'].str.contains(
    'supply security|security of supply|stable energy|reliability|...',
    case=False, na=False
)"""

query_text2 = """EXPERTISE COMPONENT:
df['Statement'].str.contains(
    'expert|expertise|analysis|recommend|report|study|research|
    scientist|professor|consultant|analyst|assessment|...',
    case=False, na=False
)"""

combined_text = """COMBINED (AND operator):
condition_combined = condition_supply_security & condition_expertise"""

ax_query.text(0.02, 0.95, 'Q5: Combined Query (Supply Security + Expertise)',
              fontsize=16, fontweight='bold', va='top')
ax_query.text(0.02, 0.75, query_text1, fontsize=8, family='monospace', va='top',
              bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))
ax_query.text(0.52, 0.75, query_text2, fontsize=8, family='monospace', va='top',
              bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))
ax_query.text(0.02, 0.35, combined_text, fontsize=9, family='monospace', va='top',
              bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

results_text = f"""RESULTS:
Total matches: {match_count_combined} statements
Requirement (≥15): {'✓ MET' if match_count_combined >= 15 else '✗ NOT MET'}
Exceeded by: {match_count_combined - 15} statements"""

ax_query.text(0.02, 0.08, results_text, fontsize=13, fontweight='bold', va='top',
              bbox=dict(boxstyle='round', facecolor='lightgreen' if match_count_combined >= 15 else 'lightcoral', alpha=0.5))

# Bottom left: By cluster
ax_cluster = fig.add_subplot(gs[1, 0])
cluster_combined = df_combined['Cluster'].value_counts().sort_values(ascending=True).head(8)
bars_cluster = ax_cluster.barh(range(len(cluster_combined)), cluster_combined.values,
                                color='darkgreen', alpha=0.6, edgecolor='darkgreen', linewidth=1.2)
ax_cluster.set_yticks(range(len(cluster_combined)))
ax_cluster.set_yticklabels([f'{c}' if c != '(None)' else 'No specific cluster' for c in cluster_combined.index],
                            fontsize=9)
ax_cluster.set_xlabel('Number of Statements', fontsize=10, fontweight='bold')
ax_cluster.set_title('Distribution by Cluster (Top 8)', fontsize=11, fontweight='bold')
ax_cluster.grid(axis='x', alpha=0.3, linestyle='--')

for i, count in enumerate(cluster_combined.values):
    ax_cluster.text(count + 0.5, i, str(count), va='center', fontsize=9, fontweight='bold')

# Bottom right: By year
ax_year = fig.add_subplot(gs[1, 1])
year_combined = df_combined['Year'].value_counts().sort_index()
bars_year = ax_year.bar(year_combined.index, year_combined.values,
                        color='darkgreen', alpha=0.6, edgecolor='darkgreen', linewidth=1.2)
ax_year.set_xlabel('Year', fontsize=10, fontweight='bold')
ax_year.set_ylabel('Number of Statements', fontsize=10, fontweight='bold')
ax_year.set_title('Distribution by Year', fontsize=11, fontweight='bold')
ax_year.grid(axis='y', alpha=0.3, linestyle='--')
plt.setp(ax_year.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Third row: Top actors
ax_actors = fig.add_subplot(gs[2, :])
actor_counts = df_combined['Actor'].value_counts().head(10).sort_values(ascending=True)
bars_actors = ax_actors.barh(range(len(actor_counts)), actor_counts.values,
                              color='navy', alpha=0.6, edgecolor='navy', linewidth=1.2)
ax_actors.set_yticks(range(len(actor_counts)))
ax_actors.set_yticklabels(actor_counts.index, fontsize=9)
ax_actors.set_xlabel('Number of Statements', fontsize=10, fontweight='bold')
ax_actors.set_title('Top 10 Actors (Experts Discussing Supply Security)', fontsize=11, fontweight='bold')
ax_actors.grid(axis='x', alpha=0.3, linestyle='--')

for i, count in enumerate(actor_counts.values):
    ax_actors.text(count + 0.2, i, str(count), va='center', fontsize=9, fontweight='bold')

plt.savefig('Q5_Combined_Query.png', dpi=300, bbox_inches='tight')
print(f"Saved: Q5_Combined_Query.png")
plt.close()

print("\n" + "="*70)
print("All visualizations generated successfully!")
print("="*70)
print("\nGenerated files:")
print("1. Q2_Supply_Security_Query.png")
print("2. Q4_Cluster_Distribution.png")
print("3. Q5_Combined_Query.png")
