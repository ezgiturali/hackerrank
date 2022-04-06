def print_formatted(number):
    # your code goes here
    l = len("{0:b}".format(number))
    # above l implies the space between each format .
    for i in range(1,number+1):
        print('{0:{l}d} {1:{l}o} {2:{l}X} {3:{l}b}'.format(i,i,i,i,l=l))
