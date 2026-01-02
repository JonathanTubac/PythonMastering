import pandas as pd

data = pd.read_csv("./21-Pandas/squirrel_censum.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

color_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count],
}

df = pd.DataFrame(color_dict)
df.to_csv("./21-Pandas/squirrel_colors.csv")