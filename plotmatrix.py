def plotmatrix(*args, **kwargs):

    import numpy as np
    from matplotlib import pyplot as plt

    nin = len(args)
    
    if nin != 1 and nin != 3:
        raise Exception('Number of inputs must be 1 or 3')

    if nin == 1:
        Rl = None
        Cl = None
        M = args[0]
    
    if nin == 3:
        Rl = args[0]
        Cl = args[1]
        M = args[2]
        if len(Rl) != M.shape[0]:
            raise Exception('len(Rl) != number of rows in M.')
        if len(Cl) != M.shape[1]:
            raise Exception('len(Cl) != number of columns in M.')
    
    if 'fig' in kwargs:
        fig = kwargs['fig']
    else:
        fig = plt.gcf()

    if 'ax' in kwargs:
        ax = kwargs['ax']
    else:
        ax = plt.gca()

    if 'cmap' in kwargs:
        cmap = kwargs['cmap']
    else:
        #allint = False
        nc = 32
        #Ig = ~np.isnan(M)
        #vmin = np.min(M[Ig])
        #vmax = np.max(M[Ig])
        #if np.all(np.equal(M[Ig], np.int32(M[Ig]))):
            # TODO: 
            #nc = 1+np.unique(M).size
            #print(nc)
            #vmin = vmin - 0.5
            #vmax = vmax + 0.5
        cmap = plt.get_cmap('viridis', nc)

    if 'origin' in kwargs:
        origin = kwargs['origin']
    else:
        origin = 'lowerlleft'

    Ro = np.arange(0,M.shape[0]+1,1,dtype=np.int32)
    R = Ro - 0.5 # Shift so ticks centered on tile

    Co = np.arange(0,M.shape[1]+1,1,dtype=np.int32)
    C = Co - 0.5 # Shift so ticks centered on tile

    if origin == 'upperleft':
        ax.xaxis.tick_top()
        ax.xaxis.set_label_position('top') 
        # Plot so matrix plot same orientation as matrix display
        M = np.flipud(M)
        if R.shape[0] == 1:
             Rl = np.fliplr(Ro[0:-1])
        else:
             Rl = np.flipud(Ro[0:-1])
    
    # https://gist.github.com/jakevdp/8a992f606899ac24b711
    #ax.set_facecolor((0.9,0.9,0.9))
    ax.set_facecolor('w')
    ax.fill_between([C[0],C[-1],C[-1],C[0]],[R[0],R[0],R[-1],R[-1]], 
                    hatch="x", linewidth=0.0, alpha=0.0)
    if False:
        from matplotlib.colors import LogNorm
        norm = LogNorm(vmin=np.nanmin(M), vmax=np.nanmax(M))
        im = ax.pcolormesh(C, R, M, cmap=cmap, norm=norm)
    else:
        im = ax.pcolormesh(C, R, M, cmap=cmap)
        
    cb = fig.colorbar(im, ax=ax)

    # TODO: 
    # If len(C) <= 10, label every.
    # If len(C) <= 20, label every other.
    # If len(C) <= 40, label every fifth.
    # If len(C) <= 100, label every tenth.
    # etc.
    ax.set_yticks(Ro[0:-1])
    ax.set_xticks(Co[0:-1])

    if nin == 1:
        ax.set_xlabel('column index')
        ax.set_ylabel('row index')

    if Rl is not None:
        ax.set_yticklabels(Rl[Ro[0:-1]])
    if Cl is not None:
        ax.set_xticklabels(Cl[Co[0:-1]])

    if nin == 3:
        ax.set_xlabel('column label')
        ax.set_ylabel('row label')

    return im, ax, cb

if False:
    from IPython import get_ipython
    ipython = get_ipython()
    ipython.magic('reset -f -s')
    
    import numpy as np
    from matplotlib import pylab as plt

    Data = np.array([[1,2,3,np.nan],[4,5,6,4],[7,8,9,np.nan]])
    print(Data)
    
    Clo = np.array([0,5,10,30])
    Rlo = np.array([1,2,3])
    print(Rlo)
    print(Clo)
    # New last bin width = last bin width
    Cl = np.append(Clo,Clo[-1]+Clo[-1]-Clo[-2]) 
    Cl = np.append(Cl,Cl[-1]+Cl[-1]-Cl[-2])
    Rl = np.append(Rlo,Rlo[-1]+Rlo[-1]-Rlo[-2]) 
    Rl = np.append(Rl,Rl[-1]+Rl[-1]-Rl[-2]) 

    Rls = np.zeros(Rl.size-1)
    Cls = np.zeros(Cl.size-1)

    print(Rl)
    print(Cl)
    for i in range(0,len(Rl)-1):
        Rls[i] = Rl[i] - (Rl[i+1]-Rl[i])/2.0
    for i in range(0,len(Cl)-1):
        Cls[i] = Cl[i] - (Cl[i+1]-Cl[i])/2.0

    print(Cls)
    print(Rls)

    fig = plt.gcf()
    ax = plt.gca()
    im = ax.pcolormesh(Rl[0:-1], Cl[0:-1], np.transpose(Data))
    #im = ax.pcolormesh(Rls, Cls, np.transpose(Data))
    cb = fig.colorbar(im, ax=ax)
    #ax.set_ylim([Cls[0],Cls[-1]])
    #ax.set_xlim([Rls[0],Rls[-1]])

    
if True:
    import numpy as np
    from matplotlib import pylab as plt

    Data = np.array([[1,2,3,np.nan],[4,5,6,4],[7,8,9,np.nan]])
#    Data = np.array([[1,2,3,4],[4,5,6,4],[7,8,9,10]])
    Cl = np.array([0,1,10,30])
    Rl = np.array([0,2,4])   
    
    plt.close('all')

    plt.figure()
    plotmatrix(Data)


    plt.figure()
    plotmatrix(Rl, Cl, Data)

    plt.figure()
    im, cm, cb = plotmatrix(Data)

    fig = plt.figure()
    ax = plt.gca()
    cmap = plt.get_cmap('jet', 8)
    im, ax, cb = plotmatrix(Data, fig=fig, cmap=cmap, origin='upperleft')     
    
if False:
    import numpy as np
    from matplotlib import pyplot as plt

    from hapiclient.hapi import hapi
    from hapiclient.hapiplot import hapitime2datetime

    from hapiclient.util.datetick import datetick
    
    server     = 'http://hapi-server.org/servers/TestData/hapi'
    dataset    = 'dataset1'
    start      = '1970-01-01Z'
    stop       = '1970-01-01T00:00:11Z'
    parameters = 'spectra'
    opts       = {'logging': True, 'use_cache': True}
    data,meta = hapi(server, dataset, parameters, start, stop, **opts)
    
    Time = hapitime2datetime(data['Time'])

    Cl = np.array(meta['parameters'][1]['bins'][0]['centers'], dtype='d')
    Rl = Time
    M = data['spectra']
    fig = plt.gcf()

    ax = plt.gca()
    #im = ax.pcolormesh(Rl, Cl, np.transpose(M))
    im, ax, cb = plotmatrix(Cl, Rl, np.transpose(M))
    cb.set_label('z')
    fig = plt.gcf()
    datetick('x', (fig,ax))