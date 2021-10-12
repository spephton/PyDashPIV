import numpy as np
import itertools
import json


#@array_function_dispatch(_roll_dispatcher)
def roll(a, shift, axis=None):
    """
    Roll array elements along a given axis.

    Elements that roll beyond the last position are re-introduced at
    the first.

    Parameters
    ----------
    a : array_like
        Input array.
    shift : int or tuple of ints
        The number of places by which elements are shifted.  If a tuple,
        then `axis` must be a tuple of the same size, and each of the
        given axes is shifted by the corresponding number.  If an int
        while `axis` is a tuple of ints, then the same value is used for
        all given axes.
    axis : int or tuple of ints, optional
        Axis or axes along which elements are shifted.  By default, the
        array is flattened before shifting, after which the original
        shape is restored.

    Returns
    -------
    res : ndarray
        Output array, with the same shape as `a`.

    See Also
    --------
    rollaxis : Roll the specified axis backwards, until it lies in a
               given position.

    Notes
    -----
    .. versionadded:: 1.12.0

    Supports rolling over multiple dimensions simultaneously.

    Examples
    --------
    >>> x = np.arange(10)
    >>> np.roll(x, 2)
    array([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
    >>> np.roll(x, -2)
    array([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])

    >>> x2 = np.reshape(x, (2,5))
    >>> x2
    array([[0, 1, 2, 3, 4],
           [5, 6, 7, 8, 9]])
    >>> np.roll(x2, 1)
    array([[9, 0, 1, 2, 3],
           [4, 5, 6, 7, 8]])
    >>> np.roll(x2, -1)
    array([[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 0]])
    >>> np.roll(x2, 1, axis=0)
    array([[5, 6, 7, 8, 9],
           [0, 1, 2, 3, 4]])
    >>> np.roll(x2, -1, axis=0)
    array([[5, 6, 7, 8, 9],
           [0, 1, 2, 3, 4]])
    >>> np.roll(x2, 1, axis=1)
    array([[4, 0, 1, 2, 3],
           [9, 5, 6, 7, 8]])
    >>> np.roll(x2, -1, axis=1)
    array([[1, 2, 3, 4, 0],
           [6, 7, 8, 9, 5]])

    """
    a = np.asanyarray(a)
    if axis is None:
        return roll(a.ravel(), shift, 0).reshape(a.shape) # ravel into 1d array and call again with axis = 0, then reshape and return

    else:
        axis = np.core.numeric.normalize_axis_tuple(axis, a.ndim, allow_duplicate=True) # sanitise axis param
        broadcasted = np.broadcast(shift, axis) # broadcasting is what numpy does to vectorise operations so they have the same dimensions. In this case it's fairly trivial: if there's only one entry in the shift tuple and more than one in the axis tuple, broadcast "stretches" shift so that it has the same dimensions as axis.
#        for foo, bar in broadcasted:
#        	print(foo, bar) # for some weird reason this was messing with the functionality. Is broadcasted a generator? Yes!
        if broadcasted.ndim > 1:
            raise ValueError(
                "'shift' and 'axis' should be scalars or 1D sequences")
        shifts = {ax: 0 for ax in range(a.ndim)} # make a dictionary to record the shift amount on each axis *of the input array* (we're accounting for the shift/axis tuples specifying shifts on less axes than the array has axes)
        for sh, ax in broadcasted: # for each shift specified on a given axis
            shifts[ax] += sh # look up that axis in the dictionary and add the shift amount to it

        rolls = [((slice(None), slice(None)),)] * a.ndim # Rolls is a list of tuples (of tuples of slice objects), the number of array dimensions long. 
        for ax, offset in shifts.items():
            offset %= a.shape[ax] or 1  # <authorcomment> If `a` is empty, nothing matters. </authorcomment> This line does two things: 
            # We modulo offset with the size of the array along the selected axis. If we're shifting 7 times along an axis size 3, that's like shifting once: don't bother looping through the whole array twice
            # <incorrect-guess> The 'or 1': applies if we're shifting by a number that divides the axis size. Given rolling an axis of size 1 also does nothing, just say it's size 1 in the code below so you don't do anything. </incorrect-guess>
            # <actually-happens>: if modulo assignment would fail due to attempt to divide by zero, modulo with one instead:
            # 	offset %= (size of axis in this dimension == 0) 
            # ^ would fail with div-by-zero error but "or 1" means instead we evaluate
            # 	offset %= 1 # (yields offset == 0)
            
            # it's not *smart*, python just evaluates the expression before assignment or, in this case, modulo assignment: '0 or 1' evaluates to '1' and modulo assignment works OK </actually-happens>
            if offset:
                # (original, result), (original, result)
                rolls[ax] = ((slice(None, -offset), slice(offset, None)),
                             (slice(-offset, None), slice(None, offset))) # Each entry in "rolls" now contains ((slice(None * 3), * 2),) objects if that axis is not being manipulated and this if that axis is being manipulated. It works as follows:
        	# Using slice(None, -offset) as an index in the original array selects all entries to that offset: the first 'len(array) - offset' elements
        	# slice(offset, None) as an index in the results array selects all entries from that offset to the end of the array.
        	# These, taken together, give us a way to map the first 'len - offset' entries from the original array to the last 'len - offset' entries of the results array. That just leaves getting the last 'offset' entries from the original array and moving those to the first 'offset' entries of the results array:
        	# slice(-offset, None) selects the last 'offset' entries of the original array
        	# slice(None, offset) selects the first 'offset' entries of the results array
        result = np.empty_like(a) # prime a results array
        for indices in itertools.product(*rolls):
            arr_index, res_index = zip(*indices)
            print(indices)
            print(f'array index: {arr_index}')
            print(f'result index: {res_index}')
            result[res_index] = a[arr_index]

# itertools.product() is probably a generator
# unpacking rolls should yield: every row of the array of tuples(of tuples of slice...) with a tuple corresponding to each axis of 'a'
# itertools.product() returns the cartesian product of the input arrays (and tuples?)

        return result


myArray = np.arange(3)
myBrray = np.arange(4)
my2dArray = myArray[:,np.newaxis] * myBrray
print(my2dArray)

print(roll(my2dArray, 1, (1,)))