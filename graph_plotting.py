import matplotlib.pyplot as plt
import itertools


def feeling_temp_to_actual_temp(temperature_list, temperature_feel_list, time_list):

    # removes degrees symbol from each item
    temperature_list = [sub[:-1] for sub in temperature_list]
    temperature_feel_list = [sub[:-1] for sub in temperature_feel_list]

    # converts all items in list to integers
    temperature_list = [int(x) for x in temperature_list]
    temperature_feel_list = [int(x) for x in temperature_feel_list]

    x = [
        time_list[0][0],
        time_list[1][0],
        time_list[2][0],
        time_list[3][0],
        time_list[4][0],
        time_list[5][0],
        time_list[6][0],
        time_list[7][0],
        time_list[8][0],
    ]
    y = [
        temperature_list[0],
        temperature_list[1],
        temperature_list[2],
        temperature_list[3],
        temperature_list[4],
        temperature_list[5],
        temperature_list[6],
        temperature_list[7],
        temperature_list[8],
    ]

    y_of_perceived_temperature = [
        temperature_feel_list[0],
        temperature_feel_list[1],
        temperature_feel_list[2],
        temperature_feel_list[3],
        temperature_feel_list[4],
        temperature_feel_list[5],
        temperature_feel_list[6],
        temperature_feel_list[7],
        temperature_feel_list[8],
    ]

    plt.plot(x, y, label="Actual Temperature")
    plt.plot(x, y_of_perceived_temperature, label="Perceived Temperature")
    plt.ylabel("Temperature")
    plt.xlabel("Time")
    plt.title("Temperature compared to feels like temperature")
    plt.legend()
    return x, y, y_of_perceived_temperature
