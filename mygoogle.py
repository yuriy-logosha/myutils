import myrequests


class GoogleError(myrequests.RequestError):
    pass


def google_geocode(address, components='locality:riga|country:LV', language='ru', key=''):
    response = myrequests.requests.get(
        f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&components={components}&language={language}&key={key}')
    if not response.ok:
        raise GoogleError(response.reason)
    else:
        body = response.json()
        if 'status' in body:
            if body['status'] in ['OK', 'ZERO_RESULTS']:
                return body['results']
            else:
                raise GoogleError(body['status'], body['error_message'])
