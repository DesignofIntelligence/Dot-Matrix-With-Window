import pandas as pd
import matplotlib.pyplot as plt
def dotplot(sequence_a,sequence_b,window,threshold,step):
    matrix = []
    matrix = [[0] * len(sequence_b) for _ in range(len(sequence_a))]
    colors = [['w'] * len(sequence_b) for _ in range(len(sequence_a))]
    for i in range(0, len(sequence_a)-window+1,step):
        for j in range(0,len(sequence_b)-window+1, step):
            counter =0
            for k in range(window):
                if sequence_b[k+i] == sequence_a[k+j]:
                    counter += 1
            if counter >= threshold:
                matrix[i + int(window/ 2)][j + int(window / 2)] = 1
                colors[i + int(window/ 2)][j + int(window / 2)] = 'g'

    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    df = pd.DataFrame(matrix, columns=list(sequence_a))

    ax.table(cellText=df.values, colLabels=df.columns,
             loc='center', rowLabels="" + sequence_b,
             cellColours=colors,
              colWidths=[0.05 for x in df.columns], )
    fig.tight_layout()
    plt.show()
    print(matrix)

sequence_a = "ACCTTGTCCTCTTTGCCC"
sequence_b = "ACGTTGACCTGTAACCTC"

window = 9
threshold = 4
step = 3
dotplot(sequence_a,sequence_b,window,threshold,step)