import requests
from api import pokemon

def lambda_handler(event, context):
    # TODO implement
    message = 'Hello {} {}!'.format(event['first_name'],
                                    event['last_name'])

    return(pokemon.all())
