from numpy import exp


def sigmoid(a, steepness, midpoint):
    return 2/(1+exp(-steepness*(a-midpoint)))-1
