# DSC 180 Section B14 Project

## Project Introduction
In an effort to reduce app wait time, the time it takes for an application to launch, we collected data on application use and app wait time for a single user over several weeks. With this data we plan to build a series of models to predict which application a user will open with an emphasis on when and for how long. The focus is currently on our foreground app data which shows us which app is in the foreground of the user’s computer with timestamp. So far, we have finished data collection, cleaned and explored the data, and created a single chain Hidden Markov Model (HMM) to predict the next app the user opens based on their current one.

## Overview
After finishing up our data collection libraries, we put them to the test and started recording the foreground windows and their use time whenever we were active on our machines. When ample data was collected, we started processing the data and analyzing it using Jupyter Notebook. The Jupyter Notebook contains a very messy version of our model, but includes visualization and all of our test and validation. The run.py file is a streamline version of our notebook that reads in the files, creates a Hidden Markov Model, and outputs prediction on every unique application that was present in our data collection.

## How to Use
1. Pull the repo to obtain all necessary files to run test
2. With a terminal, navigate onto overarching folder (dsc180-data-analysis)
3. Run the command: 
```
python run.py test
```
4. When finished, the terminal should report an accuracy of the model and outputs all possible predictions onto outputs/outputs.txt
