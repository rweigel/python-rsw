import math
import warnings

# TODO: Consider adding option for method described in
# http://vis.stanford.edu/files/2010-TickLabels-InfoVis.pdf

def demo():
    
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    
    print('\nscale(33, 99)')
    pp.pprint(scale(33, 99))

    print('\nscale(0.093, 0.8)')
    pp.pprint(scale(0.093, 0.8))

    print('\nscale(2, 21)')
    pp.pprint(scale(2, 21))

    print('\nscale_mpl(2, 21)')
    pp.pprint(scale_mpl(2, 21))

    print('\nscale(2, 21, num_ticks=6)')
    pp.pprint(scale(2, 21, num_ticks=6))

def scale_mpl(min_value, max_value):
    """Matplotlib axis ticks"""
    
    from matplotlib.figure import Figure
    ax = Figure().add_subplot(111)
    ax.plot([min_value, max_value],[min_value, max_value])

    #from matplotlib import pyplot as plt
    #plt.plot([min_value, max_value],[min_value, max_value])
    #print(plt.gca().get_xticks())
    
    ticks = list(ax.get_xticks())
    xlim = ax.get_xlim()
    if ticks[0] < xlim[0]:
        del ticks[0]
    if ticks[-1] < xlim[1]:
        del ticks[-1]
        
    s = {}
    s['ticks'] = list(ticks)
    s['tick_spacing'] = ticks[1] - ticks[0]
    s['tick_min'] = ticks[0]
    s['tick_max'] = ticks[-1]
    s['num_ticks'] = len(ticks)
    s['min_value'] = min_value
    s['max_value'] = max_value

    return s


def ticks(min_value, max_value, **kwargs):
    """Return tick list from scale()"""
    
    s = scale(min_value, max_value, kwargs)
    return s.ticks


def scale(min_value, max_value, **kwargs):
    """Compute tick min, max, and spacing
    
    Demo
    ----
    import scaleticks
    scaleticks.demo()
    
    Usage
    -----
    
    scale(min_value, max_value, **kwargs) 
    
    Compute 6 ticks given min/max values

        s = scale(min_value, max_value) 

    Compute num_ticks

        s = scale(min_value, max_value, num_ticks=N)
    
    Choose best number of ticks
    
      s = scale(min_value, max_value, min_ticks=N1, max_ticks=N2)

    In this case,

      s = scale(min_value, max_value, num_ticks=N)

    is called for for N = range(N1, N2 + 1) and the ticks associated with
    the N that gives the smallest total gap between tick limits and value
    limits
    
        gap = (s["max_value"] - s["min_tick"]) + (s["min_value"] - s["min_tick"])
    
    is used. If gap is the same for one or more N, ticks for lowest N are
    returned.

    Based on algorithm at
    https://stackoverflow.com/questions/8506881/nice-label-algorithm-for-charts-with-minimum-ticks
    
    """

    min_ticks = kwargs['min_ticks'] if 'min_ticks' in kwargs else 6
    max_ticks = kwargs['max_ticks'] if 'max_ticks' in kwargs else 10
    num_ticks = kwargs['num_ticks'] if 'num_ticks' in kwargs else 6
    
    assert not ('max_ticks' in kwargs and 'min_ticks' not in kwargs), "min_ticks must be given if max_ticks given."
    assert not ('min_ticks' in kwargs and 'max_ticks' not in kwargs), "max_ticks must be given if min_ticks given."   
    assert min_ticks > 2, "Required: min_ticks > 2"
    assert max_ticks >= min_ticks, "Required: max_ticks >= min_ticks"
    
    if 'num_ticks' in kwargs and 'min_ticks' in kwargs:
        warnings.warn('Ignoring min_ticks because num_ticks given')
    if 'num_ticks' in kwargs and 'max_ticks' in kwargs:
        warnings.warn('Ignoring max_ticks because num_ticks given')

    d, s, S = [], {}, []
    
    if 'num_ticks' in kwargs or min_ticks == max_ticks:
        # s = scale(min_value, max_value)
        # s = scale(min_value, max_value, num_ticks=num_ticks)
        value_range = nice_number(max_value - min_value, False)
        s["tick_spacing"] = nice_number(value_range / (num_ticks - 1), True)
        s["tick_min"] = math.floor(min_value / s["tick_spacing"]) * s["tick_spacing"]
        s["tick_max"] = math.ceil(max_value / s["tick_spacing"]) * s["tick_spacing"]
    else:
        # s = scale(min_value, max_value, min_ticks, max_ticks)
        for i in range(0, max_ticks - min_ticks):
            N = min_ticks + i
            print(N)
            s = scale(min_value, max_value, num_ticks=N)
            S.append(s)
            d.append(min_value - s["tick_min"] + s["tick_max"] - max_value)
            print(s)
            if i == 0:
                dmin = d[0]
                imin = i
            if d[i] < dmin:
                imin = i

        s = S[imin]

    # Number of ticks
    N = round((s["tick_max"] - s["tick_min"])/s["tick_spacing"])
    
    ticks = []
    for i in range(0, N + 1):
        tick = s["tick_min"] + i*s["tick_spacing"]
        ticks.append(tick)

    s['num_ticks'] = len(ticks)
    s['ticks'] = ticks
    s['min_value'] = min_value
    s['max_value'] = max_value

    return s

def nice_number(value_range, use_round):
    
    exponent = math.floor(math.log10(value_range));
    fraction = value_range / math.pow(10, exponent);

    if (use_round):
        if (fraction < 1.5):
            nice_fraction = 1
        elif (fraction < 3):
            nice_fraction = 2
        elif (fraction < 7):
            nice_fraction = 5;
        else:
            nice_fraction = 10;
    else :
        if (fraction <= 1):
            nice_fraction = 1
        elif (fraction <= 2):
            nice_fraction = 2
        elif (fraction <= 5):
            nice_fraction = 5
        else:
            nice_fraction = 10

    return nice_fraction * math.pow(10, exponent)
