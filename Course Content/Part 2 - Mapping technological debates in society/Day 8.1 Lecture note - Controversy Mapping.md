# Lecture Notes: Day 8.1 - Introduction to Controversy Mapping
**Course:** 42620 Science, Technology & Society (DTU)
**Lecturer:** Anders Kristian Munk

---

## 1. What is Controversy Mapping?

### Definition & Context
* **Role in RRI:** Controversy mapping is the primary method used to address the **Engagement** component of the **AREA framework** (Anticipate, Reflect, Engage, Act).
* **Core Purpose:** To open up anticipation and reflection to a wider range of societal stakeholders. It helps identify stakeholders who are not currently "on the radar".
* **Emergence:** Controversies are dynamic; they constantly produce *new* stakeholders who were previously unaware of their interests or silent. Mapping allows us to trace these actors and issues as they *emerge*.

### The "Wicked Problem" Connection
* RRI deals with wicked problems.
* The wickedness of a problem often depends on how different actors **frame** it.
* **Key Question:** *How represent diverse framings?* Controversy mapping provides the tools to see how actors define the problem differently.

### Guiding Questions for Analysis
[cite_start]Mapping answers descriptive questions in shifting situations [cite: 15-18]:
1.  **Who** are the actors?
2.  **What** are their concerns?
3.  **What** arguments are they making?
4.  **How** is the controversy changing over time?

---

## 2. Methodology: "Quali-Quantitative"
Controversy mapping is described as a **quali-quantitative** method. [cite_start]It combines digital data visualization with qualitative interpretation to explore data "from the ground up"[cite: 19].

### Key Textbooks
* [cite_start]*Controversy Mapping: A Field Guide* (Venturini & Munk) [cite: 10, 90-92].
* [cite_start]*Doing Digital Methods* (Rogers) [cite: 153-154].
* [cite_start]*Mapping the Dynamics of Science and Technology* (Callon, Law, Rip) [cite: 149-151].

---

## 3. Case Studies & Examples
The lecture introduces previous mapping projects to illustrate the method's capabilities.

### A. The Battle for Amager Commons (Fælled)
* [cite_start]**Subject:** Conflict over building on a nature reserve (2016-2017) [cite: 24-32].
* [cite_start]**Method:** Traced digital user reactions (Facebook "Like", "Angry", "Love") and engagement volume over time [cite: 55-58].
* [cite_start]**Insight:** Visualized how specific events (e.g., "Chef shares petition," "Mayor puts plans on hold") triggered spikes in public sentiment and shifted the emotional tone of the debate[cite: 71, 77].

### B. UNFCCC Negotiations (Climate Change)
* [cite_start]**Subject:** Evolution of climate issues from 1995-2013[cite: 88].
* **Method:** Visualized the "absolute and relative visibility" of keywords.
* [cite_start]**Insight:** Showed how topics like "Kyoto Protocol" faded while "Adaptation funding" rose, demonstrating the shifting focus of global attention [cite: 89, 93-96].

### C. Wind Energy Controversies (Wind2050)
* [cite_start]**Subject:** 758 websites related to wind energy across 6 countries[cite: 157].
* **Method:** Hyperlink analysis to map the network of proponents (PRO) vs. opponents (CON).
* **Findings:**
    * [cite_start]**Polarization:** A clear structural division existed between PRO and CON clusters[cite: 182].
    * [cite_start]**Density:** The Opponent (CON) network was denser and more interconnected than the Proponent network [cite: 171-172].
    * [cite_start]**Issue Specificity:** Nodes could be sized by specific concerns (e.g., "Noise regulation," "Bird migration," "Infrasound") to see *who* cared about *what* [cite: 207-209].

---

## 4. The "Energy Islands" Issue Atlas (The Course Dataset)
This section outlines the specific dataset students will use for their **Policy Brief**.

### The Dataset Structure
* [cite_start]**Content:** 6,061 **Actor Statements** regarding the Danish Energy Islands[cite: 402].
* [cite_start]**Source:** Harvested from open online sources (media, reports, parliament) Jan–May 2025[cite: 360].
* [cite_start]**Format:** Statements are paraphrased into first-person quotes (e.g., *"I insist on prioritizing local business..."*) to ensure comparability[cite: 385, 491].
* [cite_start]**Metadata:** Each statement is tagged with Actor, Organization, Role, Date, Medium, and Source URL[cite: 390].

### Two Methods of Issue Discovery
[cite_start]The dataset is organized using two distinct approaches [cite: 362-363]:

#### 1. Bottom-Up (Semantic Analysis)
* [cite_start]**Technique:** Uses AI embedding models to place statements in a 2D map based on semantic similarity[cite: 372].
* **Visual:** **Annotated Semantic Basemap**.
* **Structure:** Statements cluster naturally. [cite_start]These clusters are qualitatively summarized (e.g., "German collaboration," "Financial uncertainty") [cite: 371-374, 407].
* **Use:** Good for finding organic, unexpected themes.

#### 2. Top-Down (Expert-Driven Classification)
* **Technique:** An "Issue Dictionary" of 16 key issues was defined by experts. [cite_start]An LLM classified every statement against these issues [cite: 395-396].
* [cite_start]**Example (Issue 16):** *"Are the energy islands socially and economically just?"* [cite: 431]
    * [cite_start]Includes concerns about: Job creation, taxpayer burden, local community impact, and profit distribution [cite: 432-436].
* **Use:** Good for filtering the map to see *where* specific, known issues are being discussed.

---

## 5. Visualizations & Analysis Tools
[cite_start]Students must use these tools to justify their methodology in the exam assignment[cite: 213].

### 1. Annotated Basemap
* **What it is:** A spatial map where distance = difference. Dots close together are semantically similar.
* **How to read it:** Look for clusters. [cite_start]Large, dense areas represent dominant themes [cite: 417-418].

### 2. Issue Overview
* [cite_start]**What it is:** Highlights a specific issue (e.g., Issue 16) on the basemap[cite: 404].
* [cite_start]**Key Data:** Shows the **Top 5 Actors** addressing that issue (e.g., identifying that "Kraka Economics" is a top voice on economic justice) [cite: 461-462].

### 3. Co-occurrence Matrix
* [cite_start]**What it is:** A heatmap showing how often two issues are mentioned together[cite: 405].
* **Use:** Identifies linkages (e.g., do people who talk about "Financial Uncertainty" also talk about "Nuclear Alternative"?).

### 4. Timeline Analysis
* [cite_start]**What it is:** A graph of statement volume over time[cite: 219].
* **Use:** Tests hypotheses about *drivers* of controversy.
* [cite_start]**Example:** A spike in "financial unfairness" arguments in 2024 might correlate with the publication of a critical report by Kraka[cite: 629].

---

## 6. Exam Focus: Developing Your Methodology
[cite_start]For the **Policy Brief**, you must document your search strategy[cite: 213].

### The Iterative Process
1.  [cite_start]**Formulate a Hypothesis:** (e.g., "There are three distinct versions of the 'Social Justice' issue.")[cite: 543].
2.  [cite_start]**Query the Data:** Filter by Issue (e.g., Issue 16) AND Keywords (e.g., "jobs," "Kraka")[cite: 619, 622].
3.  **Evaluate:** Does the timeline or actor list support your hypothesis?
    * [cite_start]*Example:* If searching for "local business" yields little data, your hypothesis about that sub-theme might need revision[cite: 621].
4.  [cite_start]**Refine:** Create a new query or look at a different time period[cite: 621, 679].

### [cite_start]Questions for Deep Analysis [cite: 672-678]
* What ethical frameworks underpin the actors' arguments?
* How do actors perceive risk differently?
* Who is recognized as an "expert" in the debate?
* How do these competing frames create "wickedness"?

---

**Summary for Exam:**
Controversy mapping is not just making a pretty map; it is an **exploratory research process**. You must demonstrate that you used the tools (timelines, basemaps, queries) to *discover* something specific about the actors and their concerns that justifies your policy intervention.