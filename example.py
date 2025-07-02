def max_dist(xc, yc):
    """
    Finds the maximum distance between any two points
    in a collection of 2D points.  The points corresponding
    to this distance are also returned.

    Parameters
    ----------
    xc : list
        List of x-coordinates
    yc : list
        List of y-coordinates

    Returns
    -------
    max_dist : float
        Maximum distance
    xvals : list
        x-coodinates of two points
    yvals : list
        y-coordinates of two points

    """
    max_dist = 0.0  # initialize max_dist
    num_points = len(xc)  # number of points in collection
    for ii in range(num_points):
        for jj in range(num_points):
            dist = dist2d(xc[ii], yc[ii], xc[jj], yc[jj])
            if dist > max_dist:
                max_dist = dist
                xvals = [xc[ii], xc[jj]]
                yvals = [yc[ii], yc[jj]]
    return max_dist, xvals, yvals
