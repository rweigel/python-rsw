
def fig_position(r=0, c=0, w=None, h=None):
  import matplotlib

  print(f"Using backend: {matplotlib.get_backend()}")

  # To modify figure position on screen and size.
  # Window managers do not typically respect figsize, so use mngr.resize() to
  # adjusts the window size to keep aspect ratio correct.
  # See also https://stackoverflow.com/questions/7449585/how-do-you-set-the-absolute-position-of-figure-windows-with-matplotlib

  rcParams = matplotlib.rcParams
  if 'TKAgg' == matplotlib.get_backend():
    # Set position on screen
    mngr = matplotlib.pyplot.get_current_fig_manager()
    mngr.window.wm_geometry(f"+{r}+{c}")

    if w is None:
      w = rcParams['figure.figsize'][0]*rcParams['figure.dpi']
    if h is None:
      h = rcParams['figure.figsize'][1]*rcParams['figure.dpi']

    # Set aspect ratio
    import tkinter
    root = tkinter.Tk()
    root.withdraw()
    ws, hs = root.winfo_screenwidth(), root.winfo_screenheight()
    if h > hs:
      w = w * hs / h
      h = hs 
    # Also need to adjust for window manager decorations and tk gui controls.
    mngr.resize(w, h)
