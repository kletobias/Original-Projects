from keras.models import *
from keras.layers import *
from keras.regularizers import *
from sklearn.metrics import r2_score

# def construct_feedforward:

epochs = 5
num_neurons = 4
num_dense_layers = 10
reg = .000001
batch_size = 32

def simple_feedforward_model(num_neurons, num_dense_layers, reg,
                            loss='mean_absolute_percentage_error',
                            activation='relu', optimizer='rmsprop',
                            metrics=['accuracy']):
    model = Sequential()
    model.add(Dense(num_neurons, activation='relu', 
                          input_shape=(X_train.shape[1], ),
                          kernel_regularizer=l2(reg),
                          activity_regularizer=l1(reg)))

    for lyr in range(num_dense_layers):
        model.add(Dense(num_neurons, activation,
                        kernel_regularizer=l2(reg),
                        activity_regularizer=l1(reg)))

    model.add(Dense(1))

    model.summary()

    model.compile(optimizer=optimizer, 
                 loss=loss,
                 metrics=metrics)
    
    return model

model = simple_feedforward_model(num_neurons, num_dense_layers, reg)

history = model.fit(X_train, y_train,
                   epochs=epochs,
                   batch_size=batch_size,
                   verbose=0,
                   validation_data=(X_val, y_val))

plot_accuracy_loss(history.history)
pred = model.predict(X_test)
_r2 = r2_score(y_test, pred)

print('R-squared on test data = %.4f' % _r2)
