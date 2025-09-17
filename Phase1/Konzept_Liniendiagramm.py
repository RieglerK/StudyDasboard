import matplotlib.pyplot as plt

module = [1,2,3,4,5]
avg_grades = [2.3, 2.1, 1.9, 2.0, 1.8]

plt.figure(figsize=(8,4))
plt.plot(module, avg_grades, marker="o")
plt.xlabel("Module")
plt.ylabel("Durchschnittsnote")
plt.title("Notenentwicklung")
plt.grid(True)
plt.gca().invert_yaxis()  
plt.show()
