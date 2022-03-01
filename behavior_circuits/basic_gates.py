from numpy.linalg import norm
from numpy import tanh, sign, abs


def check_gate_input(a, b):
    """Function which checks that the inputs of a gate are of the expected type and range.

    Args:
        a (float): first input
        b (float): second input

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if norm(a) > 1 or norm(b) > 1:
        raise ValueError(
            "The Input of a behavior circuit must be within [-1,1]")
    else:
        return True


def or_gate(a, b):
    """Function abstracting the locigal or gate to the range of [-1,1].

    Args:
        a (float): first input
        b (float): second input

    Returns:
        float: output of or gate operation
    """
    check_gate_input(a, b)
    return a+b-a*b*tanh(a+b)/tanh(2)


def and_gate(a, b):
    """Function abstracting the locigal and gate to the range of [-1,1].

    Args:
        a (float): first input
        b (float): second input

    Returns:
        float: output of and gate operation
    """
    check_gate_input(a, b)
    return a*b*tanh(a+b)/tanh(2)


def compare_gate(a, b):
    """Analogical gate whose output depends on the difference between the first and second input.
       If the first input is larger than the second the output is positive, otherwise it is
       negative. 

    Args:
        a (float): first input
        b (float): second input

    Returns:
        float: output of the gate operation comparing the both inputs
    """
    check_gate_input(a, b)
    return or_gate(a, -b)


def invoke_gate(a, b):
    """Function modelling one input (a) invoking a second input (b).
       If the invoking is at either -1,0,1 the output is also at that value. 
       The second input can only modify the output between those values.

    Args:
        a (float): invoking input
        b (float): second input

    Returns:
        float: output of the invoke gate operation
    """
    check_gate_input(a, b)
    return and_gate(a, or_gate(a, b))


def prevail_gate(a, b):
    """Function modelling one input (a) prevailing over a second input (b) the larger it gets.
       In the absence of the prevailing input the output is equal to the second input.

    Args:
        a (float): prevailing input
        b (float): default input

    Returns:
        float: output of xor gate operation
    """
    check_gate_input(a, b)
    return or_gate(a, or_gate(a, b))


def xor_gate(a, b):
    """Function abstracting the locigal xor gate to the range of [-1,1].

    Args:
        a (float): first input
        b (float): second input

    Returns:
        float: output of xor gate operation
    """
    check_gate_input(a, b)
    return compare_gate(a, b)*compare_gate(a, b)*or_gate(a, b)


def not_gate(a, smoothness=0):
    """Function abstracting the locigal xor gate to the range of [-1,1].
       Since this creates discontinous around zero the function can be smoothed.

    Args:
        a (float): Input that is to be inverted using not gate
        smoothnss (float, optional): Smoothness of the not oprations. Defaults to 0.

    Returns:
        float: Inverted value
    """
    check_gate_input(a, 0)
    if a == 0:
        a = 1
    else:
        if smoothness == 0:
            return sign(a) * (1 - abs(a))
        else:
            return tanh(a*smoothness)/tanh(smoothness) * (1-abs(a))


def amp_gate(a, b):
    """Function modeling one input regulating the flow of another similar to an amplifier.
       Negative amplification changes the sign of the signal.
       Since this operation is symmetrical it does not matter which input is the 'signal' 
       and which the 'amplificiation'.

    Args:
        a (float): first input
        b (float): second input

    Returns:
        float: output of amp gate operation
    """
    check_gate_input(a, b)
    return a * b
