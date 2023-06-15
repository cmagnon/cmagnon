'''Collection of tools for deepsearching lists within lists'''
def print_lol(the_list, level=0):
    '''print all elements in a list nesting other lists'''
    for item in the_list:
        if isinstance(item, list):
            print_lol(item, level+1)
            
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(item)
            