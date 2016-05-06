# Agood example of ImportError
# Use this when you want to fall back to a secondary library(that has a common API but may
# is less desirable in terms of efficiency for example)
# try:
#   from lxml import etree
# except ImportError:
#   import xml.etree.ElementTree as etree

# when to use from and import
# import just imports a module
# from import just imports a specific thing from a module


SUFFIXES ={ 1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
# So this may look weird to you, but this is essentially defining
# an array of two arrays, with keys of 1000 and 1024 respectively.
# To access an array, you simply call SUFFIXES[1000]

# Why approximate_size? Well I want the approximate size of a file
# So I need to know whether a kilobyte is 1000 or 1024
# Why these 2 parameters?
# To know whether a kb is 1000 or 1024, I pass in a flag that defaults
# to a true value
def approximate_size(size, a_kilobyte_is_1024_bytes = True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    -   size -- file size in bytes
    -   a_kilobyte_is_1024_bytes -- if True(default), use multiples of 1024
                                if False, use multiples of 1000

    Returns:
    -   string

    Raises:
    -   ValueError

    '''
    # When I want the file of a size, I need it to be positive for this to work
    if size < 0:
        raise ValueError('number must be non-negative')

    # Check the flag since I need my multiple to use this algorithm
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    # Get each suffix in SUFFIXES
    # The idea is if I am at 1025, I should use KiB, so I get 1024/1024 KiB
    # so when I get the first array element, I will divide by 1024
    # This works because I start off with a number of bytes. When I divide once,
    # I now have KiB, and if I divide once more, I get MiB
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        # Now, with size /= multiple, the size matches the current suffix unit
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)


    raise ValueError('number too large')
# End of approximate_size

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
