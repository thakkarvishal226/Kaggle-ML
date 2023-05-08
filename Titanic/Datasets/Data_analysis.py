import pandas as pd



if __name__ == "__main__":
    df = pd.read_csv("./Datasets/train.csv")
    
    print(df.describe())