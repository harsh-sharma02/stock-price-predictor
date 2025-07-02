import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def normalize(data):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)

    return scaled_data, scaler

def plot_predictions(actual, predicted, output_path=None):
    plt.figure(figsize=(10, 6))

    plt.plot(actual, color='blue', label='Actual Price')
    plt.plot(predicted, color='red', label='Predicted Price')

    plt.title('Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Price')
    
    plt.legend()
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
