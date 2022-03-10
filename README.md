# DSC 180 Section B14 Project

## Project Introduction
In an effort to reduce app wait time, the time it takes for an application to launch, we collected data on application use and app wait time for a single user over several weeks. With this data we plan to build a series of models to predict which application a user will open with an emphasis on when and for how long. The focus is currently on our foreground app data which shows us which app is in the foreground of the user’s computer with timestamp. Using this data, we created a single chain Hidden Markov Model (HMM) to predict the next app the user opens based on their current one. With not enough amount of layers, we implemented a Long Short-Term Memory (LSTM) model to predict the amount of time a user will use an application.

## Overview
We collected foreground windows with our data collection library for 2 months on a Windows laptop. The Jupyter Notebook contains the code to read in and combine each database file, data cleaning/preprocessing, the HMM model, and the LSTM model. The run.py file is a streamline version of our notebook that reads in the files, creates a Hidden Markov Model, and outputs prediction on every unique application that was present in our data collection.

## How to Use
1. Pull the repo to obtain all necessary files to run test
2. With a terminal, navigate onto overarching folder (dsc180-data-analysis)
3. Run the command: 
```
python run.py test
```
4. When finished, the terminal should report an accuracy of the model and outputs all possible predictions onto outputs/outputs.txt

## More Information
For more information, please read our report, the pdf file on the repository, for a more in depth explanation of the process.

A visual presentation can also be viewed here: https://www.youtube.com/watch?v=2h5k6alz3WU
(note that to retrieve the most amount of information, please view the report, as the video only provides a summary of our process)
