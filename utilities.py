import matplotlib
import matplotlib.pyplot as plt
from Bio import Phylo
from io import StringIO


NAME_LENGTH = 4
ALPHABET = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
MAX_START_POPULATION_SIZE = NAME_LENGTH**len(ALPHABET)


def check_population_size(population_size):
    if population_size > MAX_START_POPULATION_SIZE:
        raise "You should change NAME_LENGTH"


def generate_name(length=NAME_LENGTH):
    return ''.join(np.random.choice(ALPHABET,size=NAME_LENGTH))


def plot_tree(treedata, mutation_data ,output_file):
    #handle = StringIO(treedata)  # parse the newick string
    tree = Phylo.read(treedata, "newick")
    matplotlib.rc('font', size=6)
    # set the size of the figure
    fig = plt.figure(figsize=(10, 20), dpi=100)
    # alternatively
    # fig.set_size_inches(10, 20)
    axes = fig.add_subplot(1, 1, 1)
    plt.scatter(mutation_data['x'],mutation_data['y'])
    Phylo.draw(tree, axes=axes)
    plt.savefig(output_file, dpi=100)
    return
