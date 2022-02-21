def is_criticality_balanced(temperature, neutrons_emitted):
    a=False
    if((temperature<800) and (neutrons_emitted>500) and (temperature*neutrons_emitted<500000)):
        a=True
    return a
 
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
 
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    area= float(temperature * neutrons_produced_per_second)
    if(area<0.9*threshold):
        return "LOW"
    elif(area<(threshold+0.1*threshold) and area>(threshold-0.1*threshold)):
        return "NORMAL"
    elif (area >0.9*threshold):
        return "DANGER"
