"""
Generates donut plot showing prob. space for dusjunction
"""
import matplotlib.pyplot as plt



group_names=['P(A or B)']
group_size=[20]
subgroup_names=['P(A)', 'P(B)']
subgroup_size=[10, 10]
plt.rcParams['text.color'] = 'white'

# Create colors
a, b, c=[plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]

# First Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=[a(0.6), b(0.6), c(0.6)] )
plt.setp( mypie, width=0.3, edgecolor='white')
plt.rcParams['text.color'] = 'black'
#fig=plt.figure()
fig.patch.set_facecolor('dimgray')


# Second Ring (Inside)
mypie2, _ = ax.pie(subgroup_size, radius=1.3-0.3, labels=subgroup_names, labeldistance=0.7, colors=[a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), c(0.6), c(0.5), c(0.4), c(0.3), c(0.2)])
plt.setp( mypie2, width=0.4, edgecolor='white')
plt.margins(0,0)


plt.savefig('prob_disjunction.png')
