# Predicting food crises using news streams

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1XN9RyNp49b5YkX2jsafKCoWoOjS2Yv2O" alt="Uncovering text features related to food insecurity."/>
<p/>

In this public repository we outline our methodolgy for [predicting food crises using news streams](https://www.science.org/doi/10.1126/sciadv.abm3449) to ease replication. Find out which features we have assembled and how to set up the methodology for your personal use cases. You can also [report bugs here](https://github.com/TryShape/tryshape/issues/new/choose).

## Methods
This repository includes multiple individual features, which we employed for our research that can be utilized in isolation.

### Feature 1: Causal Feature Extraction
This feature extracts causal indicators from (news) sentences. Our scrutinized news dataset stems from the Factiva API, wherefore we are not able to share it publicly. Therefore, we have included a sample "sentences.txt" that should allow to reproduce the method on a news text of your choice.

### Feature 2: Granger Test for Time Series
...

Once the causal factors are extracted, we include the code to extract time series, filter out non-predictive factors by doing a Granger test on the time series of the factors with code in the folder, and plotting map and scatter plots



### Feature 3: Regression Modelling
...
Finally, the processed time series are then added as input to our regression models for food insecurity in the iPython notebook: "3. Fig3_regression.ipynb". This notebook generates the data that is plotted in Fig 3. Please download the processed time series dataset from https://drive.google.com/drive/folders/1OtNqeDjTW7IVlnfgYiMyrIbvAyx4q_27?usp=sharing and change the filepath in the notebook to a relevant path in your directory.





## Data
... Data Source 1: News Sources
... Data Source 2: IPCC Classification
...


## How to set up ```food_insecurity_predictions_nlp```
...

## Built With
...

## License
This project is licensed under the MIT License - see the [```LICENSE```](https://github.com/philippzi98/food_insecurity_predictions_nlp/) file for details.


## Authors & Contact
In case of any questions or remarks, please feel free to reach out to us via e-mail:
- [e-mail](mailto:sfraiberger@worldbank.org).
- **Samuel Paul Fraiberger** - [johndoe](https://github.com/johndoe) - *Affiliation: The World Bank*
- **Balashankar** - [janesmith](https://github.com/janesmith) - *Affiliation: New York University*
- **Balashankar** - [janesmith](https://github.com/janesmith) - *Affiliation: New York University*



