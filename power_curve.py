def plot_power_curve(sorted_power_W, save=False):
    """
    Plot the power curve over seconds, the power is plotted in W.
    
    Parameters:
    sorted_power_W (numpy.ndarray): Sorted power data.
    save (bool): If True, save the figure as a PNG file.
    """
    import matplotlib.pyplot as plt
    import numpy as np
    

    # Create a figure and axis
    fig, ax = plt.subplots()

    x = np.arange(len(sorted_power_W))

    # Plot the power data
    ax.plot(x, sorted_power_W, color='red')

    #ax.set_xscale('log')

    # Set labels and title
    ax.set_xlabel('time (s)')
    ax.set_ylabel('Power (W)')
    ax.set_title('Leistungskurve 1')
    
    # Add a legend
    #ax.legend()

    # color the area under the curve
    ax.fill_between(x, sorted_power_W, color='red', alpha=0.3)

    # Set grid
    ax.grid(True)

    # Set axis limits
    ax.set_xlim(0, len(sorted_power_W) - 1)
    ax.set_ylim(0, np.max(sorted_power_W) * 1.1)   

    # Show the plot
    plt.show()

    if save:
        # Save the figure
        fig.savefig('power_curve.png', dpi=300, bbox_inches='tight')
        print("Figure saved as 'power_curve.png'")

if __name__ == "__main__":
    import numpy as np
    test_data = np.array([1, 2, 5, 7, 10])
    plot_power_curve(test_data, save=False) # save = True to save the figure