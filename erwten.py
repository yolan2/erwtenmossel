
import pandas as pd
from IPython.display import display

try:
  from google.colab import drive
  IN_COLAB=True
except:
  IN_COLAB=False

localpath = ""
if IN_COLAB:
    print("You are running Colab. Let's mount the Google Drive.")
    mount = '/content/gdrive'
    drive.mount(mount)
    localpath =  mount +'/MyDrive/erwtengids/'

erwten = pd.read_csv(localpath + 'Book1.csv', sep=";")

def pos(likely='no', shapec2_like_c4=1, plica_present='no', knob_P3=1, length=1000, ligament_length=1, Umbo_at_top=1):
    erwten = pd.read_csv(localpath + 'Book1.csv', sep=";")
    if likely == 'yes':
        erwten = erwten[erwten['likely'].isin([likely, 'U'])]
    if shapec2_like_c4 != 1:
        erwten = erwten[erwten['shape C2 similar to C4'].isin([shapec2_like_c4, 'U'])].drop('shape C2 similar to C4',
                                                                                            axis=1)
    erwten = erwten[erwten['plica present'].isin([plica_present, 'U'])].drop('plica present', axis=1)

    if length != 'A':
        erwten = erwten[((erwten['length'] < length * 1.25) & (length * 0.75 < erwten['length']))]
    if knob_P3 != 1:
        erwten = erwten[erwten['Knob on or near P3'].isin([knob_P3, 'U'])].drop('Knob on or near P3', axis=1)
    if ligament_length != 1:
        erwten = erwten[erwten['length_ligament'].isin([ligament_length, 'U'])].drop('length_ligament', axis=1)
    if Umbo_at_top != 1:
        erwten = erwten[erwten['Umbo at the top'].isin([Umbo_at_top, 'U'])].drop('Umbo at the top', axis=1)

    display(erwten)
    print('note plica is default no and characteristics that have been provided will not show up in the table anymore')
    print('U means Unclear and will behave as both a yes and no valu, for example a median value for lentgh_ligament')