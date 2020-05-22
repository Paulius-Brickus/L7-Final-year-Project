# 3_Training_model.py
# author: Harrison Kinsley/ sentdex
# date 3/05/2020
# 
#
#references: - Harrison Kinsley/ sentdex
#link: https://github.com/Sentdex/pygta5/blob/master/Tutorial%20Codes/Part%208-13%20code/train_model.py 
#this program trains the CNN with the driving data

import numpy as np
from alexnet import alexnet
WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'Driving_data-car-{}-{}-{}-epochs-300K-data.model'.format(LR, 'alexnetv2',EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

hm_data = 22

for i in range(EPOCHS):
    
    for i in range(1,hm_data+1):
        training_data = np.load('Driving_data.npy'.format(i))
        train = training_data[:-100]
        test = training_data[-100:]
        X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
        Y = [i[1] for i in train]
        test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
        test_y = [i[1] for i in test]
        model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
            snapshot_step=500, show_metric=True, run_id=MODEL_NAME)
        model.save(MODEL_NAME)



# tensorboard --logdir=foo:C:\Users\Yamato\Desktop\working\log





