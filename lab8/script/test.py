import gzip
import collections
import matplotlib.pyplot as plt

species_list = ['394', '882']
interactomes = {species: dict() for species in species_list}

print('parsing file')

with open('../data/test.txt', 'r') as filehandle:
    for line in filehandle:
        for species in interactomes:
            if line.startswith(species + '.'):
                if line.split()[0] in interactomes[species]:
                    interactomes[species][line.split()[0]] += 1
                else:
                    interactomes[species][line.split()[0]] = 1

for species in species_list:
    size = len(interactomes[species])
    total_degree = sum(interactomes[species].values())
    average_connectivity = total_degree / size
    print(species, average_connectivity)

fig, axs = plt.subplots(3,2)

axs = axs.ravel()

for index, species in enumerate(species_list):
    degree_list = interactomes[species].values()
    count = collections.Counter(degree_list)
    degree, frequency = zip(*count.items())
    axs[index].scatter(degree, frequency)
    axs[index].set_title(species)
    axs[index].set_xlabel('degree')
    axs[index].set_ylabel('frequence')
    axs[index].set_xscale('log')
    axs[index].set_yscale('log')

plt.show()
