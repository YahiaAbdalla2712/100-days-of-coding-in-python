import numpy as np
import pandas as pd
s = pd.Series(['Tom', 'William Rick', 'John',
'Alber@t ', np.nan, '1234','SteveSmith']);
print(s)
sc = s.str.split(' '); print(sc)
sc = s.str.cat(sep='_'); print(sc)
sc = s.str.contains('@'); print(sc)
sc = s.str.replace('@', '$'); print(sc)
sc = s.str.count(' '); print(sc)


