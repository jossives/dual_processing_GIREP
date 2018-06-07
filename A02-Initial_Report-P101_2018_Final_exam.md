---
title: "A02x"
author: "Joss Ives"
date: "June 7, 2018"
output:
  html_document:
    keep_md: yes
  pdf_document: default
  word_document: default
---



*updated by Joss Ives 2018 June 07, 09:17:22*

# Overview
This report discusses the initial analysis of the W2017T2 data from the Physics 101 course. In this course, 4 questions were used to look at the effect of asking students to explain their answer after a multiple-choice question. This used a crossover protocol, where there were 2 versions of the test and each version had 2 explain your answer questions that the other group did not. 

# Setup


```
## Loading required package: Matrix
```

```
## Loading required package: xts
```

```
## Loading required package: zoo
```

```
## 
## Attaching package: 'zoo'
```

```
## The following objects are masked from 'package:base':
## 
##     as.Date, as.Date.numeric
```

```
## 
## Attaching package: 'PerformanceAnalytics'
```

```
## The following object is masked from 'package:graphics':
## 
##     legend
```

```
## 
## Attaching package: 'dplyr'
```

```
## The following objects are masked from 'package:xts':
## 
##     first, last
```

```
## The following objects are masked from 'package:plyr':
## 
##     arrange, count, desc, failwith, id, mutate, rename, summarise,
##     summarize
```

```
## The following objects are masked from 'package:stats':
## 
##     filter, lag
```

```
## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union
```


### Add additional calculated values

The following is a summary of the variables present in the data file. The final 4 were caculated in this notebook. "Fix" refers to removing from the overall score on the test, the score of the specific question.

```r
names(dat.raw)
```

```
##  [1] "ID"                "QNUM"              "QCORRECT"         
##  [4] "TREATMENT"         "f.Atot40"          "f.Btot38"         
##  [7] "f.tot78"           "course.grade"      "d.version"        
## [10] "f.version"         "NCRT"              "Gender"           
## [13] "EYAfinal"          "course.grade.frac" "CRT.medsplit"     
## [16] "final.grade.LMH"   "final.grade.fix"   "final.gradeA.fix" 
## [19] "f.tot100"
```









```r
#dat.trt
```


# Data description








### How well was each question answered?

Note that Final Exam V1 had questions 5 & 9 as treatment and V2 had questions 6 & 10 as treatment. Thus both of the questions where we are seeing a difference are from the same version. We need to confirm that these two populations are not performing differently overall. This is likely done most effectively by controlling for version, gender and other differences within the logistic regression. There are too many confounding factors to be able to see through them using bar charts.


```
##   TREATMENT QNUM   N  QCORRECT median        sd         se         ci
## 1         0    5 323 0.6904025      1 0.4630450 0.02576452 0.05068804
## 2         0    6 327 0.4740061      0 0.5000891 0.02765499 0.05440477
## 3         0    9 323 0.7027864      1 0.4577405 0.02546936 0.05010737
## 4         0   10 327 0.5596330      1 0.4971920 0.02749478 0.05408959
## 5         1    5 327 0.7155963      1 0.4518213 0.02498578 0.04915371
## 6         1    6 323 0.5665635      1 0.4963184 0.02761589 0.05433037
## 7         1    9 327 0.7064220      1 0.4560988 0.02522232 0.04961905
## 8         1   10 323 0.6284830      1 0.4839600 0.02692825 0.05297753
##   binomial.error
## 1     0.02572460
## 2     0.02761267
## 3     0.02542991
## 4     0.02745271
## 5     0.02494754
## 6     0.02757311
## 7     0.02518373
## 8     0.02688654
```


![](A02-Initial_Report-P101_2018_Final_exam_files/figure-html/unnamed-chunk-12-1.png)<!-- -->


### Performance on the EYA questions by gender.
It looks like females benefit from the intervention more than males, but since the effective intervention questions were both on the same test, we need to confirm that this is not partially explained by there being a large gender difference in who wrote which test.
![](A02-Initial_Report-P101_2018_Final_exam_files/figure-html/unnamed-chunk-13-1.png)<!-- -->
### Overall final exam grades show that the males outperformed the females
Looking at final exam performance by gender and by test version. The effect looks the opposite of what we would expect from the Test 2 intervention questions being the more effective ones. Females benefit more from the intervention. However, their score on V2 as compared to V1 is worse than the males, not better. However, the effect of the intervention on overall test grade is 0.25% (approximately 5% per question, each worth approximately 5% of the test).

![](A02-Initial_Report-P101_2018_Final_exam_files/figure-html/unnamed-chunk-14-1.png)<!-- -->
### Effect of intervention by final exam performance group (tertile)
Since we know that females scored lower on the final exam than males, perhaps there will be a difference in the effectiveness of the intervention if we look at low, medium and high performers from the final exam. The graph shows no significant difference.

![](A02-Initial_Report-P101_2018_Final_exam_files/figure-html/unnamed-chunk-15-1.png)<!-- -->

### Intervention effectiveness by CRT score

Spurrious correlation? The CRT scores of 2/3 are the ones where we see the difference between treatment and control.

**TODO:** Have to check this with midterm data, data from last time we did the CRT and question pair data.

![](A02-Initial_Report-P101_2018_Final_exam_files/figure-html/unnamed-chunk-16-1.png)<!-- -->



### No difference in gender fractions taking each version of the test



![](A02-Initial_Report-P101_2018_Final_exam_files/figure-html/unnamed-chunk-17-1.png)<!-- -->

# Quick analyses show effect size of d=0.13

### Fisher's Exact for the four study questions combined

This is a sanity check for the logistic regressions to come. Overall we see an effect size of d=0.11, which is small, but maybe larger than one would expect from this type of intervention.


```
## 
## 	Fisher's Exact Test for Count Data
## 
## data:  ctable
## p-value = 0.01175
## alternative hypothesis: true odds ratio is not equal to 1
## 95 percent confidence interval:
##  1.046481 1.449223
## sample estimates:
## odds ratio 
##   1.231373
```


### Simple logistic regression


```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + (1 | QNUM) + (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3326.8   3350.2  -1659.4   3318.8     2596 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -1.8195 -0.9960  0.5496  0.7031  1.3524 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.6073   0.7793  
##  QNUM   (Intercept) 0.1339   0.3659  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##             Estimate Std. Error z value Pr(>|z|)   
## (Intercept)  0.50579    0.19557   2.586  0.00970 **
## TREATMENT1   0.23516    0.08738   2.691  0.00712 **
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##            (Intr)
## TREATMENT1 -0.215
```

```
##                  Est       LL       UL
## (Intercept) 1.658292 1.130296 2.432931
## TREATMENT1  1.265117 1.065985 1.501449
```



```
##   Model.vars AIC.val Odds.treatment  LL  UL Significant.Vars
## 1     Simple  3326.8          1.265 1.1 1.5             None
```



### A quick summary of odds ratios so far

```r
odds.table <- matrix(c(
  f.result$estimate[[1]],
  cohens.d.from.odds.simple(f.result$estimate[[1]]),
  exp(tab[[2]]),
  cohens.d.from.odds.simple(exp(tab[[2]]))
),ncol=2,byrow=TRUE)
colnames(odds.table) <- c("Odds Ratio","Cohen's d")
rownames(odds.table) <- c("Fisher's Exact Test","Logistic Regression")
as.table(odds.table)
```

```
##                     Odds Ratio Cohen's d
## Fisher's Exact Test  1.2313726 0.1147478
## Logistic Regression  1.2651171 0.1296531
```

```r
#cat("Cohen's d\n ", cohens.d.from.odds.simple(result$estimate[[1]]),"\n")
```

# Other non-interaction models

### Treatment + Gender


```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + Gender + (1 | QNUM) + (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3272.7   3302.0  -1631.3   3262.7     2595 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -2.1731 -0.9376  0.5215  0.6996  1.4394 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.4748   0.6891  
##  QNUM   (Intercept) 0.1356   0.3682  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##             Estimate Std. Error z value Pr(>|z|)    
## (Intercept)  0.19889    0.19959   0.996  0.31903    
## TREATMENT1   0.23715    0.08753   2.709  0.00674 ** 
## GenderMale   0.81702    0.10958   7.456  8.9e-14 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##            (Intr) TREATM
## TREATMENT1 -0.216       
## GenderMale -0.186  0.023
```

```
##                  Est        LL       UL
## (Intercept) 1.220043 0.8250429 1.804154
## TREATMENT1  1.267635 1.0677905 1.504883
## GenderMale  2.263753 1.8262344 2.806091
```

### Treatment + overall course grade


```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + course.grade.frac + (1 | QNUM) + (1 |  
##     ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3075.2   3104.5  -1532.6   3065.2     2595 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -2.8294 -0.9198  0.4643  0.6755  2.2846 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.1054   0.3247  
##  QNUM   (Intercept) 0.1413   0.3759  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                   Estimate Std. Error z value Pr(>|z|)    
## (Intercept)       -3.89425    0.34592 -11.258  < 2e-16 ***
## TREATMENT1         0.23100    0.08852   2.609  0.00907 ** 
## course.grade.frac  5.91422    0.39022  15.156  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM
## TREATMENT1  -0.150       
## crs.grd.frc -0.819  0.032
```

```
##                            Est           LL           UL
## (Intercept)         0.02035858   0.01033467   0.04010498
## TREATMENT1          1.25985422   1.05917839   1.49855084
## course.grade.frac 370.26686889 172.32809322 795.56125547
```

### Treatment + Test Version


```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + f.version + (1 | QNUM) + (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3326.8   3356.1  -1658.4   3316.8     2595 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -1.7693 -0.9905  0.5593  0.6873  1.3804 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.6031   0.7766  
##  QNUM   (Intercept) 0.1331   0.3648  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##             Estimate Std. Error z value Pr(>|z|)   
## (Intercept)  0.43360    0.20155   2.151  0.03145 * 
## TREATMENT1   0.22796    0.08748   2.606  0.00917 **
## f.version2   0.15137    0.10683   1.417  0.15652   
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##            (Intr) TREATM
## TREATMENT1 -0.199       
## f.version2 -0.251 -0.045
```

```
##                  Est        LL       UL
## (Intercept) 1.542806 1.0393157 2.290208
## TREATMENT1  1.256037 1.0581207 1.490974
## f.version2  1.163429 0.9436278 1.434429
```

### TREATMENT + Final Exam Grade (corrected for intervention question scores)


```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + final.grade.fix + (1 | QNUM) + (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3116.9   3146.3  -1553.5   3106.9     2595 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -2.9816 -0.9543  0.4777  0.7077  2.4355 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.0000   0.0000  
##  QNUM   (Intercept) 0.1368   0.3699  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)     -2.15808    0.25741  -8.384  < 2e-16 ***
## TREATMENT1       0.22800    0.08683   2.626  0.00864 ** 
## final.grade.fix  3.98093    0.26141  15.229  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM
## TREATMENT1  -0.181       
## finl.grd.fx -0.654  0.025
```

```
##                        Est          LL         UL
## (Intercept)      0.1155463  0.06976559  0.1913688
## TREATMENT1       1.2560793  1.05951439  1.4891115
## final.grade.fix 53.5670463 32.09099162 89.4153876
```

### TREATMENT + Final Exam Grade Tertile


```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + final.grade.LMH + (1 | QNUM) + (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3052.5   3081.9  -1521.3   3042.5     2595 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -2.8041 -0.9277  0.4026  0.6437  1.6497 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.05587  0.2364  
##  QNUM   (Intercept) 0.14151  0.3762  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)     -1.42685    0.22737  -6.275 3.49e-10 ***
## TREATMENT1       0.23317    0.08848   2.635   0.0084 ** 
## final.grade.LMH  0.97677    0.06072  16.087  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM
## TREATMENT1  -0.209       
## fnl.grd.LMH -0.489  0.038
```

```
##                       Est        LL        UL
## (Intercept)     0.2400634 0.1537389 0.3748591
## TREATMENT1      1.2625969 1.0615766 1.5016825
## final.grade.LMH 2.6558610 2.3578731 2.9915085
```

### Treatment + number of CRT questions correct


```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + NCRT + (1 | QNUM) + (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3202.9   3232.2  -1596.5   3192.9     2595 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -2.2440 -0.9410  0.5031  0.6793  1.5782 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.3263   0.5713  
##  QNUM   (Intercept) 0.1375   0.3708  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##             Estimate Std. Error z value Pr(>|z|)    
## (Intercept) -0.47881    0.21377   -2.24  0.02510 *  
## TREATMENT1   0.23534    0.08781    2.68  0.00736 ** 
## NCRT         0.52052    0.04689   11.10  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##            (Intr) TREATM
## TREATMENT1 -0.211       
## NCRT       -0.390  0.030
```

```
##                   Est        LL        UL
## (Intercept) 0.6195198 0.4074682 0.9419257
## TREATMENT1  1.2653336 1.0652647 1.5029778
## NCRT        1.6829033 1.5351395 1.8448900
```

### TREATMENT + Final Exam Part A Grade (corrected for intervention question scores)


```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + final.gradeA.fix + (1 | QNUM) + (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3153.9   3183.2  -1571.9   3143.9     2595 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -2.9023 -0.9744  0.5087  0.7209  2.3399 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.0000   0.000   
##  QNUM   (Intercept) 0.1377   0.371   
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                  Estimate Std. Error z value Pr(>|z|)    
## (Intercept)      -1.79148    0.24913  -7.191 6.44e-13 ***
## TREATMENT1        0.23123    0.08618   2.683  0.00729 ** 
## final.gradeA.fix  3.48410    0.24512  14.214  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM
## TREATMENT1  -0.186       
## fnl.grdA.fx -0.622  0.028
```

```
##                         Est         LL         UL
## (Intercept)       0.1667133  0.1023072  0.2716654
## TREATMENT1        1.2601543  1.0643001  1.4920498
## final.gradeA.fix 32.5931935 20.1593805 52.6958785
```

### TREATMENT + Gender + Final Exam Grade (corrected for intervention question scores)


```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + Gender + final.grade.fix + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3087.3   3122.4  -1537.6   3075.3     2594 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.4212 -0.9272  0.4654  0.7062  2.5242 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.0000   0.0000  
##  QNUM   (Intercept) 0.1403   0.3746  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)     -2.18770    0.25975  -8.422  < 2e-16 ***
## TREATMENT1       0.23200    0.08738   2.655  0.00793 ** 
## GenderMale       0.52307    0.09367   5.584 2.35e-08 ***
## final.grade.fix  3.74161    0.26475  14.133  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM GndrMl
## TREATMENT1  -0.181              
## GenderMale  -0.039  0.014       
## finl.grd.fx -0.640  0.023 -0.126
```

```
##                        Est          LL         UL
## (Intercept)      0.1121746  0.06742042  0.1866371
## TREATMENT1       1.2611210  1.06262270  1.4966988
## GenderMale       1.6872076  1.40421111  2.0272376
## final.grade.fix 42.1657635 25.09571670 70.8468154
```

### TREATMENT + Gender + Overall Course Grade


```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + Gender + course.grade.frac + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3041.9   3077.1  -1514.9   3029.9     2594 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.3221 -0.9011  0.4490  0.6843  2.4737 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.04731  0.2175  
##  QNUM   (Intercept) 0.14232  0.3773  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                   Estimate Std. Error z value Pr(>|z|)    
## (Intercept)       -3.85120    0.34072 -11.303  < 2e-16 ***
## TREATMENT1         0.23249    0.08868   2.622  0.00875 ** 
## GenderMale         0.57229    0.09668   5.920 3.22e-09 ***
## course.grade.frac  5.57152    0.38128  14.613  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM GndrMl
## TREATMENT1  -0.151              
## GenderMale  -0.048  0.017       
## crs.grd.frc -0.807  0.029 -0.055
```

```
##                            Est           LL           UL
## (Intercept)         0.02125415   0.01089966   0.04144523
## TREATMENT1          1.26174076   1.06042843   1.50127034
## GenderMale          1.77232698   1.46639861   2.14207984
## course.grade.frac 262.83289872 124.48748635 554.92431149
```

### Results

Gender is a significant predictor and will be investigated further. Final exam grade (corrected for scores on intervention questions) and course grade are both good controls, but how good may depend on the course. NCRT and Gender will be investigated further in terms of interaction terms with other variables.

The best baseline model is 

  QCORRECT ~ TREATMENT + Gender + course.grade.frac + (1|QNUM) + (1|ID)

or

  QCORRECT ~ TREATMENT + Gender + final.grade.fix + (1|QNUM) + (1|ID)
  
Adding NCRT would improve the model further, but we do not always have access to this quantity so will pursue it only if it is an investigation of CRT score, not when it is only helping to improve the model.


```r
r.df
```

```
##               Model.vars AIC.val Odds.treatment    LL    UL
## 1                 Simple  3326.8          1.265   1.1   1.5
## 2                 Gender  3272.7          1.268 1.068 1.505
## 3           Course grade  3075.2           1.26 1.059 1.499
## 4           Test Version  3326.8          1.256 1.058 1.491
## 5       Final Exam Grade  3116.9          1.256  1.06 1.489
## 6         Final Exam LMH  3052.5          1.263 1.062 1.502
## 7                   NCRT  3202.9          1.265 1.065 1.503
## 8      Final Exam Part A  3153.9           1.26 1.064 1.492
## 9    Gender + Exam Grade  3087.3          1.261 1.063 1.497
## 10 Gender + Course Grade  3041.9          1.262  1.06 1.501
##              Significant.Vars
## 1                        None
## 2                   ***Gender
## 3             ***Course grade
## 4                        None
## 5         ***Final Exam Grade
## 6           ***Final Exam LMH
## 7                     ***NCRT
## 8        ***Final Exam Part A
## 9    ***Gender, ***Exam Grade
## 10 ***Gender, ***Course Grade
```
