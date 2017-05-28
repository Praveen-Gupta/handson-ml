#*******************************************************************************
# Import Modules
#*******************************************************************************
import os
import tarfile
import urllib
import pandas as pd
import numpy as np

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"

#*******************************************************************************
# Fetch Housing Data from given URL and extract CSV
#*******************************************************************************

def fetch_housing_data(housing_url = HOUSING_URL, housing_path = HOUSING_PATH):

    if not os.path.isdir(housing_path):
        print("{} doesn't exists, creating.\n".format(housing_path))
        os.makedirs(housing_path)
    else:
        print("path already exists, continue...\n")

    tgz_path = os.path.join(housing_path, "housing.tgz")

    urllib.request.urlretrieve(housing_url, tgz_path)

    housing_tgz = tarfile.open(tgz_path)

    housing_tgz.extractall(path = housing_path)

    housing_tgz.close()


#*******************************************************************************
# Load Housing Data from CSV to dataFrame
#*******************************************************************************

def load_housing_data(housing_path = HOUSING_PATH):

    csv_path = os.path.join(housing_path, "housing.csv")

    return pd.read_csv(csv_path)

#*******************************************************************************
# Split Data to Train_Set and Test_Set
#*******************************************************************************

def split_train_set(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int (len(data) * test_ratio)

    test_indices = shuffled_indices[0:test_set_size]
    train_indices = shuffled_indices[test_set_size:]

    return data.iloc[train_indices], data.iloc[test_indices]
    
