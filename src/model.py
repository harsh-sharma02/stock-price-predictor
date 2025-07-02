from keras.models import Sequential
from keras.layers import Dense

def create_standard_model(input_dimension):
    model = Sequential()

    model.add(Dense(64, input_dim=input_dimension, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
