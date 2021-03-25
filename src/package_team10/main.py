import numpy as np
import statistical as st

if _name_ == '_main_':
    test = np.array((1, 1, 1.2, 1.3, 3.5, 2.0))
    dist = st.euclidean_distance([0,2,4], [1,3,5],test)
    print('Found distance {}'.format(dist))
