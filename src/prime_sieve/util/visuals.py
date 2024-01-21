import matplotlib.pyplot as plt
import pandas as pd
import scipy.sparse


def visual(coordinates,values, shape):
    sparse_matrix = scipy.sparse.csr_matrix((values,coordinates),shape=shape)
    matrix = pd.DataFrame.sparse.from_spmatrix(sparse_matrix)
    table = pd.DataFrame([coordinates[0],coordinates[1],values],["y","x","value"]).T

    full_visual = plt.figure(figsize=(8,5))

    matrix_visual = full_visual.add_subplot(131)
    matrix_visual.axis('off')
    matrix_table = matrix_visual.table(cellText = matrix.values, rowLabels = matrix.index, bbox=[0, 0, 1, 1], colLabels=matrix.columns)
    matrix_table.auto_set_font_size(False)
    matrix_table.set_fontsize(14)

    matrix_plot = full_visual.add_subplot(132)
    matrix_plot.spy(sparse_matrix)

    table_visual = full_visual.add_subplot(133)
    table_visual.axis('off')
    table_table = table_visual.table(cellText = table.values, rowLabels = table.index, bbox=[0, 0, 1, 1], colLabels=table.columns)
    table_table.auto_set_font_size(False)
    table_table.set_fontsize(14)