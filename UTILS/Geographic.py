import pandas as pd

def lati_long_converter(data):
    lati = data[0::2].to_frame(name = "latitude").reset_index(drop = True)
    long = data[1::2].to_frame(name = "longitude").reset_index(drop = True)
    return pd.concat([lati, long], axis = 1)

if __name__ == "__main__":
    import sys
    sys.path.insert(0, "../")
    path = "../London Datathon Materials Anonymized/"
    df = pd.read_csv(path + "dataset_9.csv")
