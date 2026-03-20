import pandas as pd
import glob

files = glob.glob("*.csv")

cols = [
    "4um-Open",
    "4um-Steg",
    "6um-Open",
    "6um-Steg",
    "8um-Open",
    "8um-Steg"
]

results = []

for file in files:

    print("Reading:", file)

    df = pd.read_csv(file, sep=";", decimal=",")

    df.columns = df.columns.str.strip()

    data = df[cols].apply(pd.to_numeric, errors="coerce")

    mean = data.mean().to_dict()

    mean["file"] = file

    results.append(mean)

summary = pd.DataFrame(results)

summary = summary.set_index("file")

print(summary)