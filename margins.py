def bottom(ax):
    plt.draw()
    renderer = plt.gcf().canvas.get_renderer()
    fig_height = plt.gcf().get_size_inches()[1]

    # Get the height of the tick lines below the axis
    tick_line_heights = []
    for tickline in ax.xaxis.get_ticklines():
        if tickline.get_markersize() > 0:  # Only consider tick lines that are visible
            tick_line_height = tickline.get_markersize() / plt.gcf().dpi  # Convert from points to inches
            tick_line_heights.append(tick_line_height)
    max_tick_line_height = max(tick_line_heights) if tick_line_heights else 0
    print(f"max_tick_line_height: {max_tick_line_height / fig_height}")

    # Get the padding between tick labels and tick lines
    tick_padding = ax.xaxis.majorTicks[0].get_pad() / plt.gcf().dpi  # Convert from points to inches
    print(f"tick_padding: {tick_padding / fig_height}")

    # Get the max height of the x tick labels
    xticklabel_heights = []
    for label in ax.get_xticklabels():
        bbox = label.get_window_extent(renderer=renderer)
        xticklabel_height = bbox.height / plt.gcf().dpi  # Convert from pixels to inches
        xticklabel_heights.append(xticklabel_height)
    max_xticklabel_height = max(xticklabel_heights) if xticklabel_heights else 0
    print(f"max_xticklabel_height: {max_xticklabel_height / fig_height}")

    # Get the height of the x label
    x_label_bbox = ax.xaxis.get_label().get_window_extent(renderer=renderer)
    x_label_height = x_label_bbox.height / plt.gcf().dpi  # Convert from pixels to inches
    print(f"x_label_height: {x_label_height / fig_height}")

    # Get the padding of the x label
    x_label_padding = ax.xaxis.labelpad / plt.gcf().dpi  # Convert from points to inches
    x_label_padding = 4*x_label_padding # Should be 2x the padding
    print(f"x_label_padding: {x_label_padding / fig_height}")

    # Compute the smallest increment in relative height
    smallest_increment = 1 / plt.gcf().dpi / fig_height  # One pixel in inches divided by figure height in inches
    print(f"smallest_increment: {smallest_increment}")

    total_height = max_tick_line_height + max_xticklabel_height + x_label_height + x_label_padding + tick_padding
    relative_height = total_height / fig_height  # Scale to 1.0
    print(relative_height)
    return relative_height

