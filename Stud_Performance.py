import numpy as np
import matplotlib.pyplot as plt

marks=[65,70,75,80,85]
subjects=["Math","Physics","Chemistry","Englis","CS"]

fig,axs=plt.subplots(1,2,figsize=(10,5))
axs[0].bar(subjects,marks,color=["blue","green","Yellow","pink","black"])

axs[0].set_title("Subjects VS Marks")
axs[0].set_xlabel('subjects')
axs[0].set_ylabel("Marks")


axs[1].plot(marks,marker="*",color="yellow",linestyle="--")
axs[1].set_title("Marks Trend")

plt.show()