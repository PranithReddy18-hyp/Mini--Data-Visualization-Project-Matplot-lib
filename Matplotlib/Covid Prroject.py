import matplotlib.pyplot as plt
days=[1,2,3,4,5]
cases=[100,200,300,400,500]
recoveries=[50,150,250,30,450]

plt.plot(days,cases,color="red",marker="o",label="Cases")
plt.plot(days,recoveries,color="blue",marker="*",label="Recoveries")
plt.title("CORONA (Cases vs Recovories)")
plt.xlabel("No of Days")
plt.ylabel("Cases & Rcovories")
plt.legend()
plt.show()