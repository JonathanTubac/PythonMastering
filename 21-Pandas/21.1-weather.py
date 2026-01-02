import pandas as pd

data = pd.read_csv("./21-Pandas/weather_data.csv")
print(data)

data_to_dict = data.to_dict()
print(data_to_dict)

#temperatures = data["temp"].to_list()
#average_temp = round((sum(temperatures) / len(temperatures)), 2)
#print(f"the average temp was: {average_temp}")

average_temp = data["temp"].mean()
print(average_temp)
highest_temp = data["temp"].max()
print(highest_temp)

#data in columns 
print(data["condition"])
print(data.condition)

#get data in row
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

#Create a dataframe from scratch
students = {
    "students": ["Amy", "James", "Angela"],
    "scores": [56, 23, 12]
}

data = pd.DataFrame(students)
print(data)
data.to_csv("./21-Pandas/students.csv")