"""
This type stub file was generated by pyright.
"""

"""
A buffered iterator for big arrays.

This module solves the problem of iterating over a big file-based array
without having to read it into memory. The `Arrayterator` class wraps
an array object, and when iterated it will return sub-arrays with at most
a user-specified number of elements.

"""
class Arrayterator(object):
    """
    Buffered iterator for big arrays.

    `Arrayterator` creates a buffered iterator for reading big arrays in small
    contiguous blocks. The class is useful for objects stored in the
    file system. It allows iteration over the object *without* reading
    everything in memory; instead, small blocks are read and iterated over.

    `Arrayterator` can be used with any object that supports multidimensional
    slices. This includes NumPy arrays, but also variables from
    Scientific.IO.NetCDF or pynetcdf for example.

    Parameters
    ----------
    var : array_like
        The object to iterate over.
    buf_size : int, optional
        The buffer size. If `buf_size` is supplied, the maximum amount of
        data that will be read into memory is `buf_size` elements.
        Default is None, which will read as many element as possible
        into memory.

    Attributes
    ----------
    var
    buf_size
    start
    stop
    step
    shape
    flat

    See Also
    --------
    ndenumerate : Multidimensional array iterator.
    flatiter : Flat array iterator.
    memmap : Create a memory-map to an array stored in a binary file on disk.

    Notes
    -----
    The algorithm works by first finding a "running dimension", along which
    the blocks will be extracted. Given an array of dimensions
    ``(d1, d2, ..., dn)``, e.g. if `buf_size` is smaller than ``d1``, the
    first dimension will be used. If, on the other hand,
    ``d1 < buf_size < d1*d2`` the second dimension will be used, and so on.
    Blocks are extracted along this dimension, and when the last block is
    returned the process continues from the next dimension, until all
    elements have been read.

    Examples
    --------
    >>> a = np.arange(3 * 4 * 5 * 6).reshape(3, 4, 5, 6)
    >>> a_itor = np.lib.Arrayterator(a, 2)
    >>> a_itor.shape
    (3, 4, 5, 6)

    Now we can iterate over ``a_itor``, and it will return arrays of size
    two. Since `buf_size` was smaller than any dimension, the first
    dimension will be iterated over first:

    >>> for subarr in a_itor:
    ...     if not subarr.all():
    ...         print(subarr, subarr.shape)
    ...
    [[[[0 1]]]] (1, 1, 1, 2)

    """
    def __init__(self, var, buf_size=...) -> None:
        ...
    
    def __getattr__(self, attr):
        ...
    
    def __getitem__(self, index):
        """
        Return a new arrayterator.

        """
        ...
    
    def __array__(self):
        """
        Return corresponding data.

        """
        ...
    
    @property
    def flat(self):
        """
        A 1-D flat iterator for Arrayterator objects.

        This iterator returns elements of the array to be iterated over in
        `Arrayterator` one by one. It is similar to `flatiter`.

        See Also
        --------
        Arrayterator
        flatiter

        Examples
        --------
        >>> a = np.arange(3 * 4 * 5 * 6).reshape(3, 4, 5, 6)
        >>> a_itor = np.lib.Arrayterator(a, 2)

        >>> for subarr in a_itor.flat:
        ...     if not subarr:
        ...         print(subarr, type(subarr))
        ...
        0 <type 'numpy.int32'>

        """
        ...
    
    @property
    def shape(self):
        """
        The shape of the array to be iterated over.

        For an example, see `Arrayterator`.

        """
        ...
    
    def __iter__(self):
        ...
    


