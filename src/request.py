import requests


class Request:
    def __init__(self, base_url='', auth=None) -> None:
        self.base_url = base_url
        self.auth = auth

    def post(self, url, data):
        # Send the POST request with application/x-www-form-urlencoded content
        args = {}
        if self.auth:
            args['auth'] = (self.auth['username'], self.auth['password'])
        response = requests.post(
            url=f"{self.base_url}/{url}",
            data=data,
            **args,
        )
        return response.text
