import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

import matplotlib.ticker as ticker


    
def plot_csv(csv_filepath):
    """
    Assumes a csv with dataset that consists of a datetime column called timestamp for x axis and other numeric columns to be plotted on y axis
    """

    #  Sample data
    # data = {
    #     'timestamp': pd.to_datetime(['2024-11-01 12:34:56', '2024-11-02 08:45:00', '2024-11-03 16:23:45']),
    #     'short_sma': [10, 20, 30],
    #     'long_sma': [15, 25, 35]
    # }
    # df = pd.DataFrame(data)

    df = pd.read_csv(csv_filepath)

    # testing only
    # plt.plot(df['timestamp'], df['close'], label='close')

    #Add each column to the plot (except timestamp which is on the x axis)
    for col in df.columns:

        if not col == 'timestamp':
            print(col)
            plt.plot(df['timestamp'], df[col], label=col)

    ax = plt.gca()  # Get current axes
    ax.xaxis.set_major_locator(ticker.MaxNLocator(nbins=10))  # Limit x axis lables to 10, else they are unreadable for large number of timestamps/tuples

    plt.xticks(rotation=45) 

    plt.tight_layout()  #ensures there is enough vertical space below the graph to display the x axis labels when angled down


    # Set the y axis limits from the min and max values of the variables to plot. Dont need to do this currently, range is set ok automatically
    # numeric_df = df.select_dtypes(include=['number'])  # Get df that exclues the timeframe
    # overall_min = numeric_df.min().min()
    # overall_max = numeric_df.max().max()
    # plt.ylim(overall_min, overall_max)



    # Disable offset on y-axis
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

    plt.legend()
    plt.show()

        

def plot_csv_multi_axis(csv_filepath):

    # This method is incomplete.

    df = pd.read_csv(csv_filepath)

    # Plotting
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot variable1 on primary y-axis
    ax1.plot(df['timestamp'], df['close'], color='blue', label='Variable 1')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Variable 1', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')


    # Create a second y-axis for variable2 and variable3
    ax2 = ax1.twinx()
    ax2.plot(df['timestamp'], df['mac_value_order_score'], color='red', label='Variable 2')
    # ax2.plot(df['time'], df['variable3'], color='orange', linestyle='--', label='Variable 3')
    ax2.set_ylabel('Variable 2 & 3', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # plt.tight_layout()
    plt.show()

    print("chjicken")


def plot_csv_multi_plots(csv_filepath):

    df = pd.read_csv(csv_filepath)


    # Create subplots
    fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

    axes[0].plot(df['timestamp'], df['close'], color='blue', label='Variable 1')
    axes[0].set_ylabel('Variable 1')
    axes[0].set_title('Variable 1')
    axes[0].legend()

    axes[1].plot(df['timestamp'], df['mac_value_order_score'], color='red', label='Variable 2')
    # axes[1].plot(df['time'], df['variable3'], color='orange', linestyle='--', label='Variable 3')
    axes[1].set_ylabel('Variable 2 & 3')
    axes[1].set_title('Variable 2 & 3')
    axes[1].legend()

    axes[2].plot(df['timestamp'], df['10'], color='green', label='10')
    axes[2].plot(df['timestamp'], df['20'], color='orange', linestyle='--', label='20')
    axes[2].plot(df['timestamp'], df['30'], color='orange', linestyle='--', label='30')
    axes[2].plot(df['timestamp'], df['40'], color='orange', linestyle='--', label='40')
    axes[2].set_ylabel('Variable 4')
    axes[2].set_title('Variable 4')
    axes[2].legend()



    # Add vertical lines where variable1 equals a specific value
    times_with_specific_value = df['timestamp'][df['mac_value_order_score'] == 1]

    for time_point in times_with_specific_value:
        for ax in axes:  # Add vertical line to all subplots
            ax.axvline(x=time_point, color='black', linestyle='--', alpha=0.7)

    times_with_specific_value = df['timestamp'][df['mac_value_order_score'] == -1]

    for time_point in times_with_specific_value:
        for ax in axes:  # Add vertical line to all subplots
            ax.axvline(x=time_point, color='red', linestyle='--', alpha=0.7)


    plt.show()

    print("chjicken")