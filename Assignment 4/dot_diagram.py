from re import I
import matplotlib.pyplot as plt
import numpy as np
def make_diagram(seq1, seq2):
    data = np.zeros((len(seq1), len(seq2)))
    for i, base1 in enumerate(seq1):
        for j, base2 in enumerate(seq2):
            if base1 == base2:
                data[i, j] = 1
    #plt.xticks(range(len(seq2)), labels=seq2)
    #plt.yticks(range(len(seq1)), labels=seq1)
    plt.imshow(data, interpolation='nearest', cmap='binary')
    plt.gca().xaxis.tick_top()
make_diagram('AATGAGAAAGTATTTCCCCGACAATCAATACGGGACGCTCCTAAGTTTTTCCACTCGCTTGAGCCGGCTAGGCCTCTCTGCCCGAAGTTTCGACGGACTGCTGCCAACACCCAGGCATAGTTTTAGGAGGGTTATTCGGGGGCACTCGCAGCCAACTTGTCGGGTCCTGCCCGGCTGGTCTTCGGGCTAATATAGCGAATTGCCGAGAACCCGGCCCCACGCAATGGAACGTCTTTAGCTCCGGCAGGCAATTAAGGACAACGTAAGTATAGCGCATATAAACAGAGAAATGGGCGAATGAACCTATTCGTACCGTATCGAAGAATAGCCTCGCGGAGGCATGTGCCATGCTAGCGTGCGGGGCACTCTAGTTATGCATATGGTCCACAGGACACTCGTCGCTTTCGGATTTGCCCTCTATGTGGCGGTTTTCAGGCACACTTATGCTCAGCACCGTTTAAACCAGACCGACACTAGATCTATAAGGTCCGCCATGCAGACGAGAGCGCACGGAGATCACCGAGCGATCTATCAGATCGGCGACCATTTGTGAGGTACTGGAGCCGAGAGGTAACTACGATGCCGCTAAGAAC', 
'TCTCGGTCGTCGCTGACGTTTACACTCTAGTCTCATTATAATCGTTCGCTATTCAGGGATTGACCAACACCGGAAAACATCTCACTTGAAGTAATGTATACGACAGAGTCCGTGCACCTACCAAACCTCTTTAGTCTAAGTTCAGACTAGTTGGAAGTTTGTCTAGATCTCAGATTTTGTCACTAGAGGACGCACGCTCTATTTTTATGATCCATTGATGTCCCTGACGCTGCAAAATTTGCAACCAGGCAGTCTTCGCGGTAGGTCCTAGTGCAATGGGGCTTTTTTTCCATAGTCCTCGAGAGGAGGAGACGTCAGTCCAGATATCTTTGATGTCGTGATTGGAAGGACCCTTGGCCCTCCACCCTTAGGCAGTGTATACTCTTCCATAAACGGGCTATTAGTT')
plt.savefig('large_dot_diagram.png')