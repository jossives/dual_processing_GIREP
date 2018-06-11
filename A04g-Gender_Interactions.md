---
title: "A04g Gender Interactions (All P100/P101 Exams)"
author: "Joss Ives"
date: "June 10, 2018"
output:
  html_document:
    keep_md: yes
  pdf_document: default
  word_document: default
---



*updated by Joss Ives 2018 June 10, 22:56:17*

# Overview
This report discusses the initial analysis of the W2017-T1 data from the Physics 100 course. In this course, 4 questions were used to look at the effect of asking students to explain their answer after a multiple-choice question. This used a crossover protocol, where there were 2 versions of the test and each version had 2 explain your answer questions that the other group did not. 

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




```r
names(dat.raw)
```

```
##  [1] "ID"              "QNUM.0"          "QNUM.long"      
##  [4] "QNUM"            "COURSE"          "TERM"           
##  [7] "EXAM"            "QCORRECT"        "TREATMENT"      
## [10] "Version"         "Gender"          "EYAinclude"     
## [13] "d.version"       "NCRT"            "ExamGrade.100"  
## [16] "ExamGrade.fix"   "ExamGrade.LMH"   "ExamGrade.fix.z"
```










### Run the regressions on the two groups individually

Female-only data first

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + ExamGrade.fix.z + (1 | QNUM) + (1 | ID)
##    Data: subset(dat.trt, Gender == "Female")
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   7642.5   7676.6  -3816.3   7632.5     6707 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -8.2355 -0.7913  0.1775  0.7555  3.3661 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.1155   0.3399  
##  QNUM   (Intercept) 1.6373   1.2796  
## Number of obs: 6712, groups:  ID, 752; QNUM, 14
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)      0.28961    0.34491   0.840 0.401085    
## TREATMENT1       0.19459    0.05622   3.461 0.000538 ***
## ExamGrade.fix.z  0.55262    0.03336  16.564  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM
## TREATMENT1  -0.081       
## ExmGrd.fx.z  0.012  0.012
```

```
##                      Est        LL       UL
## (Intercept)     1.335911 0.6794957 2.626445
## TREATMENT1      1.214808 1.0880551 1.356327
## ExamGrade.fix.z 1.737799 1.6277991 1.855232
```

Male-only data

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT + ExamGrade.fix.z + (1 | QNUM) + (1 | ID)
##    Data: subset(dat.trt, Gender == "Male")
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   3938.4   3969.3  -1964.2   3928.4     3607 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -7.2533 -0.7897  0.3702  0.6466  2.8781 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.1861   0.4314  
##  QNUM   (Intercept) 1.4397   1.1999  
## Number of obs: 3612, groups:  ID, 431; QNUM, 14
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)      0.66889    0.32765   2.042   0.0412 *  
## TREATMENT1       0.16915    0.07930   2.133   0.0329 *  
## ExamGrade.fix.z  0.62431    0.04611  13.539   <2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATM
## TREATMENT1  -0.119       
## ExmGrd.fx.z -0.015  0.023
```

```
##                      Est       LL       UL
## (Intercept)     1.952068 1.027065 3.710155
## TREATMENT1      1.184300 1.013815 1.383454
## ExamGrade.fix.z 1.866952 1.705622 2.043542
```

Gender effect for control condition only, controlling for question difficulty and test perfromance

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ Gender + ExamGrade.fix.z + (1 | QNUM) + (1 | ID)
##    Data: subset(dat.trt, TREATMENT == 0)
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   5817.7   5850.5  -2903.9   5807.7     5157 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -7.7314 -0.7810  0.2217  0.7218  3.3847 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.1567   0.3958  
##  QNUM   (Intercept) 1.6176   1.2718  
## Number of obs: 5162, groups:  ID, 1183; QNUM, 14
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)      0.29836    0.34305   0.870    0.384    
## GenderMale       0.39440    0.07422   5.314 1.07e-07 ***
## ExamGrade.fix.z  0.58484    0.03637  16.078  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) GndrMl
## GenderMale  -0.071       
## ExmGrd.fx.z  0.013 -0.100
```

```
##                      Est        LL       UL
## (Intercept)     1.347652 0.6879729 2.639878
## GenderMale      1.483488 1.2826488 1.715775
## ExamGrade.fix.z 1.794699 1.6712039 1.927320
```

Gender effect for treatment condition only, controlling for question difficulty and test performance

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ Gender + ExamGrade.fix.z + (1 | QNUM) + (1 | ID)
##    Data: subset(dat.trt, TREATMENT == 1)
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##   5825.4   5858.1  -2907.7   5815.4     5157 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -7.6664 -0.7899  0.3330  0.6962  2.5395 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.1923   0.4386  
##  QNUM   (Intercept) 1.5111   1.2293  
## Number of obs: 5162, groups:  ID, 1183; QNUM, 14
## 
## Fixed effects:
##                 Estimate Std. Error z value Pr(>|z|)    
## (Intercept)      0.49602    0.33207   1.494    0.135    
## GenderMale       0.35413    0.07548   4.692 2.71e-06 ***
## ExamGrade.fix.z  0.61145    0.03679  16.620  < 2e-16 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) GndrMl
## GenderMale  -0.074       
## ExmGrd.fx.z  0.018 -0.096
```

```
##                      Est        LL       UL
## (Intercept)     1.642176 0.8565624 3.148331
## GenderMale      1.424944 1.2289813 1.652154
## ExamGrade.fix.z 1.843108 1.7148846 1.980918
```

### Run the regressions on the entire data set with TREATMENT x Gender interaction term

First run with Gender=Female and TREATMENT=Control as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT * Gender + ExamGrade.fix.z + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##  11580.9  11631.6  -5783.5  11566.9    10317 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -8.7496 -0.7846  0.2735  0.7186  3.4032 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.1327   0.3643  
##  QNUM   (Intercept) 1.5824   1.2580  
## Number of obs: 10324, groups:  ID, 1183; QNUM, 14
## 
## Fixed effects:
##                       Estimate Std. Error z value Pr(>|z|)    
## (Intercept)            0.29815    0.33913   0.879  0.37932    
## TREATMENT1             0.19970    0.05597   3.568  0.00036 ***
## GenderMale             0.39281    0.07276   5.399 6.71e-08 ***
## ExamGrade.fix.z        0.57560    0.02686  21.428  < 2e-16 ***
## TREATMENT1:GenderMale -0.03333    0.09687  -0.344  0.73078    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATMENT1 GndrMl ExmG..
## TREATMENT1  -0.082                         
## GenderMale  -0.072  0.387                  
## ExmGrd.fx.z  0.010  0.011     -0.092       
## TREATMENT1:  0.048 -0.577     -0.662  0.005
```

```
##                             Est        LL       UL
## (Intercept)           1.3473637 0.6931194 2.619158
## TREATMENT1            1.2210399 1.0941668 1.362625
## GenderMale            1.4811392 1.2842871 1.708164
## ExamGrade.fix.z       1.7781998 1.6870017 1.874328
## TREATMENT1:GenderMale 0.9672172 0.7999578 1.169448
```

Then run with Gender=Male and TREATMENT=Control as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ TREATMENT * GRELEVEL + ExamGrade.fix.z + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##  11580.9  11631.6  -5783.5  11566.9    10317 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -8.7496 -0.7846  0.2735  0.7186  3.4032 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.1327   0.3643  
##  QNUM   (Intercept) 1.5825   1.2580  
## Number of obs: 10324, groups:  ID, 1183; QNUM, 14
## 
## Fixed effects:
##                           Estimate Std. Error z value Pr(>|z|)    
## (Intercept)                0.69097    0.34164   2.022   0.0431 *  
## TREATMENT1                 0.16637    0.07908   2.104   0.0354 *  
## GRELEVELFemale            -0.39281    0.07276  -5.399  6.7e-08 ***
## ExamGrade.fix.z            0.57560    0.02686  21.428  < 2e-16 ***
## TREATMENT1:GRELEVELFemale  0.03333    0.09687   0.344   0.7308    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) TREATMENT1 GRELEV ExmG..
## TREATMENT1  -0.114                         
## GRELEVELFml -0.142  0.537                  
## ExmGrd.fx.z -0.010  0.014      0.092       
## TREATMENT1:  0.094 -0.816     -0.662 -0.005
```

```
##                                 Est        LL        UL
## (Intercept)               1.9956460 1.0215818 3.8984672
## TREATMENT1                1.1810114 1.0114386 1.3790138
## GRELEVELFemale            0.6751564 0.5854265 0.7786395
## ExamGrade.fix.z           1.7781998 1.6870016 1.8743280
## TREATMENT1:GRELEVELFemale 1.0338931 0.8551098 1.2500557
```

**This one is not working for unknown reasons**

Then run with Gender=Male and TREATMENT=Treatment as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ CONTROL * GRELEVEL + ExamGrade.fix.z + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##  11580.9  11631.6  -5783.5  11566.9    10317 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -8.7496 -0.7846  0.2735  0.7186  3.4032 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.1327   0.3643  
##  QNUM   (Intercept) 1.5825   1.2580  
## Number of obs: 10324, groups:  ID, 1183; QNUM, 14
## 
## Fixed effects:
##                         Estimate Std. Error z value Pr(>|z|)    
## (Intercept)              0.85733    0.34173   2.509   0.0121 *  
## CONTROL1                -0.16637    0.07908  -2.104   0.0354 *  
## GRELEVELFemale          -0.35948    0.07309  -4.918 8.73e-07 ***
## ExamGrade.fix.z          0.57560    0.02686  21.428  < 2e-16 ***
## CONTROL1:GRELEVELFemale -0.03333    0.09687  -0.344   0.7308    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) CONTROL1 GRELEV ExmG..
## CONTROL1    -0.117                       
## GRELEVELFml -0.143  0.547                
## ExmGrd.fx.z -0.006 -0.014    0.085       
## CONTROL1:GR  0.095 -0.816   -0.666  0.005
```

```
##                               Est        LL        UL
## (Intercept)             2.3568578 1.2062688 4.6049260
## CONTROL1                0.8467321 0.7251501 0.9886991
## GRELEVELFemale          0.6980394 0.6048737 0.8055550
## ExamGrade.fix.z         1.7781997 1.6870013 1.8743282
## CONTROL1:GRELEVELFemale 0.9672180 0.7999542 1.1694552
```

And then for completion run with Gender=Female and TREATMENT=Treatment as the base levels

```
## Generalized linear mixed model fit by maximum likelihood (Laplace
##   Approximation) [glmerMod]
##  Family: binomial  ( logit )
## Formula: QCORRECT ~ CONTROL * Gender + ExamGrade.fix.z + (1 | QNUM) +  
##     (1 | ID)
##    Data: dat.trt
## Control: glmerControl(optimizer = "bobyqa")
## 
##      AIC      BIC   logLik deviance df.resid 
##  11580.9  11631.6  -5783.5  11566.9    10317 
## 
## Scaled residuals: 
##     Min      1Q  Median      3Q     Max 
## -8.7496 -0.7846  0.2735  0.7186  3.4032 
## 
## Random effects:
##  Groups Name        Variance Std.Dev.
##  ID     (Intercept) 0.1327   0.3643  
##  QNUM   (Intercept) 1.5825   1.2580  
## Number of obs: 10324, groups:  ID, 1183; QNUM, 14
## 
## Fixed effects:
##                     Estimate Std. Error z value Pr(>|z|)    
## (Intercept)          0.49786    0.33922   1.468  0.14220    
## CONTROL1            -0.19970    0.05598  -3.568  0.00036 ***
## GenderMale           0.35948    0.07309   4.918 8.73e-07 ***
## ExamGrade.fix.z      0.57560    0.02686  21.428  < 2e-16 ***
## CONTROL1:GenderMale  0.03333    0.09688   0.344  0.73080    
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Correlation of Fixed Effects:
##             (Intr) CONTROL1 GndrMl ExmG..
## CONTROL1    -0.083                       
## GenderMale  -0.071  0.380                
## ExmGrd.fx.z  0.012 -0.011   -0.085       
## CONTROL1:GM  0.048 -0.578   -0.666 -0.005
```

```
##                           Est        LL        UL
## (Intercept)         1.6451935 0.8461849 3.1986644
## CONTROL1            0.8189744 0.7338754 0.9139413
## GenderMale          1.4325841 1.2413769 1.6532425
## ExamGrade.fix.z     1.7781999 1.6870014 1.8743285
## CONTROL1:GenderMale 1.0338927 0.8550932 1.2500789
```

### Summary of results

_Format table in markdown instead of R for fun_

None of the cross terms were statistically significant

| ODDS RATIOS [95%CI] | Data Subset           | Interaction Term  |
| ------------- |------------|-----|
| Treatment (Female) | 1.215&ast;&ast;&ast; [1.088, 1.356] | 1.221&ast;&ast;&ast; [1.094, 1.363] |
| Treatment (Male) | 1.184&ast; [1.014, 1.383]  |1.181 [1.011, 1.379] |
| Gender (Control) | 1.483&ast;&ast;&ast; [1.283, 1.716]      | 1.481&ast;&ast;&ast; [1.284, 1.708] |
| Gender (Treatment) | 1.425&ast;&ast;&ast; [1.229, 1.652]      | 1.433&ast;&ast;&ast; [1.241, 1.653] |



