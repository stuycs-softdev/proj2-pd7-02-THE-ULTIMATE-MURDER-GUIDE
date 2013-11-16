from rauth import OAuth1Session

def search_yelp(term, location,
                consumer_key,
                consumer_secret,
                access_token,
                access_token_secret
                ):
    """
    searches yelp for a term at a location (city, state, ...)

    consumer_key, consumer_secret, access_token and access_token_secret can be
    accessed at http://www.yelp.com/developers/getting_started/api_access.
    They are not included for security reasons. 
    """
    path = 'http://api.yelp.com/v2/search'
    params = {'term':term, 'location':location}
    session = OAuth1Session(consumer_key, consumer_secret,
                            access_token, access_token_secret)
    return session.get(path, params=params).json()
