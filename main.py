#file_list = ['24_ET1.txt', '48_ET1.txt','72_ET1.txt','24_GluA1GFP.txt','48_GluA1GFP.txt','72_GluA1GFP.txt','24_GluA2GFP.txt','48_GluA2_GFP.txt','72_GluA2GFP.txt','24_negCTRL.txt','48_negCTRL.txt','72_negCTRL.txt']
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import figure
file_list = ['48_negCTRL.txt','72_negCTRL.txt']

dfData = pd.DataFrame()
for file in file_list:
    raw_file = open('txt_files/{}'.format(file))
    read_file = raw_file.read()
    line_list = read_file.split('\n')
    start = line_list.index('Em. Wavelength(nm)	507')
    end = line_list.index('[LC Status Trace(Pump A Pressure)]')
    intensities = []
    for line in line_list[start+2:end-1]:
        line = line.replace('\t', ' ')
        #print(line)
        intensities.append(line[8:15])

    dfData[('{}'.format(file))] =  intensities
    plt.plot(range(len(intensities)), intensities )
    plt.savefig('fig1.png', dpi = 300)
    plt.close()
