"""There are a few changes here... Nevertheless..."""

def take(count, iterable):
    """Take items from the front of an iterable

    Args:
        count: The maximum number of items to retrieve.
        iterable: The source series.

    Yields:
        At most 'count' items from 'iterable'.

    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    """Return unique items by eliminating duplicates

    Args:
        iterable: The source series.

    Yields:
        Unique elements in order from 'iterable'.
    """
    seen = set() #creates an empty set
    for item in iterable:
        if item in seen: #if we have seen the item before
            continue #control flow construct
        yield item
        seen.add(item)

def run_distinct():
    """This function helps us run the distinct() function

       Args:

       Returns:
    """
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)

def run_take():
    """This function helps us run the take() function

    Args:

    Returns:

    """
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)

def run_pipeline():
    """This function takes take() and distinct() and runs them as a pipeline

    Args:

    Returns:

    """
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)

if __name__ == '__main__':
    #run_take()
    #run_distinct()
    run_pipeline()



