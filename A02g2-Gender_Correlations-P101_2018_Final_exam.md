---
title: "A02g2 Gender Correlations course grade (P101 Final exam - Jan, 2018)"
author: "Joss Ives"
date: "June 7, 2018"
output:
  html_document:
    keep_md: yes
  pdf_document: default
  word_document: default
---



*updated by Joss Ives 2018 June 07, 12:40:42*

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
## Formula: QCORRECT ~ TREATMENT + course.grade.frac + (1 | QNUM) + (1 |  
##     ID)
##    Data: subset(dat.trt, Gender == "Female")
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   2020.7   2047.6  -1005.3   2010.7     1611 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -2.1003 -0.9443  0.4914  0.7551  2.4780 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.05409  0.2326  
##  QNUM   (Intercept) 0.15115  0.3888  
## Number of obs: 1616, groups:  ID, 402; QNUM, 4
## 
## Fixed effects:
##                   Estimate Std. Error z value Pr(>|z|)    
## (Intercept)        -3.6749     0.3996  -9.196   <2e-16 ***
## TREATMENT1          0.2710     0.1081   2.506   0.0122 *  
## course.grade.frac   5.3011     0.4719  11.233   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM
## TREATMENT1  -0.162       
## crs.grd.frc -0.852  0.034
```

```
##                            Est          LL           UL
## (Intercept)         0.02535302  0.01158455   0.05548558
## TREATMENT1          1.31125168  1.06079075   1.62084838
## course.grade.frac 200.56503884 79.53346215 505.77874665
```

Male-only data

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + course.grade.frac + (1 | QNUM) + (1 |  
##     ID)
##    Data: subset(dat.trt, Gender == "Male")
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   1033.1   1057.6   -511.6   1023.1      979 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.4273 -0.5939  0.4154  0.5692  1.8530 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.03522  0.1877  
##  QNUM   (Intercept) 0.13480  0.3671  
## Number of obs: 984, groups:  ID, 246; QNUM, 4
## 
## Fixed effects:
##                   Estimate Std. Error z value Pr(>|z|)    
## (Intercept)        -3.6055     0.5200  -6.934  4.1e-12 ***
## TREATMENT1          0.1567     0.1555   1.008    0.314    
## course.grade.frac   6.0545     0.6484   9.338  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM
## TREATMENT1  -0.162       
## crs.grd.frc -0.910  0.017
```

```
##                            Est           LL           UL
## (Intercept)         0.02717388 9.806676e-03 7.529767e-02
## TREATMENT1          1.16968703 8.623814e-01 1.586500e+00
## course.grade.frac 426.04420276 1.195521e+02 1.518281e+03
```

Gender effect for control condition only, controlling for question difficulty and test perfromance

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ Gender + course.grade.frac + (1 | QNUM) + (1 | ID)
##    Data: subset(dat.trt, TREATMENT == 0)
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   1533.0   1558.8   -761.5   1523.0     1295 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -2.8963 -0.8627  0.4242  0.6940  2.6698 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.1003   0.3168  
##  QNUM   (Intercept) 0.2032   0.4508  
## Number of obs: 1300, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                   Estimate Std. Error z value Pr(>|z|)    
## (Intercept)        -4.0667     0.4725  -8.606  < 2e-16 ***
## GenderMale          0.6443     0.1383   4.661 3.15e-06 ***
## course.grade.frac   5.8484     0.5670  10.315  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) GndrMl
## GenderMale  -0.076       
## crs.grd.frc -0.863 -0.019
```

```
##                            Est           LL           UL
## (Intercept)         0.01713399 6.786116e-03 4.326092e-02
## GenderMale          1.90474670 1.452623e+00 2.497592e+00
## course.grade.frac 346.69505152 1.141046e+02 1.053397e+03
```

Gender effect for treatment condition only, controlling for question difficulty and test performance

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ Gender + course.grade.frac + (1 | QNUM) + (1 | ID)
##    Data: subset(dat.trt, TREATMENT == 1)
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   1521.6   1547.4   -755.8   1511.6     1295 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -2.8594 -0.9125  0.4552  0.6531  2.0155 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.19797  0.4449  
##  QNUM   (Intercept) 0.08523  0.2919  
## Number of obs: 1300, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                   Estimate Std. Error z value Pr(>|z|)    
## (Intercept)        -3.5405     0.4368  -8.106 5.22e-16 ***
## GenderMale          0.5307     0.1420   3.738 0.000185 ***
## course.grade.frac   5.5042     0.5697   9.662  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) GndrMl
## GenderMale  -0.059       
## crs.grd.frc -0.923 -0.045
```

```
##                            Est          LL           UL
## (Intercept)         0.02899944  0.01232016   0.06825949
## GenderMale          1.70005289  1.28715689   2.24539824
## course.grade.frac 245.71922898 80.44967492 750.50569874
```

### Run the regressions on the entire data set with TREATMENT x Gender interaction term

First run with Gender=Female and TREATMENT=Control as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT * Gender + course.grade.frac + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3043.5   3084.5  -1514.7   3029.5     2593 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.2557 -0.8964  0.4489  0.6835  2.4988 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.0479   0.2189  
##  QNUM   (Intercept) 0.1431   0.3783  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                       Estimate Std. Error z value Pr(>|z|)    
## (Intercept)            -3.8710     0.3426 -11.298  < 2e-16 ***
## TREATMENT1              0.2716     0.1084   2.506   0.0122 *  
## GenderMale              0.6300     0.1335   4.718 2.38e-06 ***
## course.grade.frac       5.5723     0.3814  14.611  < 2e-16 ***
## TREATMENT1:GenderMale  -0.1187     0.1886  -0.629   0.5291    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATMENT1 GndrMl crs.g.
## TREATMENT1  -0.178                         
## GenderMale  -0.100  0.402                  
## crs.grd.frc -0.803  0.029     -0.034       
## TREATMENT1:  0.096 -0.575     -0.690 -0.008
```

```
##                                Est           LL          UL
## (Intercept)             0.02083816   0.01064636   0.0407866
## TREATMENT1              1.31207396   1.06095709   1.6226274
## GenderMale              1.87751701   1.44519857   2.4391597
## course.grade.frac     263.04314993 124.56467961 555.4680424
## TREATMENT1:GenderMale   0.88809374   0.61366703   1.2852418
```

Then run with Gender=Male and TREATMENT=Control as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: 
## QCORRECT ~ TREATMENT * GRELEVEL + course.grade.frac + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3043.5   3084.5  -1514.7   3029.5     2593 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.2557 -0.8964  0.4489  0.6835  2.4988 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.0479   0.2189  
##  QNUM   (Intercept) 0.1431   0.3783  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                           Estimate Std. Error z value Pr(>|z|)    
## (Intercept)                -3.2410     0.3550  -9.129  < 2e-16 ***
## TREATMENT1                  0.1529     0.1543   0.991    0.322    
## GRELEVELFemale             -0.6299     0.1335  -4.718 2.38e-06 ***
## course.grade.frac           5.5723     0.3814  14.611  < 2e-16 ***
## TREATMENT1:GRELEVELFemale   0.1187     0.1886   0.629    0.529    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATMENT1 GRELEV crs.g.
## TREATMENT1  -0.218                         
## GRELEVELFml -0.279  0.561                  
## crs.grd.frc -0.788  0.010      0.034       
## TREATMENT1:  0.167 -0.818     -0.690  0.008
```

```
##                                   Est           LL           UL
## (Intercept)                 0.0391240   0.01950906   0.07846034
## TREATMENT1                  1.1652459   0.86113990   1.57674511
## GRELEVELFemale              0.5326186   0.40997838   0.69194511
## course.grade.frac         263.0432564 124.56049595 555.48714853
## TREATMENT1:GRELEVELFemale   1.1260063   0.77806824   1.62953605
```


Then run with Gender=Male and TREATMENT=Treatment as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ CONTROL * GRELEVEL + course.grade.frac + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3043.5   3084.5  -1514.7   3029.5     2593 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.2557 -0.8964  0.4489  0.6835  2.4988 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.0479   0.2189  
##  QNUM   (Intercept) 0.1431   0.3783  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                         Estimate Std. Error z value Pr(>|z|)    
## (Intercept)              -3.0881     0.3548  -8.703  < 2e-16 ***
## CONTROL1                 -0.1529     0.1543  -0.991 0.321628    
## GRELEVELFemale           -0.5113     0.1366  -3.744 0.000181 ***
## course.grade.frac         5.5723     0.3814  14.612  < 2e-16 ***
## CONTROL1:GRELEVELFemale  -0.1187     0.1886  -0.629 0.529136    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) CONTROL1 GRELEV crs.g.
## CONTROL1    -0.216                       
## GRELEVELFml -0.295  0.582                
## crs.grd.frc -0.784 -0.010    0.045       
## CONTROL1:GR  0.189 -0.818   -0.706 -0.008
```

```
##                                  Est           LL           UL
## (Intercept)               0.04558926   0.02274114   0.09139298
## CONTROL1                  0.85818904   0.63421862   1.16125323
## GRELEVELFemale            0.59973219   0.45888278   0.78381390
## course.grade.frac       263.04176696 124.56636866 555.45466971
## CONTROL1:GRELEVELFemale   0.88809315   0.61367090   1.28523196
```

And then for completion run with Gender=Female and TREATMENT=Treatment as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ CONTROL * Gender + course.grade.frac + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3043.5   3084.5  -1514.7   3029.5     2593 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.2557 -0.8964  0.4489  0.6835  2.4988 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.0479   0.2189  
##  QNUM   (Intercept) 0.1431   0.3783  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                     Estimate Std. Error z value Pr(>|z|)    
## (Intercept)          -3.5994     0.3405 -10.571  < 2e-16 ***
## CONTROL1             -0.2716     0.1084  -2.506 0.012212 *  
## GenderMale            0.5113     0.1366   3.743 0.000181 ***
## course.grade.frac     5.5723     0.3814  14.611  < 2e-16 ***
## CONTROL1:GenderMale   0.1187     0.1886   0.629 0.529137    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) CONTROL1 GndrMl crs.g.
## CONTROL1    -0.139                       
## GenderMale  -0.093  0.401                
## crs.grd.frc -0.799 -0.028   -0.045       
## CONTROL1:GM  0.087 -0.575   -0.706  0.008
```

```
##                              Est           LL           UL
## (Intercept)           0.02734131   0.01402759   0.05329123
## CONTROL1              0.76215177   0.61628495   0.94254341
## GenderMale            1.66741095   1.27581228   2.17920717
## course.grade.frac   263.04221607 124.56434503 555.46559025
## CONTROL1:GenderMale   1.12600768   0.77806885   1.62953870
```

### Summary of results

_Format table in markdown instead of R for fun_

None of the cross terms were statistically significant

| ODDS RATIOS [95%CI] | Data Subset           | Interaction Term  |
| ------------- |------------|-----|
| Treatment (Female) | 1.311&ast; [1.061, 1.621] | 1.312&ast; [1.061, 1.623] |
| Treatment (Male) | 1.17 [0.862, 1.586]  |1.165 [0.861, 1.577] |
| Gender (Control) | 1.905&ast;&ast;&ast; [1.453, 2.498]      | 1.878&ast;&ast;&ast; [1.445, 2.439] |
| Gender (Treatment) | 1.7&ast;&ast;&ast; [1.287, 2.245]      | 1.667&ast;&ast;&ast; [1.276, 2.179] |



