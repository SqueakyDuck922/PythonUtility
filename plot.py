import matplotlib.pyplot as plt
import matplotlib
import pandas as pd



def plot_csv(csv_filepath):
    print("plot_csv" + str(csv_filepath))

    df = pd.read_csv(csv_filepath)


    matplotlib.use('TkAgg')   #Required to actually see a graph when running in VSCode on MAC (doesnt need this when run via terminal on MAC)

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(df['short_sma'], df.index, label='short_sma')
    plt.plot(df['long_sma'], df.index, label='long_sma')
    plt.show()

    print("test block")