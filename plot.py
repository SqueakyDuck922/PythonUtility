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

    # TODO testing only
    # plt.plot(df['timestamp'], df['close'], label='close')

    # TODO put back
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

        