import numpy as np
import matplotlib.pyplot as plt
months=["Jan","Feb","Mar","Apr","May"]
sales=[200,250,300,280,350]
profit=[20,30,50,40,60]

fig,axs=plt.subplots(1,2,figsize=(10,5))

axs[0].plot(months,sales,marker="o",color="blue",label="Sales")
axs[0].set_title("Sales vs Months")
axs[0].set_xlabel("Month")
axs[0].set_ylabel("Sales")

axs[0].legend()

axs[1].bar(months,profit,color="red",label="Profit")
axs[1].set_title("Profit vs Months")
axs[1].set_xlabel("Month")
axs[1].set_ylabel("Profits")

axs[1].legend()
plt.show()