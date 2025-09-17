import matplotlib.pyplot as plt

gesamt_ects = 180
erreichte_ects = 45
offen_ects = gesamt_ects - erreichte_ects

werte = [erreichte_ects, offen_ects]
labels = [f"Geschafft: {erreichte_ects} ECTS", f"Offen: {offen_ects} ECTS"]
farben = ["#66bb6a", "#b54343"]  

plt.figure(figsize=(6,6))
plt.pie(
    werte, 
    labels=labels, 
    autopct="%1.1f%%", 
    startangle=90, 
    colors=farben
)
plt.title("Studienfortschritt in ECTS")
plt.show()
