# This project

This project has two purposes. 
1. To try to get a better handle on the OSF <=>  GitHub <=> RStudio work environment
1. To perform analysis for the Explain Your Answer poster at GIREP 2018

# The main steps

1. __dual_processing_raw_data_prep.Rmd__: The raw data, stored on OwnCloud are combined and anonymized.
1. __python/convert_to_logistic_regression_gradebook.py__: Pandas is used to create the logistic regression input data file. Because I can already do it quickly using Pandas, I used it to convert the anonymized gradebook to one that is appropriate for running logistic regressions and the like

# Analyses

### Todo
1. There are 24 data points with the treatment variable not set, need to look into these
1. Produce a report based on A01. Discuss odds ratio + effect size, lack of correlations with CRT, and the fact there seems to be a significant gender effect with the intervention. This report should also have some clearly stated research questions based on these initial findings.
1. Bring in the other EYA data (P101 MT, Fall P100 MT & Final, older courses). Need to consider how to deal with students where we have 4 measurements (P100 students that took P101)
1. Figure out how best to combine these data into a single result (meta-analysis stylee is likely)

### A01 

Perform logistic analysis on final exam EYA data. Look at how inclusing all of the questions, the total score or other additional variables influences results.

Interesting findings:
1. 
