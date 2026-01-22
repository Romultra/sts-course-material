# Lecture Notes: Day 9.2 - Mapping #3: Make Data-Driven Points
**Course:** 42620 Science, Technology & Society (DTU)
**Lecturer:** Mathieu Jacomy (Aalborg University Tantlab + MASSHINE)

---

## 1. Core Concept: Making Data-Driven Arguments

### Measurements in Sociology
* **Definition:** Measurements are the practical work of making social life knowable, comparable, and actionable within research communities.
* **Application:** In this course, the visualizations and numbers generated from the dataset (via notebooks) constitute "measurements".
* [cite_start]**Objectivity:** A measurement like "26.9% of statements mention Bornholm" is a fact that does not depend on the reader's subjectivity [cite: 2343-2344].

### Circulating Reference (Bruno Latour)
* **Concept:** Scientific facts do not mirror reality directly. [cite_start]They gain power by moving through a "chain of transformations"[cite: 2346].
* [cite_start]**The Chain:** Each step changes the **matter** (format) but maintains the **form** (connection/logic) [cite: 2351-2356].
    * [cite_start]*Phenomenon (Reality)* $\rightarrow$ *Dataset* $\rightarrow$ *Visualization* $\rightarrow$ *Measurement* $\rightarrow$ *Argument (Policy Brief)* [cite: 2358-2363].
* **Implication:** Your Policy Brief argument is the final link in this chain, grounded in the original phenomenon through these robust steps.

### Truth vs. Robustness
* **Key Distinction:** Scientific arguments are not robust because they are inherently "true." [cite_start]Instead, they **become true** as they get more robust (i.e., when they "hold" against criticism) [cite: 2365-2367].
* **Goal:** You must demonstrate to others that your reasoning is resilient to counterarguments. It is not enough to just be convinced yourself.

---

## 2. The Toulmin Argument Model
To build robust scientific arguments, use the framework introduced by philosopher **Stephen Toulmin** (1958). A robust argument is not just *Claim + Data*; it requires connecting the two explicitly.

### The 6 Components of an Argument
1.  [cite_start]**Claim:** The statement that something is so (e.g., "The Earth is round")[cite: 2404].
2.  [cite_start]**Grounds:** The data or measurement backing the claim (e.g., "Earth's shadow on the Moon is round")[cite: 2400].
3.  [cite_start]**Warrant:** The logical bridge explaining *why* the claim follows from the grounds (e.g., "Shadows indicate the shape of objects")[cite: 2399]. *Crucial for validity.*
4.  [cite_start]**Backing:** Factual support for the Warrant (e.g., "We have seen spherical objects cast round shadows many times")[cite: 2397].
5.  [cite_start]**Qualifier:** The degree of certainty (e.g., "So we can *reasonably consider*...")[cite: 2406].
6.  [cite_start]**Rebuttal:** Exceptions/counter-arguments (e.g., "Unless the Earth is a flat disc facing the sun directly")[cite: 2408].

### [cite_start]Example: The Bornholm Argument [cite: 2426-2442]
* **Grounds:** "1632 of 6061 statements (26.9%) mention 'Bornholm'."
* **Claim:** "Bornholm is an important part of the Energy Islands project."
* **Warrant:** "Terms recurring in this corpus are important elements of the discourse."
* **Backing:** "The corpus captures the voices of many different actors in many different spaces."
* **Rebuttal:** "Unless the corpus is strongly biased in favor of mentioning Bornholm."

---

## 3. Advanced Tools: NotebookLM & RAG

### Retrieval Augmented Generation (RAG)
* [cite_start]**Definition:** RAG is the technology behind tools like NotebookLM [cite: 2446-2447].
* **Mechanism:**
    1.  **Retrieval:** The system searches your specific documents (the "Knowledge Stack") for relevant information.
    2.  **Generation:** It feeds that specific information into an LLM to generate an answer.
* **Benefit:** Allows you to "chat" with your specific dataset rather than just using the AI's general training data.

### Practical Application
* **NotebookLM / Msty Studio:** You can ingest the course corpus (as Markdown files) into these tools to investigate it qualitatively.
    * *Note:* The corpus was chunked into 7 markdown files because it was too large for a single upload.
* **Nomic Atlas:** A tool used to visualize the "embedding space" (semantic map) that powers RAG systems, showing how the AI groups similar concepts.

---

## 4. Exam & Policy Brief Tips
* [cite_start]**Build "Scaffolding":** Your arguments should be structured like scaffolding—visible, logical, and supporting the weight of your claims[cite: 2327].
* **Explicit Warrants:** In your assignment, don't just show a graph and a conclusion. Explain *why* that graph allows you to draw that conclusion (the Warrant).
* **Acknowledge Limits:** Use the **Rebuttal** and **Qualifier** to show you understand the limitations of your data (e.g., "Unless the dataset is biased..."). This increases scientific robustness.