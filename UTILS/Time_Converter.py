from datetime import datetime
import pandas as pd

def Date_Parser_1(timestamp):
    date, time = timestamp.split(" ")
    day, month, year = date.split("/")
    year = "20" + year
    date = day + "/" + month + "/" + year
    time = time + ":00"
    return datetime.strptime(date + " " + time, "%d/%m/%Y %H:%M:%S")

def Date_Parser_2(timestamp):
    date, time = timestamp.split(" ")
    day, month, year = date.split("-")
    year = "20" + year
    date = day + "-" + month + "-" + year
    return datetime.strptime(date + " " + time, "%m-%d-%Y %H:%M:%S")

if __name__ == "__main__":
    import sys
    sys.path.insert(0, "../")
    path = "../London Datathon Materials Anonymized/"
    df = pd.read_csv(path + "dataset_9.csv")

    print(df)
    # print(Date_Parser_2(df.iloc[0, 1]))
