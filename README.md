# Early-Stage Melanoma Recurrence Prediction
Source code of the paper:    
**[Prediction of Early-Stage Melanoma Recurrence Using Clinical and Histopathologic Features](https://www.nature.com/articles/s41698-022-00321-4)**   
by Guihong Wan, Nga Nguyen, Feng Liu, Mia S. DeSimone, Bonnie W. Leung, ..., Peter K. Sorger, Kun-Hsing Yu, and Yevgeniy R. Semenov.
Accepted in principle in NPJ Precision Oncology, 2022.
Research Use Only.

## Description
data: includes an sample dataset.    
melanoma_example_v1.0.csv: 30 artificial samples created to demonstrate the running of the codes.


code: includes codes for the analyses.          
Melanoma_cohort_v1.0.Rmd for data preprocessing.              
ml-analysis-site-binary-classification-v1.0.ipynb: binary recurrence classification tasks.        
ml-analysis-site-binary-feature-importance-v1.0.ipynb: permutation feature importance in binary classification.       
ml-analysis-site-time2event-prediction-v1.0.ipynb: time-to-event prediction, permutation feature importance, and sample predictions.  


## Settings
Data collection and analyses were performed in R 4.2.1, Python 3.8.12, NumPy 1.20.2, scikit-learn 0.24.1, and scikit-survival 0.17.2. 


## Contact
Please contact gwan@mgh.harvard.edu or ysemenov@mgh.harvard.edu in case you have any questions.

## Cite
Please cite our paper if you use the code in your own work:       

```
@article{earlymelanoma2022,         
  title={Prediction of Early-Stage Melanoma Recurrence Using Clinical and Histopathologic Features},            
  author={Wan, Guihong       
  and Nguyen, Nga    
  and Liu, Feng       
  and DeSimone, Mia S       
  and Leung, Bonnie W       
  and others},      
  journal={NPJ Precision Oncology},     
  year="2022"      
}
```
