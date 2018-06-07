---
title: "A02g CRT Correlations (P101 Final exam - Jan, 2018)"
author: "Joss Ives"
date: "June 7, 2018"
output:
  html_document:
    keep_md: yes
  pdf_document: default
  word_document: default
---



*updated by Joss Ives 2018 June 07, 12:23:36*

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
## [19] "f.tot100"          "CONTROL"           "CRT.medsplit.rev" 
## [22] "GRELEVEL"
```








# Treatment x CRT.medsplit

In this section we compare making data subset for each level of the CRT median split with using the TREATMENT x CRT.medsplit interaction terms

### Run the regressions on the two groups individually

Low CRT data first

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + final.grade.fix + (1 | QNUM) + (1 | ID)
##    Data: subset(dat.trt, CRT.medsplit == 0)
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   1206.5   1230.6   -598.2   1196.5      911 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -1.7074 -0.8922 -0.4745  0.9298  2.5137 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.0000   0.0000  
##  QNUM   (Intercept) 0.1834   0.4282  
## Number of obs: 916, groups:  ID, 228; QNUM, 4
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)      -1.7681     0.3423  -5.166 2.39e-07 ***
## TREATMENT1        0.1725     0.1386   1.245    0.213    
## final.grade.fix   2.7528     0.4207   6.544 5.99e-11 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM
## TREATMENT1  -0.213       
## finl.grd.fx -0.726  0.014
```

```
##                        Est         LL         UL
## (Intercept)      0.1706497 0.08724775  0.3337772
## TREATMENT1       1.1882996 0.90564663  1.5591688
## final.grade.fix 15.6859338 6.87768656 35.7748958
```

High CRT data

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + final.grade.fix + (1 | QNUM) + (1 | ID)
##    Data: subset(dat.trt, CRT.medsplit == 1)
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   1853.0   1880.1   -921.5   1843.0     1679 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.5670 -0.8901  0.4451  0.6209  1.9233 
## 
## Random effects:
##  Groups Name        Variance  Std.Dev. 
##  ID     (Intercept) 4.752e-17 6.893e-09
##  QNUM   (Intercept) 2.084e-01 4.565e-01
## Number of obs: 1684, groups:  ID, 420; QNUM, 4
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)      -1.9907     0.3426   -5.81 6.26e-09 ***
## TREATMENT1        0.2860     0.1144    2.50   0.0124 *  
## final.grade.fix   4.0380     0.3598   11.22  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM
## TREATMENT1  -0.178       
## finl.grd.fx -0.709  0.027
```

```
##                        Est          LL          UL
## (Intercept)      0.1366045  0.06979153   0.2673788
## TREATMENT1       1.3311383  1.06374968   1.6657388
## final.grade.fix 56.7123397 28.01703628 114.7976340
```

CRT effect for control condition only, controlling for question difficulty and test perfromance

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ CRT.medsplit + final.grade.fix + (1 | QNUM) + (1 |  
##     ID)
##    Data: subset(dat.trt, TREATMENT == 0)
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   1567.0   1592.8   -778.5   1557.0     1295 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -2.7254 -0.8776  0.4564  0.7223  2.1447 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.04938  0.2222  
##  QNUM   (Intercept) 0.17479  0.4181  
## Number of obs: 1300, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)      -2.2374     0.3309  -6.762 1.36e-11 ***
## CRT.medsplit      0.5645     0.1343   4.205 2.61e-05 ***
## final.grade.fix   3.5738     0.3989   8.960  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) CRT.md
## CRT.medsplt -0.074       
## finl.grd.fx -0.713 -0.218
```

```
##                       Est          LL         UL
## (Intercept)      0.106731  0.05580075  0.2041461
## CRT.medsplit     1.758644  1.35172582  2.2880583
## final.grade.fix 35.650129 16.31314065 77.9084626
```

CRT effect for treatment condition only, controlling for question difficulty and test performance

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ CRT.medsplit + final.grade.fix + (1 | QNUM) + (1 |  
##     ID)
##    Data: subset(dat.trt, TREATMENT == 1)
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   1523.5   1549.3   -756.7   1513.5     1295 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -2.8951 -0.9044  0.4590  0.6524  2.3367 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.09284  0.3047  
##  QNUM   (Intercept) 0.10412  0.3227  
## Number of obs: 1300, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)      -1.9880     0.3040  -6.539 6.19e-11 ***
## CRT.medsplit      0.6950     0.1389   5.004 5.63e-07 ***
## final.grade.fix   3.4238     0.4047   8.461  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) CRT.md
## CRT.medsplt -0.089       
## finl.grd.fx -0.779 -0.197
```

```
##                       Est          LL         UL
## (Intercept)      0.136966  0.07547907  0.2485416
## CRT.medsplit     2.003647  1.52612931  2.6305762
## final.grade.fix 30.686604 13.88350109 67.8263811
```

### Run the regressions on the entire data set with TREATMENT x CRT.medsplit interaction term

First run with low CRT and TREATMENT=Control as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT * CRT.medsplit + final.grade.fix + (1 |  
##     QNUM) + (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3076.0   3117.1  -1531.0   3062.0     2593 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.1572 -0.9095  0.4642  0.6908  2.6693 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.0000   0.000   
##  QNUM   (Intercept) 0.1421   0.377   
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                         Estimate Std. Error z value Pr(>|z|)    
## (Intercept)              -2.1747     0.2665  -8.160 3.34e-16 ***
## TREATMENT1                0.1554     0.1397   1.112    0.266    
## CRT.medsplit              0.5615     0.1280   4.387 1.15e-05 ***
## final.grade.fix           3.4669     0.2719  12.752  < 2e-16 ***
## TREATMENT1:CRT.medsplit   0.1224     0.1795   0.682    0.495    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATMENT1 CRT.md fnl.g.
## TREATMENT1  -0.266                         
## CRT.medsplt -0.172  0.542                  
## finl.grd.fx -0.602  0.008     -0.188       
## TREATMENT1:  0.200 -0.779     -0.688  0.006
```

```
##                                Est          LL         UL
## (Intercept)              0.1136441  0.06740656  0.1915984
## TREATMENT1               1.1680910  0.88826229  1.5360739
## CRT.medsplit             1.7533076  1.36431982  2.2532015
## final.grade.fix         32.0361018 18.80297438 54.5824187
## TREATMENT1:CRT.medsplit  1.1302342  0.79494196  1.6069466
```

Then run with high CRT and TREATMENT=Control as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT * CRT.medsplit.rev + final.grade.fix + (1 |  
##     QNUM) + (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3076.0   3117.1  -1531.0   3062.0     2593 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.1572 -0.9095  0.4642  0.6908  2.6693 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.0000   0.000   
##  QNUM   (Intercept) 0.1421   0.377   
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                             Estimate Std. Error z value Pr(>|z|)    
## (Intercept)                  -1.6132     0.2751  -5.864 4.51e-09 ***
## TREATMENT1                    0.2778     0.1127   2.466   0.0137 *  
## CRT.medsplit.rev             -0.5615     0.1280  -4.387 1.15e-05 ***
## final.grade.fix               3.4669     0.2719  12.753  < 2e-16 ***
## TREATMENT1:CRT.medsplit.rev  -0.1224     0.1795  -0.682   0.4953    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATMENT1 CRT.m. fnl.g.
## TREATMENT1  -0.208                         
## CRT.mdsplt. -0.299  0.423                  
## finl.grd.fx -0.671  0.019      0.188       
## TREATMENT1:  0.126 -0.628     -0.688 -0.006
```

```
##                                    Est         LL         UL
## (Intercept)                  0.1992535  0.1162129  0.3416313
## TREATMENT1                   1.3202159  1.0586438  1.6464180
## CRT.medsplit.rev             0.5703502  0.4438147  0.7329622
## final.grade.fix             32.0360576 18.8032989 54.5813258
## TREATMENT1:CRT.medsplit.rev  0.8847727  0.6223034  1.2579438
```


Then run with high CRT and TREATMENT=Treatment as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ CONTROL * CRT.medsplit.rev + final.grade.fix + (1 |  
##     QNUM) + (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3076.0   3117.1  -1531.0   3062.0     2593 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.1572 -0.9095  0.4642  0.6908  2.6693 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.0000   0.000   
##  QNUM   (Intercept) 0.1421   0.377   
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                           Estimate Std. Error z value Pr(>|z|)    
## (Intercept)                -1.3354     0.2747  -4.862 1.16e-06 ***
## CONTROL1                   -0.2778     0.1127  -2.466   0.0137 *  
## CRT.medsplit.rev           -0.6839     0.1305  -5.243 1.58e-07 ***
## final.grade.fix             3.4669     0.2718  12.753  < 2e-16 ***
## CONTROL1:CRT.medsplit.rev   0.1224     0.1795   0.682   0.4953    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) CONTROL1 CRT.m. fnl.g.
## CONTROL1    -0.202                       
## CRT.mdsplt. -0.304  0.449                
## finl.grd.fx -0.664 -0.019    0.176       
## CONTROL1:CR  0.131 -0.628   -0.702  0.006
```

```
##                                  Est         LL         UL
## (Intercept)                0.2630577  0.1535466  0.4506733
## CONTROL1                   0.7574515  0.6073793  0.9446036
## CRT.medsplit.rev           0.5046303  0.3907792  0.6516513
## final.grade.fix           32.0360843 18.8036529 54.5803896
## CONTROL1:CRT.medsplit.rev  1.1302342  0.7949482  1.6069342
```

And then for completion run with Low CRT and TREATMENT=Treatment as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: 
## QCORRECT ~ CONTROL * CRT.medsplit + final.grade.fix + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3076.0   3117.1  -1531.0   3062.0     2593 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.1572 -0.9095  0.4642  0.6908  2.6693 
## 
## Random effects:
##  Groups Name        Variance  Std.Dev. 
##  ID     (Intercept) 1.155e-13 3.399e-07
##  QNUM   (Intercept) 1.421e-01 3.770e-01
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                       Estimate Std. Error z value Pr(>|z|)    
## (Intercept)            -2.0193     0.2659  -7.594 3.10e-14 ***
## CONTROL1               -0.1554     0.1397  -1.112    0.266    
## CRT.medsplit            0.6839     0.1305   5.243 1.58e-07 ***
## final.grade.fix         3.4669     0.2719  12.753  < 2e-16 ***
## CONTROL1:CRT.medsplit  -0.1224     0.1795  -0.682    0.495    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) CONTROL1 CRT.md fnl.g.
## CONTROL1    -0.259                       
## CRT.medsplt -0.177  0.540                
## finl.grd.fx -0.599 -0.008   -0.176       
## CONTROL1:CR  0.209 -0.779   -0.702 -0.006
```

```
##                              Est         LL         UL
## (Intercept)            0.1327469  0.0788279  0.2235471
## CONTROL1               0.8560976  0.6510110  1.1257921
## CRT.medsplit           1.9816478  1.5345611  2.5589911
## final.grade.fix       32.0360673 18.8032207 54.5815862
## CONTROL1:CRT.medsplit  0.8847724  0.6223010  1.2579481
```

### Summary of results

_Format table in markdown instead of R for fun_

None of the cross terms were statistically significant

| ODDS RATIOS [95%CI] | Data Subset           | Interaction Term  |
| ------------- |------------|-----|
| Treatment (low CRT) | 1.188 [0.906, 1.559] | 1.168 [0.888, 1.536] |
| Treatment (high CRT) | 1.331&ast; [1.064, 1.666]  |1.32&ast; [1.059, 1.646] |
| CRT split (Control) | 1.759&ast;&ast;&ast; [1.352, 2.288]      | 1.753&ast;&ast;&ast; [1.364, 2.253] |
| CRT split (Treatment) | 2.004&ast;&ast;&ast; [1.526, 2.631]      | 1.982&ast;&ast;&ast; [1.535, 2.559] |


# Some quick checks with NCRT instead of CRT.medsplit


```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT * NCRT + final.grade.fix + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3067.7   3108.8  -1526.9   3053.7     2593 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -3.2781 -0.9067  0.4619  0.6866  2.7912 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.0000   0.0000  
##  QNUM   (Intercept) 0.1423   0.3772  
## Number of obs: 2600, groups:  ID, 648; QNUM, 4
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)     -2.28794    0.27208  -8.409  < 2e-16 ***
## TREATMENT1       0.20138    0.16934   1.189    0.234    
## NCRT             0.30026    0.05823   5.157 2.51e-07 ***
## final.grade.fix  3.33545    0.27581  12.093  < 2e-16 ***
## TREATMENT1:NCRT  0.01663    0.08110   0.205    0.838    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATMENT1 NCRT   fnl.g.
## TREATMENT1  -0.316                         
## NCRT        -0.247  0.590                  
## finl.grd.fx -0.571  0.008     -0.214       
## TREATMENT1:  0.263 -0.855     -0.684  0.002
```

```
##                        Est          LL         UL
## (Intercept)      0.1014756  0.05953351  0.1729665
## TREATMENT1       1.2230911  0.87764137  1.7045138
## NCRT             1.3502107  1.20458924  1.5134361
## final.grade.fix 28.0909650 16.36049334 48.2321833
## TREATMENT1:NCRT  1.0167644  0.86733496  1.1919384
```

