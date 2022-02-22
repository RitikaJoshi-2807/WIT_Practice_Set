def is_criticality_balanced(temperature, neutrons_emitted):
    a=False
    if((temperature<800) and (neutrons_emitted>500) and (temperature*neutrons_emitted<500000)):
        a=True
    return a

    """Assess reactor efficiency zone.

    :param voltage: voltage value (integer or float)
    :param current: current value (integer or float)
    :param theoretical_max_power: power that corresponds to a 100% efficiency (integer or float)
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power=voltage*current
    percentage_value=(generated_power/theoretical_max_power)*100
    a="black"
    if ((percentage_value>=80)):
       a="green"
    elif((60<=percentage_value<=80)):
       a="orange"
    elif ((30<=percentage_value<=60)):
        a="red"
    return a


    
    """Assess and return status code for the reactor.

    :param temperature: value of the temperature in kelvin (integer or float)
    :param neutrons_produced_per_second: neutron flux (integer or float)
    :param threshold: threshold (integer or float)
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 90% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges ==  
    'DANGER'
    """
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    area= float(temperature * neutrons_produced_per_second)
    if(area<0.9*threshold):
        return "LOW"
    elif(area<(threshold+0.1*threshold) and area>(threshold-0.1*threshold)):
        return "NORMAL"
    elif (area >0.9*threshold):
        return "DANGER"
