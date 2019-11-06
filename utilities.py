import matplotlib
import matplotlib.pyplot as plt
from Bio import Phylo
from io import StringIO

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