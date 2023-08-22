import pandas as pd
from keras.models import Model, load_model

# generate model with
# DM.py -r 1 --no_clf -cd UserDataExample.csv --ae -dm 20 --save_rep

path = "AE[20]_UserDataExample.h5"

# taken from https://github.com/paulzierep/DeepMicro/blob/f93cc954fe9d6ccef43daf54b51364db9420e3d3/DM.py#L243-L245
autoencoder = load_model(path)
layer_idx = int((len(autoencoder.layers) - 1) / 2)
encoder = Model(autoencoder.layers[0].input, autoencoder.layers[layer_idx].output)

X = pd.read_csv("data/UserDataExample.csv", sep=',', index_col=None, header=None)

print(X.shape)

# applying the learned encoder again on the same input to check it is persistent
X_conv = pd.DataFrame(encoder.predict(X))
X_conv.to_csv("results/AE[20]_UserDataExample_rep2.csv", index=False, header=None)
