[![European Galaxy server](https://img.shields.io/badge/usegalaxy-.eu-brightgreen?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAASCAYAAABB7B6eAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAACXBIWXMAAAsTAAALEwEAmpwYAAACC2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS40LjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDx0aWZmOlJlc29sdXRpb25Vbml0PjI8L3RpZmY6UmVzb2x1dGlvblVuaXQ+CiAgICAgICAgIDx0aWZmOkNvbXByZXNzaW9uPjE8L3RpZmY6Q29tcHJlc3Npb24+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlBob3RvbWV0cmljSW50ZXJwcmV0YXRpb24+MjwvdGlmZjpQaG90b21ldHJpY0ludGVycHJldGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KD0UqkwAAAn9JREFUOBGlVEuLE0EQruqZiftwDz4QYT1IYM8eFkHFw/4HYX+GB3/B4l/YP+CP8OBNTwpCwFMQXAQPKtnsg5nJZpKdni6/6kzHvAYDFtRUT71f3UwAEbkLch9ogQxcBwRKMfAnM1/CBwgrbxkgPAYqlBOy1jfovlaPsEiWPROZmqmZKKzOYCJb/AbdYLso9/9B6GppBRqCrjSYYaquZq20EUKAzVpjo1FzWRDVrNay6C/HDxT92wXrAVCH3ASqq5VqEtv1WZ13Mdwf8LFyyKECNbgHHAObWhScf4Wnj9CbQpPzWYU3UFoX3qkhlG8AY2BTQt5/EA7qaEPQsgGLWied0A8VKrHAsCC1eJ6EFoUd1v6GoPOaRAtDPViUr/wPzkIFV9AaAZGtYB568VyJfijV+ZBzlVZJ3W7XHB2RESGe4opXIGzRTdjcAupOK09RA6kzr1NTrTj7V1ugM4VgPGWEw+e39CxO6JUw5XhhKihmaDacU2GiR0Ohcc4cZ+Kq3AjlEnEeRSazLs6/9b/kh4eTC+hngE3QQD7Yyclxsrf3cpxsPXn+cFdenF9aqlBXMXaDiEyfyfawBz2RqC/O9WF1ysacOpytlUSoqNrtfbS642+4D4CS9V3xb4u8P/ACI4O810efRu6KsC0QnjHJGaq4IOGUjWTo/YDZDB3xSIxcGyNlWcTucb4T3in/3IaueNrZyX0lGOrWndstOr+w21UlVFokILjJLFhPukbVY8OmwNQ3nZgNJNmKDccusSb4UIe+gtkI+9/bSLJDjqn763f5CQ5TLApmICkqwR0QnUPKZFIUnoozWcQuRbC0Km02knj0tPYx63furGs3x/iPnz83zJDVNtdP3QAAAABJRU5ErkJggg==)](https://usegalaxy.eu/root?tool_id=deepmicro)

* Modified from https://github.com/minoh0201/DeepMicro
* Added to bioconda
* Added wrapper for Galaxy

# DeepMicro
DeepMicro is a deep representation learning framework exploiting various autoencoders to learn robust low-dimensional representations from high-dimensional data and training classification models based on the learned representation.

## Quick Setup Guide

```
~$ conda install deepmicro
```

* For GPU usage install tensorflow GPU version
```
~$ conda install tensorflow-gpu==1.13.1
```
**Step 5:** Run DeepMicro, printing out its usage.
```
~$ python DM.py -h
```

## Quick Start Guide
*Make sure you have already gone through the **Quick Setup Guide** above.*
### Learning representation with your own data
__1. Copy your data under the `/data` directory.__ Your data should be a comma separated file without header and index, where each row represents a sample and each column represents a microbe. We are going to assume that your file name is `UserDataExample.csv` which is already provided.

__2. Check your data can be successfully loaded and verify its shape with the following command.__
```
~$ python DM.py -r 1 --no_clf -cd UserDataExample.csv
```
The output will show the number of rows and columns right next to `X_train.shape`. Our data `UserDataExample.csv` contains 80 rows and 200 columns.
```
Using TensorFlow backend.
Namespace(act='relu', ae=False, ae_lact=False, ae_oact=False, aeloss='mse', cae=False, custom_data='UserDataExample.csv', custom_data_labels=None, data=None, dataType='float64', data_dir='', dims='50', max_epochs=2000, method='all', no_clf=True, numFolds=5, numJobs=-2, patience=20, pca=False, repeat=1, rf_rate=0.1, rp=False, save_rep=False, scoring='roc_auc', seed=0, st_rate=0.25, svm_cache=1000, vae=False, vae_beta=1.0, vae_warmup=False, vae_warmup_rate=0.01)
X_train.shape:  (80, 200)
Classification task has been skipped.
```
    
__3. Suppose that we want to reduce the number of dimensions of our data to 20 from 200 using a *shallow autoencoder*.__ Note that `--save_rep` argument will save your representation (the complete representation - not just the training) under the `/results` folder.
```
~$ python DM.py -r 1 --no_clf -cd UserDataExample.csv --ae -dm 20 --save_rep
```
    
__4. Suppose that we want to use *deep autoencoder* with 2 hidden layers which has 100 units and 40 units, respectively.__ Let the size of latent layer to be 20. We are going to see the structure of deep autoencoder first.
```
~$ python DM.py -r 1 --no_clf -cd UserDataExample.csv --ae -dm 100,40,20 --no_trn
```
It looks fine. Now, run the model and get the learned representation.
```    
~$ python DM.py -r 1 --no_clf -cd UserDataExample.csv --ae -dm 100,40,20 --save_rep
```
__5. We can try *variational autoencoder* and * convolutional autoencoder* as well.__ Note that you can see detailed argument description by using `-h` argument.
```
~$ python DM.py -r 1 --no_clf -cd UserDataExample.csv --vae -dm 100,20 --save_rep
```
```
~$ python DM.py -r 1 --no_clf -cd UserDataExample.csv --cae -dm 100,50,1 --save_rep
```

### Conducting binary classification after Learning representation with your own data
__1. Copy your *data file* and *label file* under the `/data` directory.__ Your data file should be a comma separated value (CSV) format without header and index, where each row represents a sample and each column represents a microbe. __Your label file should contain a binary value (0 or 1) in each line and the number of lines should be equal to that in your data file.__ We are going to assume that your data file name is `UserDataExample.csv` and label file name is `UserLabelExample.csv` which are already provided.

__2. Check your data can be successfully loaded and verify its shape with the following command.__
```
~$ python DM.py -r 1 --no_clf -cd UserDataExample.csv -cl UserLabelExample.csv
```
Our data `UserDataExample.csv` consists of 80 samples each of which has 200 features. The data will be split into the training set and the test set (in 8:2 ratio). The output will show the number of rows and columns for each data set.
```
Namespace(act='relu', ae=False, ae_lact=False, ae_oact=False, aeloss='mse', cae=False, custom_data='UserDataExample.csv', custom_data_labels='UserLabelExample.csv', data=None, dataType='float64', data_dir='', dims='50', max_epochs=2000, method='all', no_clf=True, no_trn=False, numFolds=5, numJobs=-2, patience=20, pca=False, repeat=1, rf_rate=0.1, rp=False, save_rep=False, scoring='roc_auc', seed=0, st_rate=0.25, svm_cache=1000, vae=False, vae_beta=1.0, vae_warmup=False, vae_warmup_rate=0.01)
X_train.shape:  (64, 200)
y_train.shape:  (64,)
X_test.shape:  (16, 200)
y_test.shape:  (16,)
Classification task has been skipped.
```

__3. Suppose that we want to directly apply SVM algorithm on our data without representation learning.__  Remove `--no_clf` command and specify classification method with `-m svm` argument (If you don't specify classification algorithm, all three algorithms will be running). 
```
~$ python DM.py -r 1 -cd UserDataExample.csv -cl UserLabelExample.csv -m svm
```
The result will be saved under `/results` folder as a `UserDataExample_result.txt`. The resulting file will be growing as you conduct more experiments.

__4. You can learn representation first, and then apply SVM algorithm on the learned representation.__
```
~$ python DM.py -r 1 -cd UserDataExample.csv -cl UserLabelExample.csv --ae -dm 20 -m svm
```

__4.1. You can reload the stored the representation, and then apply SVM algorithm on the learned representation.__
```
~$ python DM.py -r 1 -cd UserDataExample.csv -cl UserLabelExample.csv --load_rep results/PCA_UserDataExample_rep.csv -m svm
```

__5. You can repeat the same experiment by changing seeds for random partitioning of training and test set.__  Suppose we want to repeat classfication task five times. You can do it by put 5 into `-r` argument.
```
~$ python DM.py -r 5 -cd UserDataExample.csv -cl UserLabelExample.csv --ae -dm 20 -m svm
```

