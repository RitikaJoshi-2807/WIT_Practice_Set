# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
EXPECTED_BAKE_TIME= 40
PREPARATION_TIME=2
# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(cooking_time):
    """
    Return bake time remaining.
 
    This function takes one number representing cooking time.
    """
    return EXPECTED_BAKE_TIME-cooking_time
def preparation_time_in_minutes(number_of_layers):
    """
    Return preparation time in minutes.
 
    This function takes one number representing the number of layers and calculates the preparation time in minutes spent cooking one layer.
    """
    return PREPARATION_TIME*number_of_layers
    
# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.
 
    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time
    