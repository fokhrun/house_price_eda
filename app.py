
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats


df_train = pd.read_csv('data/train.csv')


def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Distribution Plot"
        ]
    )
    linePlot()
    

def linePlot():
    fig = plt.figure(figsize=(10, 4))
    sns.distplot(df_train['SalePrice'])
    st.pyplot(fig)
    
if __name__ == "__main__":
    main()