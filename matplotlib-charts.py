import matplotlib.pyplot as plt

# ---------- Pie Chart ----------
labels = ['Python', 'Java', 'C++', 'Ruby']
sizes = [40, 30, 20, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Programming Language Usage")
plt.axis("equal")
plt.show()

# Horizontal Bar Chart 
Names = ["Anurag Sharma", "Priyanka Mishra", "Mohammad Salman", "Harshita Jain", "Sameer Ali"]
Salary = [5.5, 6.2, 7.0, 5.8, 6.5]

plt.figure(figsize=(10,5))
for i in range(len(Salary)):
    plt.text(Salary[i]+0.1, i, str(Salary[i]), va="center")

plt.barh(Names, Salary, color='red')
plt.title("Employee Salary (in LPA)")
plt.xlabel("Salary_in_LPA")
plt.ylabel("Employee_Name")
plt.tight_layout()
plt.show()
