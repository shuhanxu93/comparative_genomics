import gzip
import collections
import matplotlib.pyplot as plt

species_list = ['362663', '100226', '4932', '266117', '349124']
interactomes = {species: dict() for species in species_list}

with gzip.open('../data/protein.links.v10.5.txt.gz', 'r') as filehandle:
    for line in filehandle:
        for species in interactomes:
            if line.startswith(species + '.'):
                if not line.split()[0] in interactomes[species]:
                    interactomes[species][line.split()[0]] = 1
                else:
                    interactomes[species][line.split()[0]] += 1

for species in species_list:
    size = len(interactomes[species])
    total_degree = sum(interactomes[species].values())
    average_connectivity = total_degree / size
    print(species, average_connectivity)

fig, axs = plt.subplots(3,2)

axs = axs.ravel()

for index, species in enumerate(species_list):
    degree_list = list(interactomes[species].values())
    count = dict(collections.Counter(degree_list))
    degree, frequency = zip(*count.items())
    axs[index].scatter(degree, frequency)
    axs[index].set_title(species)

for ax in axs.flatten():
    ax.set_xlabel('degree')
    ax.set_ylabel('frequence')
    ax.set_xscale('log')
    ax.set_yscale('log')

plt.show()
