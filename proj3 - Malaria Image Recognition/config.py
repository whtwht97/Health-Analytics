#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np


# In[2]:


# initialize the path to the *original* input directory of images
ORIG_INPUT_DATASET = "malaria/cell_images"

# initialize the base path to the *new* directory that will contain
# our images after computing the training and testing spli
BASE_PATH = "malaria"

# derive the training, validation, and testing directories
TRAIN_PATH = os.path.sep.join([BASE_PATH, "training"])
VAL_PATH = os.path.sep.join([BASE_PATH, "validation"])
TEST_PATH = os.path.sep.join([BASE_PATH, "testing"])


# In[3]:


# define the amount of data that will be used training
TRAIN_SPLIT = 0.8

# the amount of validation data will be a percentage of the
# *training* data
VAL_SPLIT = 0.1


# In[ ]:




