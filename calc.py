import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import math

c = 299792458
point = (c / 2, c)

plt.figure()

x, y = point

def pythagoras_formula(hp, b):
    return math.sqrt((hp ** 2) - (b ** 2))

h = pythagoras_formula(y, x) / c

print("측정 & 결과: 빛의 속도로 이동하는 물체가 시간 수축을 겪는 특수상대성 이론의 기본 개념을 시각적으로 설명하는 그래프에서,\n빛의 속도의 50%로 이동할 때 감축된 시간 정도는 약 " + str(h) + "이다.")
print("증명: 공간 이동 속도를 x축, 시간 이동 속도를 y축으로 할 때, 빛의 속도를 1로 두고, 빛의 속도 50%로 가속한 속도를 0.5로 두면, 우리가 느끼는 시간은 피타고라스의 정리를 이용해, 빗변이 1이고 밑변이 0.5인 직각삼각형의 높이에 해당한다. 이때, 해당 삼각형의 높이는 약 0.866이다.")
print("이 코드의 목적은 특수상대성 이론을 이해하고, 1과 0.5라는 간소화된 값을 사용하여 측정한 결과를 실제 빛의 속도(c 상수)와 비교하는 데 있다.")

plt.xlabel('공간 (SPACE)')
plt.ylabel('시간 (TIME)')

plt.scatter(x, y, color='red')
plt.plot([0, x], [0, y], linestyle='-', color='black')
plt.plot([x, x], [y, 0], color='black')
plt.plot([0, x], [0, 0], color='grey')
plt.grid(True)

plt.gca().xaxis.set_major_locator(tkr.MultipleLocator(20000000))
plt.gca().yaxis.set_major_locator(tkr.MultipleLocator(20000000))

plt.gca().yaxis.set_major_formatter(tkr.ScalarFormatter(useOffset=False))
plt.gca().xaxis.set_major_formatter(tkr.ScalarFormatter(useOffset=False))

plt.show()
