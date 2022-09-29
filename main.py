#variable del tiempo de cocción y tiempo de preparación
EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2

#función que coja el tiempo en minutos que lleva la lasaña en el horno y devuelva el tiempo que le queda de cocción
def bake_time_remaining(elapsed_bake_time):
  return EXPECTED_BAKE_TIME - elapsed_bake_time

#función que calcule el tiempo de preparación cogiendo el numero de capas de la lasaña y multiplicando el tiempo que se tarda en preparar cada capa
def preparation_time_in_minutes(number_of_layers):
  return number_of_layers * PREPARATION_TIME


#función que calcule el tiempo que llevas cocinando la lasaña mediante la suma de la preparación y el tiempo que ya lleva en el horno
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
  return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time