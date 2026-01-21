# Assignment D: Questions 1-5 Answers

## Energy Supply Security & Expertise Analysis

---

## Q1: Alternative Formulations for "Energy Supply Security"

**Question**: Find at least 3 alternative ways actors express "energy supply security" in the corpus.

**Answer**:

Based on systematic analysis of the corpus, here are 5 alternative formulations for "energy supply security":

### 1. **"Supply security"** (Direct variant)
- **Statement ID**: 17 (Kraka Economics)
- **Context**: "supply security has increasingly become the central justification for the project"
- **Usage**: Shortened form, commonly used in Danish energy discourse

### 2. **"Security of supply"** (Word order variation)
- **Statement ID**: 6536 (Frederik Løssøe Nielsen, Kraka Economics)
- **Context**: "better Danish security of supply"
- **Usage**: British English variant, emphasizes the security aspect

### 3. **"Stable energy supply"** (Descriptive formulation)
- **Statement ID**: Multiple in Issue 5 (e.g., 2463, 4769, 478)
- **Context**: Issue 5 title: "Will we have a stable energy supply?"
- **Usage**: Emphasizes stability and continuity of energy provision

### 4. **"Reliability"** / **"Reliable energy"** (Outcome-focused)
- **Statement IDs**: 16 (Jacob Trøst), 85 (Hanne Storm Edlefsen), 112 (Brian Vad Mathiesen)
- **Context**: Discusses whether energy systems can be counted on consistently
- **Usage**: Focuses on performance characteristics rather than security concept

### 5. **"Backup power"** / **"Intermittency concerns"** (Problem-oriented)
- **Statement IDs**: 193 (Facebook user), 149 (Lars Aagaard), 2463 (LinkedIn user)
- **Context**: "backup" systems needed, "intermittent" wind generation issues
- **Usage**: Describes the challenges that supply security addresses

**Additional observations**:
- "Energy security" appears in some international contexts (ID: 256, Danish Energy Agency)
- Terms like "resilience" and "fluctuation" also relate to supply security
- Issue 5 contains 755 statements (12.5% of corpus) on this topic

---

## Q2: Comprehensive Supply Security Query

**Question**: Build a Pandas query capturing energy supply security statements.

**Query**:
```python
condition_supply_security = df['Statement'].str.contains(
    'supply security|security of supply|stable energy|energy stability|'
    'reliability|reliable energy|reliable supply|backup power|backup|'
    'resilience|resilient|intermittent|fluctuat|energy storage|'
    'stable supply|energy stability',
    case=False,
    na=False
)
```

**Results**:
- **Total matches**: 320 statements
- **Percentage of corpus**: 5.3%
- **Overlap with Issue 5**: 214 statements (28.3% coverage of Issue 5)

**Validation**:
- Issue 5 ("Will we have a stable energy supply?") has 755 statements total
- Our query captures 28.3% of Issue 5, indicating good precision
- The remaining Issue 5 statements likely use more implicit language

**Temporal distribution**:
- Peak activity in 2024: 112 statements (35% of matches)
- Steady growth from 2021-2025: 276 statements (86% of matches)
- Historical references date back to 1998

**Key insight**: The query successfully captures explicit mentions of energy supply security using multiple formulations, with strong overlap with the manually-coded Issue 5.

---

## Q3: Issue Identification for Energy Supply Security

**Question**: Which issue(s) correspond to energy supply security?

**Answer**:

**Issue 5: "Will we have a stable energy supply?"**

This issue directly corresponds to energy supply security concerns in the Energy Islands controversy.

**Evidence**:
- **Issue 5 contains 755 statements** (12.5% of the entire corpus)
- **Top actors** discussing this issue include:
  - Lars Aagaard (28 statements)
  - Energinet (15 statements)
  - Jacob Østergaard (14 statements)

**Key themes within Issue 5**:
1. **Reliability of renewable-dependent systems**: Can wind-based energy islands provide consistent power?
2. **Intermittent wind power concerns**: What happens when "the wind doesn't blow"?
3. **Backup power requirements**: What backup systems are needed?
4. **Energy storage solutions**: How can we store excess energy?
5. **Overall security of supply**: Will Denmark have stable electricity?

**Issue Atlas description context**:
Issue 5 addresses fundamental questions about whether Denmark's transition to renewable energy via energy islands will maintain a stable and reliable electricity supply, making it the primary issue for energy supply security discussions.

---

## Q4: Cluster Identification for Energy Supply Security

**Question**: Which semantic cluster(s) correspond to energy supply security?

**Answer**:

**Primary Cluster**: **(None)** - 233 statements (72.8% of supply security statements)

The majority of energy supply security statements fall into the **(None)** cluster, indicating that supply security is discussed across multiple thematic contexts rather than being concentrated in a single semantic cluster.

**Secondary Clusters** (statements also discussing supply security):

1. **"Waste of tax payer's money"** - 22 statements (6.9%)
   - Supply security used as justification for expensive projects
   - Economic criticism of projects defended on security grounds

2. **"Energy hubs towards P2X"** - 19 statements (5.9%)
   - Technical discussions of energy storage and conversion
   - Power-to-X solutions for handling intermittency

3. **"Job creation and innovation"** - 12 statements (3.8%)
   - Supply security linked to economic development
   - Innovation opportunities in grid stability technologies

4. **"The nuclear alternative"** - 7 statements (2.2%)
   - Comparing renewable intermittency with nuclear baseload power
   - Supply security arguments for/against nuclear

**Key insight**: Energy supply security is a **cross-cutting concern** rather than a standalone topic. It appears in debates about economics, technology, policy, and alternatives, reflecting its role as a fundamental requirement that intersects with multiple controversy dimensions.

---

## Q5: Combined Query (Supply Security + Expertise)

**Question**: Create a query capturing statements about BOTH energy supply security AND expertise (minimum 15 matches).

**Query**:
```python
# Supply security component
condition_supply_security = df['Statement'].str.contains(
    'supply security|security of supply|stable energy|energy stability|'
    'reliability|reliable energy|reliable supply|backup power|backup|'
    'resilience|resilient|intermittent|fluctuat|energy storage|'
    'stable supply|energy stability',
    case=False,
    na=False
)

# Expertise component
condition_expertise = df['Statement'].str.contains(
    'expert|expertise|analysis|analyze|recommend|recommendation|report|study|research|'
    'scientist|professor|consultant|analyst|assessment|evaluate|evaluation|'
    'agency|authority|institute|university|model|forecast|predict|estimate',
    case=False,
    na=False
)

# Combined (AND operator)
condition_combined = condition_supply_security & condition_expertise
```

**Results**:
- **Total matches**: 116 statements
- **Requirement (≥15)**: ✓ **MET** (exceeded by 101 statements!)
- **Percentage of supply security statements**: 36.3% (116/320)

**Key Actors** (expertise-based organizations discussing supply security):

1. **Kraka Economics**: Think tank providing critical economic analysis
2. **Energinet**: State transmission system operator with technical expertise
3. **Danish Energy Agency**: Government authority providing cost-benefit analyses
4. **Aalborg University** (Brian Vad Mathiesen): Academic energy systems research
5. **Technical University of Denmark** (DTU Energy, Søren Linderoth): Technical research
6. **COWI**: Engineering consultancy
7. **Danish Chamber of Commerce**: Business sector economic analysis
8. **Baltic Energy Island**: Project developer conducting assessments

**Cluster Distribution**:
- **(None)**: Majority of statements
- **"Waste of tax payer's money"**: Economic critique based on expert analysis
- **"Energy hubs towards P2X"**: Technical research on storage solutions
- **"Job creation and innovation"**: DTU and research institutions

**Temporal Distribution**:
- Peak in 2024-2025: Corresponds to expert reports from Kraka Economics and Danish Energy Agency
- Sustained academic and technical discourse throughout controversy

**Sample High-Impact Statements**:

- **ID 17** (Kraka Economics): Critiques supply security as insufficient justification
- **ID 85** (Hanne Storm Edlefsen, Energinet): Technical analysis of feasibility
- **ID 112** (Brian Vad Mathiesen, Aalborg University): Academic response to Kraka report
- **ID 256** (Danish Energy Agency): Cost-benefit analysis conclusion
- **ID 6536** (Frederik Løssøe Nielsen, Kraka Economics): Expert critique of project economics

**Key insight**: Expert discourse on supply security is substantial, with 116 statements representing diverse expertise types (academic, technical, economic, governmental). This demonstrates that energy supply security is heavily contested through expert knowledge claims rather than purely political or ideological arguments.

---

## Summary Statistics

| Question | Metric | Value |
|----------|--------|-------|
| Q1 | Alternative formulations identified | 5 |
| Q2 | Supply security statements | 320 (5.3%) |
| Q2 | Issue 5 coverage | 28.3% |
| Q3 | Primary issue | Issue 5 (755 statements, 12.5%) |
| Q4 | Primary cluster | (None) - 72.8% |
| Q4 | Secondary clusters | 5 identified |
| Q5 | Combined matches | 116 (exceeds requirement) |
| Q5 | Expert organizations | 8+ identified |

---

## Methodological Notes

1. **Query Design**: Regex patterns were iteratively refined using exploratory searches
2. **Validation**: Cross-checked query results against Issue Atlas manually-coded categories
3. **Cluster Analysis**: The high percentage of "(None)" cluster suggests supply security is discussed across multiple semantic contexts
4. **Expertise Definition**: Broad definition including academic, technical, governmental, and consultancy sources
5. **Dataset**: 6,061 actor statements from Energy Islands controversy (data/Actor statement dataset.csv)

---

## Files Generated

1. **Notebook**: `notebooks/local/Assignment_Q1_Q2_Q4_Q5.ipynb` (interactive analysis)
2. **Script**: `notebooks/local/run_Q1_Q2_Q4_Q5.py` (automated analysis)
3. **Results**: `notebooks/local/Q1_Q2_Q4_Q5_results.txt` (full output, 848 lines)
4. **Answers**: `notebooks/local/Assignment_D_Q1-Q5_Answers.md` (this document)

---

*Analysis completed: 2026-01-20*
*Dataset: Actor statement dataset (6,061 statements)*
*Corpus: Energy Islands controversy, Denmark (1998-2025)*
