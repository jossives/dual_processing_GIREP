# This project

This project has two purposes. 
1. To try to get a better handle on the OSF <=>  GitHub <=> RStudio work environment
1. To perform analysis for the Explain Your Answer poster at GIREP 2018

# The main steps

1. __dual_processing_raw_data_prep.Rmd__: The raw data, stored on OwnCloud are combined and anonymized.
1. __python/convert_to_logistic_regression_gradebook.py__: Pandas is used to create the logistic regression input data file. Because I can already do it quickly using Pandas, I used it to convert the anonymized gradebook to one that is appropriate for running logistic regressions and the like

# Data Prep

### P01

Process each file to the point that it is ready to be converted to logistic regression format (in Python)

### P02 

One (or more) file(s) to convert data to logistic regression format

### P03

Some final data prep, to calculate for example corrected exam averages, z scores, etc so that these do not have to be redone in every analysis file. All exams are combined into a single data file

# Analyses

### Todo
1. Bring in the other EYA data (P101 MT, Fall P100 MT & Final, older courses). Need to consider how to deal with students where we have 4 measurements (P100 students that took P101)
1. Figure out how best to combine these data into a single result (meta-analysis stylee is likely)

### A01 

Perform logistic analysis on final exam EYA data. Look at how inclusing all of the questions, the total score or other additional variables influences results.

Interesting findings:
1. Questions 6 and 10 disagreee at the 68% level when looked at as bar graphs
1. A logistic regression on this 4 question data set gives an odds ratio of 1.28 (d=0.12) and Fisher's Exact Test gives 1.24 for the effect of treatment over control
1. Played around with some other ways to look at the data, such as treating question number as a random effect, and including all of the other questions. None of these had a significant impact on the effect of TREATMENT.
1. Looking at the number of CRT questions answered correctly, we see that those scoring 2/3 are the only ones with a 68%CI difference between treatment and control. 
1. Looking at final exam grades (divided into LMH), L and H are the ones that see a difference due to treatment at the 68%CI level. 
1. There's a significant difference between how the treatment affects males and females. Doing logistic regressions on the individual populations gives treatment Odds for females is 1.33** (1.08, 1.64) and Odds for males 1.20ns (0.88, 1.62). The population is approximately 2:1 F:M.
1. We can also look at it with a TREATMENTxGender interaction term and see the same thing. The treatment is significant for females 1.33** (1.08, 1.65) (almost identical to before), and the odds ratio associated with male vs female is 2.33.
1. Controlling for final exam score (outside of the question in question) make almost no change to the treatment odds for females: 1.32** (1.07, 1.63). However, it makes a significant impact on the gender odds ratio with male vs female going down to 1.74.

### A02 Initial Explain Your Answer Report (P101 Final exam - Jan, 2018)

Establishes the analyses to perform with the other (P100, etc) data sets in order to look at the effect of treatment. It establishes that final exam grade and course grade are good predictors to control for in order to improve the model. Even after controlling for performance, gender matters. How this (and correlations with CRT score) are going to be analyzed will be pursued in A02g (gender) and A02c (CRT)

* A02g Gender correlations - Establishes how we will look for the gender correleations in subsequent data sets
* A02c NCRT correlations - Establishes how we look at NCRT correlations. In this case we see treatment effect on high CRT scores, but not low
* A02gn Gender correlations with NCRT split as an additional predictor - Nothing significant changes from A02g
* A02g2 Gender correlations with course grade - swapping in course grade instead of final exam grade. No significant differences as expected

### A03 Repeating the A02 analysis with the P100 Sept, 2017 Final Exam

No effect for this data set

### A04 Combining four tests (P100/101 from 2017-2018)

In preparing this data set, I can see that we want to have all four tests processed individually, including how they are loaded into the Axx analysis scripts. However, they will be combined into a single data file within the script

### A04c 

Looking at CRT. Adding CRT.medsplit and ExamGrade.fix.LMH in the processing of the data files when opened.

### A04g

Looking at the possible differences in gender actions

# Todo

Some analyses to perform
* Question difficulty vs Odds ratio
* Median split on exam scores...see if crt.split x exam.split means/shows anything

