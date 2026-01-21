# Day 8.2 - Mapping #1: Explore the issue atlas

---

In these sessions we work with the data, scripts and case material collected in the [The issue atlas on the Danish energy islands](https://learn.inside.dtu.dk/d2l/common/dialogs/quickLink/quickLink.d2l?ou=294618&type=content&rcode=dtu-713211).

## Purpose of this lecture

Engage with the actor statement dataset and learn how to use the notebooks. Why we don’t have to follow demographic sociology with web data. Understand that one can be objective about the actors’ discourse without deciding who is or isn’t objective. Understand how the semantic map supports exploration. Differentiate coding that is bottom-up (clusters) or top-down (issues).

## Lecture slides

Attached.

## Material

[Mini into to Google Colab (video)](https://youtu.be/UPyGLa4q_Dw)

The dataset and the notebooks are available in this GitHub repository:

> **[> https://github.com/jacomyma/dtu-sts-material/](https://github.com/jacomyma/dtu-sts-material/)**

The notebooks come in two versions because you have two options.

1.  Run notebooks online with Google Colab. Open the [notebook/colab/](https://github.com/jacomyma/dtu-sts-material/tree/main/notebooks/colab) folder, click on a notebook in the list, then click on "Open in Colab" on top. This will create a copy of the notebook in your Google Drive and open it in Colab (see intro above). This will require you to authorize each script to access your Google account so that it can access the online version of the document.
    ![Google Colab Folder Button](https://learn.inside.dtu.dk/content/enforced/294618-DTU_v25_42620/image_20250812112513275.png)

2.  Run notebooks locally with Jupyter (or another compatible system like VS Code). We recommend that you download, install, and run [Anaconda Navigator](https://www.anaconda.com/download/success) and from there to run Jupyter. You can then run the notebooks from the GitHub repository in the [notebook/local/](https://github.com/jacomyma/dtu-sts-material/tree/main/notebooks/local) folder. Those do not require any Google account, but you have to set up the notebook environment and download the notebooks and the data.
    ![Anaconda Navigator Interface](https://learn.inside.dtu.dk/content/enforced/294618-DTU_v25_42620/image_20250812112805330.png)

Note: the repository also contains the dataset as a CSV in the [data/](https://github.com/jacomyma/dtu-sts-material/tree/main/data) folder.

Here is a quick **description** of what each notebook does and how you should use it:

* [**Query examples**](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Query_examples.ipynb): read it carefully to understand how to compose queries in the language of Pandas. Suggestion: make a copy of that notebook and add your own queries in the end, that will be useful for copy-pasting them into other notebooks.
* [**Retrieve subcorpus - Filter and export**](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Retrieve_subcorpus_Filter_and_export.ipynb): assuming you have a query, use it to filter the actor statements matching it (i.e. the "subcorpus"), and export it as a CSV or as a text file. The CSV allows you to analyze the subcorpus into another tool like a spreadsheet. The text file is to make it easier for you to read through the statements, which is very important for qualitative moments of the analysis.
* [**Semantic map - Explore (interactive)**](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Semantic_map_Explore_(interactive).ipynb): generates a zoomable plot that you can explore interactively. It allows you to read statements by semantic proximity, which is useful to explore different parts of the controversy. It matches the annotated renderings of the atlas.
* [**Semantic map - Filter and explore (interactive)**](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Semantic_map_Filter_and_explore_(interactive).ipynb): same as above, but allows you to highlight certain statements with a query. Useful to check if a query gives semantically similar results.
* [**Semantic map - Filter and render**](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Semantic_map_Filter_and_render.ipynb): same as above including the ability to query, but produces a high-resolution, non-interactive rendering, which is better suited to copy-paste into documents.
* [**Timeline - Filter and render**](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Timeline_Filter_and_render.ipynb): renders a timeline of the volume of statements over time, as a bar chart. Requires a query, and produces 4 variations to choose from. Read the pros and cons of each variation to understand which one is the most appropriate in your situation.
* [**Visualize by actor - Filter and render**](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Visualize_by_actor_Filter_and_render.ipynb): Generates bar charts of the volume of statements by actor. Requires a query.
* [**Visualize by cluster - Filter and render**](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Visualize_by_cluster_Filter_and_render.ipynb): Generates bar charts of the volume of statements by cluster. Requires a query.
* [**Visualize by issue X - Filter and render**](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Visualize_by_issue_X_Filter_and_render.ipynb): Generates bar charts of the volume of statements by issue (you have to precise which issue you want to focus on). Requires a query.
* [**Visualize by organization (represented by an actor) - Filter and render**](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Visualize_by_organization_(represented_by_an_actor)_Filter_and_render.ipynb): Generates bar charts of the volume of statements by column "represented by" which indicates which organization is represented by the statement's author (if any). Requires a query.
* [**Visualize by source name - Filter and render**](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Visualize_by_source_name_Filter_and_render.ipynb): Generates bar charts of the volume of statements by source name. Requires a query.
* [**Visualize by source type - Filter and render**](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Visualize_by_source_type_Filter_and_render.ipynb): Generates bar charts of the volume of statements by source type. Requires a query.

Note: the purpose of the "Visualize by..." notebooks is always to produce query-based measurements of the corpus. Each one may or may not be relevant to you depending on what you will focus on in your policy brief.

## Key notions

Each point was explained during the lecture, but they are briefly recapped here and you can find a bit more in two places: in the PDF "17 key controversy mapping notions" (look into learn under the lecture *Mapping #1*) and in the glossary that you will receive at the beginning of week 3.

### Post demographics (Rogers)
Is online friendship “real” friendship? Are social media accounts “real” people?

In short, according to Richard Rogers, we do not have to pretend that a user account matches a person, which is not true in general. We can still study user accounts sociologically.

### Just observe
According to Bruno Latour, you should *“just observe and describe controversies.”* Which means:
* Do not restrain your observation to any single theory or methodology;
* observe from as many viewpoints as possible;
* listen to actors’ voices more than to your own presumptions.

### Second degree objectivity
Within a controversy, the absence of agreement between actors prevents us from finding “the objective truth.” But if there is no objectivity in controversies, how can they be studied objectively?

Second-degree objectivity means **being objective about what actors say and do regarding disputed facts**, rather than trying to objectively determine which facts are true.

### Exploratory Data Analysis (EDA)
Exploratory vs. confirmatory: exploring data differs from applying the statistical toolbox to confirm hypotheses. Exploration finds questions, while confirmation finds answers.

Exploratory vs. explanatory: although the tools are the same, exploration entails visualizing for yourself while explanation entails visualizing for other people, which requires different strategies.

## Exercise instructions

**Goal: familiarize yourselves with the Python notebooks.**

If you are already familiar with Python and notebooks, you may skip this and try the bonus exercise.

* Try to run a notebook on Google Colab.
* If you feel you can do it, try to run a notebook on your local computer using Anaconda and Jupyter.
* Read the description of the notebooks (find it above or in the GitHub's [README](https://github.com/jacomyma/dtu-sts-material/tree/main?tab=readme-ov-file#notebook-description)) to have an idea of what they do.
* Take a close look at the "[Query examples](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Query_examples.ipynb)" notebook to have an idea of how queries work in those notebooks.
* Take a look at the "[Timeline - filter and render](https://github.com/jacomyma/dtu-sts-material/blob/main/notebooks/colab/Timeline_Filter_and_render.ipynb)" notebook and take note of the fact that it produces 4 different versions of the same visualization. Most notebooks produce those 4 different versions, and you will have to understand their differences.

### **Bonus follow-up exercise: Learn how to use the different notebooks as tools for inquiry.**

**Goals: (1) realize that the most difficult part is not to make the notebooks work on a technical level, but to find out how you must tune them to get insightful dataset measurements; and (2) to make a few attempts at obtaining some specific measurements.**

Use the notebooks to achieve as many of the following tasks as you can. Take screenshots of the queries and visualizations used to achieve each task and paste them in a document so that you can go back to it later on.

1.  Task: Identify an issue that peaks in 2023 (relatively to the total volume of statements in the corpus)
2.  Task: Identify an issue that strongly matches a cluster in particular, i.e. where >70% of that cluster's statements would be matching the issue, while other clusters would match the issue at <30%.
    *Optional: Hypothesize what broader pattern or phenomenon this limited result set might indicate.*
3.  Task: Identify a query that is present mostly on social media (all other source types matching it at less than half the percentage they match social media).
    *Optional: Hypothesize what broader pattern or phenomenon this limited result set might indicate.*
4.  Task: Identify a search query that returns fewer than 5 results.
    *Optional: Find a query where obtaining fewer than 5 results would be meaningful for analyzing the project. Hypothesize what broader pattern or phenomenon this limited result set might indicate.*
5.  Task: Identify a search query that returns more than 3000 results.
    *Optional: Find a query where obtaining more than 3000 results would be meaningful for analyzing the project. Hypothesize what broader pattern or phenomenon this limited result set might indicate.*
6.  Task: Identify a search query that returns 100 to 1000 results, and those results are evenly distributed in the map.
    *Optional: idem about the results being evenly distributed in the map.*
7.  Task: Identify a search query that returns 100 to 1000 results, and those results are mostly clustered in the map.
    *Optional: idem about the results being mostly clustered in the map.*