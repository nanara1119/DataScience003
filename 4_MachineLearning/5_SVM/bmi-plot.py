import matplotlib.pyplot as plt
import pandas as pd

#   Pandas 로 csv 읽기
tbl = pd.read_csv("bmi.csv", index_col=2)

#   그래프 그림
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#   서브 플롯 적용
def scatter(lbl, color) :
    b = tbl.loc[lbl]
    ax.scatter(b["weight"],b["height"], c=color, label=lbl)

scatter("fat", "red")
scatter("normal", "yellow")
scatter("thin", "purple")

ax.legend()
plt.savefig("bmi-test.png")
