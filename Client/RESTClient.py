import requests


class RESTClient(object):
    """
    This class is responsible for connecting, receiving and sending information to/from REST API
    """
    def __init__(self, address):
        self.address = address

    def check_connection(self):
        try:
            r = requests.get(self.address + "/color_schemes/")
        except requests.exceptions.RequestException:
            print("Server not found. Offline mode.")
            return False
        else:
            if r.status_code == 200:
                return True
            return False

    def get_color_schemes(self):
        try:
            r = requests.get(self.address + "/color_schemes")
        except requests.exceptions.RequestException:
            print("Server not found. Offline mode.")
        else:
            data = r.json()
            return data

    def get_high_scores(self):
        try:
            r = requests.get(self.address + "/high_scores")
        except requests.exceptions.RequestException:
            print("Server not found. Offline mode.")
        else:
            data = r.json()
            return data

    def add_high_score(self, name, score):
        pass

