def ft_filter(function, iterable):
    """
    Construct an iterator from those elements of iterable for which function returns true.
    
    iterable may be either a sequence, a container which supports iteration, or an iterator.
    If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.
    """
    if function is None:
        return [item for item in iterable if item]
    else:
        return [item for item in iterable if function(item)]


