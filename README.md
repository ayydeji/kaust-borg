# Comparing Symbolic and Distributive Methods In Machine Learning.
## Overview.
This project was conducted in KAUST as part of the Bio-Otology Research group. In this repository you will find the files and results from normal distributive models e.g. TransE, TransR and ConvE in comparison with the results obtained from symbolic methods implemented using TILDE, GILPS and QuickFoil.
## System Requirements.
- Python3 
- [Pykeen]( https://github.com/SmartDataAnalytics/PyKEEN)
`
pip install pykeen
`
- [TILDE](https://github.com/joschout/tilde.git) ` git clone https://github.com/joschout/tilde.git`
- [GILPS](https://github.com/bio-ontology-research-group/GILPS.git) ` git clone https://github.com/bio-ontology-research-group/GILPS.git`
- [QuickFoil](https://github.com/bio-ontology-research-group/quickfoil.git) ` git clone https://github.com/bio-ontology-research-group/quickfoil.git`

## The Data.
### Drug Disease.
The aim of this dataset is to predict drug-disease associations using pykeen and ilp methods; TILDE, GILPS and QuickFOIL.
The data was created by integrating Drug-Target interactions from **DrugBank**, Protein-Protein Interactions from **STRING** Protein-Disease and Drug-Disease Interactions from **SIDER**.
### Maxat Test (Yeast and Human).
This directory holds protein annotations and protein links for both human and yeast datasets. In the **Data** sub-directory you will find the indevidual files. In the **pykeen** subdirectory you will find the files that will run using pykeen and in the **ilp** directory you will find the reelvent Knowledgebase files for the respective tools; TILDE, GILPS and QuickFOIL.

In the Scripts directory you will find the scripts used to create these indevidual files, written in python.
### Knowledege_embeddings.
This is the microsoft **FB15K-237** dataset, as well as the training and testing datasets you will also find the scripts used to convert the data to the relevent formats.
