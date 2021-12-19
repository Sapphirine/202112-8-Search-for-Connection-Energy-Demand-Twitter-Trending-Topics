# Energy Demand and Twitter Analysis

Use Big Data Analytics to investigate the relationship between electricity load energy demand and Twitter activity

Group: 
Kevin Mark Murning (kmm2344)
Rifqi Luthfan (rl3154)
Rohan Raghuraman (rr3417)

# Project Description

Effective energy demand forecasting plays a vital role in power systems, especially in resource allocation and economically viable pricing. 
Some trends are easy to infer, for example an increase in demand in winter months due to use of heating. 
However, outlier events can cause spikes in demand that are hard to predict. How can we predict anomalous changes in demand? 
Much work has been done on monitoring social media for time series forecasting but very little has been done in the energy sector.

Our Question: _Can Twitter activity formulated into topics be linked in a causal relationship with energy demand spikes?_

# How to Setup

# Repository Content

## Solution Diagram
![overall_dag](./figures/overall_dag.png)

## Datasets

1. Time-series electricity load data from NYISO (web scraping from http://dss.nyiso.com/dss_oasis/PublicReports)
    1. Across 15 regions in NY state
    2. 5-mins granularity
    3. From 01/01/2010 to 12/31/2020 for training, 01/01/2021 to 10/31/2021 for validation
2. Forecasting data from FBProphet
    1. Produces energy demand prediction
    2. Using historical comparison we will identify anomalous dates
3. Streamed Twitter data (needs Twitter Full Archive Search API approval)
    1. Region-level top/trending tweets with timestamps
    2. Includes pictures/videos, likes and retweets

## Notebooks

1. 00-data-collection-electricity_load.ipynb
2. 10-modelling-fbprophet.ipynb
3. 11-evaluate-model.ipynb
4. 12-forecast_results_charts.ipynb
5. GET_Tweets.ipynb in "Full Archive Tweets Search" folder

## Source Codes

### LDA

### Web Dashboard

