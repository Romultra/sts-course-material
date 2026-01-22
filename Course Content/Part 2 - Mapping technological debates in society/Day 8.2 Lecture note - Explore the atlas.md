# Lecture Notes: Day 8.2 - Mapping #1: Explore the Atlas
**Course:** 42620 Science, Technology & Society (DTU)
**Lecturer:** Mathieu Jacomy (Aalborg University Tantlab + MASSHINE)

---

## 1. The Semantic Map: Understanding the Tool

### What is it?
The core of the "Issue Atlas" is a **semantic map**. It visualizes the corpus of actor statements based on their content.
* [cite_start]**The Dot:** Each dot represents a single **statement**[cite: 707].
* **The Space:** The distance between dots represents **semantic similarity**.
    * [cite_start]**Close dots** = Similar meaning/content[cite: 708].
    * [cite_start]**Distant dots** = Dissimilar meaning/content[cite: 708].
* [cite_start]**The Cluster:** Groups of very similar documents that form dense clouds on the map[cite: 709].

### Where does it come from? (Technical Basis)
* [cite_start]The map is generated using a **text embedding model** (similar to Word2Vec, but for whole documents) [cite: 743-749].
* [cite_start]**How it works:**  The model transforms words/texts into **vectors** that preserve relations of meaning (e.g., "King" is to "Queen" what "Man" is to "Woman")[cite: 745].
* [cite_start]**Dimensionality Reduction:** The complex, multi-dimensional vector data is "flattened" into a 2D map to make it readable for human analysis[cite: 746].

---

## 2. Theoretical Frameworks for Digital Methods
These three concepts are critical for justifying your methodology in the exam and Policy Brief.

### A. Post-Demographics (Richard Rogers)
* [cite_start]**The Problem:** Online data is not representative of the general population (e.g., Is a Twitter account a "real" person? Is an online friend a "real" friend?) [cite: 751-753].
* **The Concept:** "Post-demographics" stands in contrast to traditional sociology. [cite_start]We do not attempt to organize groups/voters in a demographic sense[cite: 755].
* **The Method:** We do not pretend a user account matches a biological person. [cite_start]Instead, **we study actor statements for what they are**, regardless of "representativity" [cite: 758-759].

### B. "Just Observe" (Bruno Latour/Tommaso Venturini)
* **The Instruction:** To analyze a controversy, you must suspend judgment. [cite_start]"Don't give your opinion or tell who is right or wrong"[cite: 771].
* [cite_start]**Guidelines for "Just Observing"** [cite: 762-766]:
    1.  Do not restrict observation to a single theory.
    2.  Observe from as many viewpoints as possible.
    3.  Listen to actors' voices rather than your own presumptions.

### C. Second-Degree Objectivity
* [cite_start]**The Paradox:** If a controversy is defined by a lack of agreement (subjectivity), how can we study it objectively?[cite: 795].
* [cite_start]**Definition:** Unlike first-degree objectivity (collective agreement on facts), **second-degree objectivity** is attained by revealing the *full extent* of the actors' disagreement[cite: 797].
* [cite_start]**Application:** Do not denounce actors for lacking objectivity; instead, objectively describe the extent of their subjectivity [cite: 800-801].

---

## 3. Methodological Approaches: Issues vs. Clusters
The dataset is organized in two ways. You must understand the difference to use them correctly in your analysis.

| Feature | **Issues (Top-Down)** | **Clusters (Bottom-Up)** |
| :--- | :--- | :--- |
| **Origin** | [cite_start]Defined by **Researchers** (The "Issue Dictionary")[cite: 875]. | [cite_start]Defined by **Actors** (The semantic data itself)[cite: 885]. |
| **Method** | [cite_start]**AI Coding:** LLM codes statements against 16 descriptions[cite: 872]. | [cite_start]**Vector Math:** Dense groups in the vector space are identified and labeled [cite: 880-881]. |
| **Exclusivity** | [cite_start]**Non-mutually exclusive:** A statement can be tagged with 0, 1, or multiple issues[cite: 874]. | [cite_start]**Mutually exclusive:** Each statement belongs to exactly one cluster (or zero)[cite: 883]. |
| **Homogeneity**| [cite_start]**Heterogeneous:** Captures variety within a topic[cite: 876]. | [cite_start]**Homogeneous:** Contains semantically similar statements by design[cite: 886]. |

---

## 4. Exploratory Data Analysis (EDA)
The lectures distinguish between different modes of analysis you will perform.

### Exploratory vs. Confirmatory
* **Exploratory:** Finding the questions. You visualize data to find patterns or anomalies.
* **Confirmatory:** Finding the answers. Applying statistical tools to confirm a hypothesis.

### Exploratory vs. Explanatory
* **Exploratory:** Visualizing for *yourself* to understand the data.
* **Explanatory:** Visualizing for *others* (e.g., in your Policy Brief) to communicate a specific finding.

---

## 5. Practical Tools: The Notebooks
You will use Python notebooks (via Google Colab or Jupyter) to query the dataset.

### Key Notebooks for the Exam Assignment
* **Semantic Map (Interactive):** Useful for exploring. You can zoom in and read statements based on their semantic proximity.
* **Timeline (Filter and Render):** Produces bar charts of statement volume over time. Essential for seeing when a controversy "spiked".
* **Visualize by Actor/Source:** Helps identify *who* is speaking about a specific query.

### The Investigation Process
1.  **Query:** Create a search query (e.g., "Nuclear Power").
2.  **Filter:** Isolate the "subcorpus" that matches the query.
3.  **Visualize:** Use the notebooks to render this subcorpus on the map or timeline.
4.  **Interpret:** Does the map follow intuition? (e.g., Does the "Nuclear" query light up the specific area of the map where Issue 9 is located?) [cite_start][cite: 863-865].

---

**Summary for Exam:**
* **Methodology:** You are using **Post-demographic** methods to achieve **Second-degree objectivity**.
* **Data:** You are navigating between **Top-down** (Issues defined by experts) and **Bottom-up** (Clusters defined by semantic similarity) perspectives.
* **Goal:** To "Just Observe" the controversy as it unfolds, mapping the actors and their concerns without imposing your own judgment on who is "right."