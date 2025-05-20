import matplotlib.pyplot as plt

with open("violent_crime_data.txt", "r") as file:
    lines = file.readlines()

years = []
crime_counts = []

for line in lines:
    year, count = line.strip().split(",")
    years.append(int(year))
    crime_counts.append(int(count))

plt.figure(figsize=(10, 6)) 

plt.plot(years, crime_counts, color='red', marker='o', label='Violent Crimes')

plt.title("Violent Crime in the U.S. (2010–2020)")
plt.xlabel("Year")
plt.ylabel("Number of Violent Crimes")
plt.grid(True)
plt.legend()

plt.show()