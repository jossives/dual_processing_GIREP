---
title: "A02g Gender Correlations (P101 Final exam - Jan, 2018)"
author: "Joss Ives"
date: "June 7, 2018"
output:
  html_document:
    keep_md: yes
  pdf_document: default
  word_document: default
---



*updated by Joss Ives 2018 June 07, 11:41:56*

# Overview
This is a companion report for "A02 Initial Explain Your Answee Report (P101 Final exam - Jan, 2018)". In this report, correlations between the treatment and gender are examined in more detail. It has the same setup section as A02

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
## [19] "f.tot100"          "CONTROL"           "GRELEVEL"
```








# Treatment x Gender

In this section we compare making data subset for each Gender with using the TREATMENT x Gender interaction terms

### Run the regressions on the two groups individually

Female-only data first

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + final.grade.fix + (1 | QNUM) + (1 | ID)
##    Data: subset(dat.trt, Gender == "Female")
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   2049.9   2076.8  -1019.9   2039.9     1611 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -2.2436 -0.9573  0.5055  0.7934  2.4346 
## 
## Random effects:
##  Groups Name        Variance  Std.Dev. 
##  ID     (Intercept) 3.455e-14 1.859e-07
##  QNUM   (Intercept) 1.485e-01 3.854e-01
## Number of obs: 1616, groups:  ID, 402; QNUM, 4
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)      -2.0462     0.2904  -7.045 1.85e-12 ***
## TREATMENT1        0.2685     0.1064   2.523   0.0116 *  
## final.grade.fix   3.4859     0.3242  10.751  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM
## TREATMENT1  -0.198       
## finl.grd.fx -0.703  0.025
```

```
##                        Est          LL         UL
## (Intercept)      0.1292214  0.07313322  0.2283254
## TREATMENT1       1.3079709  1.06175964  1.6112760
## final.grade.fix 32.6528362 17.29545442 61.6467012
```

Male-only data

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + final.grade.fix + (1 | QNUM) + (1 | ID)
##    Data: subset(dat.trt, Gender == "Male")
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   1048.5   1073.0   -519.3   1038.5      979 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.6274 -0.7583  0.4255  0.5859  1.6886 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.0000   0.0000  
##  QNUM   (Intercept) 0.1338   0.3658  
## Number of obs: 984, groups:  ID, 246; QNUM, 4
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)      -1.9646     0.3726  -5.273 1.34e-07 ***
## TREATMENT1        0.1605     0.1535   1.046    0.296    
## final.grade.fix   4.2389     0.4576   9.263  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM
## TREATMENT1  -0.218       
## finl.grd.fx -0.822  0.021
```

```
##                       Est          LL          UL
## (Intercept)      0.140209  0.06755419   0.2910044
## TREATMENT1       1.174093  0.86905952   1.5861923
## final.grade.fix 69.330748 28.27511499 169.9994029
```

Gender effect for control condition only, controlling for question difficulty and test perfromance

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ Gender + final.grade.fix + (1 | QNUM) + (1 | ID)
##    Data: subset(dat.trt, TREATMENT == 0)
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   1564.7   1590.5   -777.3   1554.7     1295 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.0900 -0.8981  0.4519  0.7256  2.2723 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.04443  0.2108  
##  QNUM   (Intercept) 0.19198  0.4382  
## Number of obs: 1300, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)      -2.2167     0.3365  -6.588 4.46e-11 ***
## GenderMale        0.5958     0.1347   4.422 9.78e-06 ***
## final.grade.fix   3.7630     0.3901   9.646  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) GndrMl
## GenderMale  -0.062       
## finl.grd.fx -0.724 -0.087
```

```
##                        Est          LL         UL
## (Intercept)      0.1089703  0.05634971  0.2107291
## GenderMale       1.8145142  1.39337058  2.3629477
## final.grade.fix 43.0770297 20.05244705 92.5388551
```

Gender effect for treatment condition only, controlling for question difficulty and test performance

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ Gender + final.grade.fix + (1 | QNUM) + (1 | ID)
##    Data: subset(dat.trt, TREATMENT == 1)
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   1537.3   1563.2   -763.7   1527.3     1295 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.0714 -0.9446  0.4659  0.6817  2.1944 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.09722  0.3118  
##  QNUM   (Intercept) 0.08945  0.2991  
## Number of obs: 1300, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)      -1.9530     0.2966  -6.585 4.54e-11 ***
## GenderMale        0.4740     0.1381   3.432 0.000599 ***
## final.grade.fix   3.7767     0.3985   9.477  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) GndrMl
## GenderMale  -0.058       
## finl.grd.fx -0.821 -0.101
```

```
##                        Est          LL         UL
## (Intercept)      0.1418534  0.07932385  0.2536739
## GenderMale       1.6064248  1.22547491  2.1057963
## final.grade.fix 43.6709021 19.99778254 95.3679580
```

### Run the regressions on the entire data set with TREATMENT x Gender interaction term

First run with Gender=Female and TREATMENT=Control as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT * Gender + final.grade.fix + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3088.9   3129.9  -1537.4   3074.9     2593 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.3553 -0.9291  0.4659  0.7041  2.5013 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.000    0.0000  
##  QNUM   (Intercept) 0.141    0.3755  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                       Estimate Std. Error z value Pr(>|z|)    
## (Intercept)            -2.2064     0.2619  -8.425  < 2e-16 ***
## TREATMENT1              0.2700     0.1069   2.527   0.0115 *  
## GenderMale              0.5788     0.1302   4.444 8.82e-06 ***
## final.grade.fix         3.7416     0.2647  14.135  < 2e-16 ***
## TREATMENT1:GenderMale  -0.1149     0.1857  -0.618   0.5362    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATMENT1 GndrMl fnl.g.
## TREATMENT1  -0.214                         
## GenderMale  -0.109  0.404                  
## finl.grd.fx -0.636  0.021     -0.088       
## TREATMENT1:  0.118 -0.576     -0.695 -0.003
```

```
##                              Est          LL         UL
## (Intercept)            0.1100948  0.06589364  0.1839459
## TREATMENT1             1.3099603  1.06242436  1.6151699
## GenderMale             1.7839230  1.38201987  2.3027031
## final.grade.fix       42.1643213 25.09685022 70.8387697
## TREATMENT1:GenderMale  0.8914947  0.61950686  1.2828958
```

Then run with Gender=Male and TREATMENT=Control as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT * GRELEVEL + final.grade.fix + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3088.9   3129.9  -1537.4   3074.9     2593 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.3553 -0.9291  0.4659  0.7041  2.5013 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.000    0.0000  
##  QNUM   (Intercept) 0.141    0.3755  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                           Estimate Std. Error z value Pr(>|z|)    
## (Intercept)                -1.6276     0.2795  -5.823 5.79e-09 ***
## TREATMENT1                  0.1551     0.1518   1.022    0.307    
## GRELEVELFemale             -0.5788     0.1302  -4.444 8.82e-06 ***
## final.grade.fix             3.7416     0.2647  14.134  < 2e-16 ***
## TREATMENT1:GRELEVELFemale   0.1149     0.1857   0.619    0.536    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATMENT1 GRELEV fnl.g.
## TREATMENT1  -0.270                         
## GRELEVELFml -0.364  0.566                  
## finl.grd.fx -0.637  0.010      0.088       
## TREATMENT1:  0.213 -0.818     -0.695  0.003
```

```
##                                  Est         LL         UL
## (Intercept)                0.1964011  0.1135562  0.3396853
## TREATMENT1                 1.1678199  0.8672156  1.5726232
## GRELEVELFemale             0.5605612  0.4342706  0.7235786
## final.grade.fix           42.1643382 25.0963156 70.8403354
## TREATMENT1:GRELEVELFemale  1.1217146  0.7794870  1.6141945
```


Then run with Gender=Male and TREATMENT=Treatment as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ CONTROL * GRELEVEL + final.grade.fix + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3088.9   3129.9  -1537.4   3074.9     2593 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.3553 -0.9291  0.4659  0.7041  2.5013 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.000    0.0000  
##  QNUM   (Intercept) 0.141    0.3755  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                         Estimate Std. Error z value Pr(>|z|)    
## (Intercept)              -1.4725     0.2798  -5.263 1.42e-07 ***
## CONTROL1                 -0.1551     0.1518  -1.022 0.306895    
## GRELEVELFemale           -0.4640     0.1335  -3.475 0.000511 ***
## final.grade.fix           3.7416     0.2647  14.134  < 2e-16 ***
## CONTROL1:GRELEVELFemale  -0.1149     0.1857  -0.619 0.536231    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) CONTROL1 GRELEV fnl.g.
## CONTROL1    -0.273                       
## GRELEVELFml -0.376  0.586                
## finl.grd.fx -0.630 -0.010    0.091       
## CONTROL1:GR  0.231 -0.818   -0.713 -0.003
```

```
##                                Est         LL         UL
## (Intercept)              0.2293609  0.1325474  0.3968877
## CONTROL1                 0.8562958  0.6358852  1.1531052
## GRELEVELFemale           0.6287900  0.4840124  0.8168734
## final.grade.fix         42.1642954 25.0966237 70.8393219
## CONTROL1:GRELEVELFemale  0.8914928  0.6195108  1.2828821
```

And then for completion run with Gender=Female and TREATMENT=Treatment as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ CONTROL * Gender + final.grade.fix + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3088.9   3129.9  -1537.4   3074.9     2593 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.3553 -0.9291  0.4659  0.7041  2.5013 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.000    0.0000  
##  QNUM   (Intercept) 0.141    0.3755  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                     Estimate Std. Error z value Pr(>|z|)    
## (Intercept)          -1.9364     0.2608  -7.425 1.13e-13 ***
## CONTROL1             -0.2700     0.1069  -2.527 0.011515 *  
## GenderMale            0.4640     0.1335   3.475 0.000511 ***
## final.grade.fix       3.7416     0.2647  14.134  < 2e-16 ***
## CONTROL1:GenderMale   0.1149     0.1857   0.619 0.536242    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) CONTROL1 GndrMl fnl.g.
## CONTROL1    -0.195                       
## GenderMale  -0.109  0.407                
## finl.grd.fx -0.630 -0.021   -0.091       
## CONTROL1:GM  0.118 -0.576   -0.713  0.003
```

```
##                            Est          LL         UL
## (Intercept)          0.1442198  0.08650373  0.2404444
## CONTROL1             0.7633818  0.61913030  0.9412425
## GenderMale           1.5903575  1.22417843  2.0660688
## final.grade.fix     42.1643590 25.09669828 70.8393251
## CONTROL1:GenderMale  1.1217128  0.77948923  1.6141847
```

### Summary of results

_Format table in markdown instead of R for fun_

None of the cross terms were statistically significant

| ODDS RATIOS [95%CI] | Data Subset           | Interaction Term  |
| ------------- |------------|-----|
| Treatment (Female) | 1.308&ast; [1.062, 1.611] | 1.31&ast; [1.062, 1.615] |
| Treatment (Male) | 1.174 [0.869, 1.586]  |1.168 [0.867, 1.573] |
| Gender (Control) | 1.815&ast;&ast;&ast; [1.393, 2.363]      | 1.784&ast;&ast;&ast; [1.382, 2.303] |
| Gender (Treatment) | 1.606&ast;&ast;&ast; [1.225, 2.106]      | 1.59&ast;&ast;&ast; [1.224, 2.066] |



