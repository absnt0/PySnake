import requests


class RESTClient(object):
    """
    This class is responsible for connecting, receiving and sending information to/from REST API
    """
    def __init__(self, address, port):
        self.address = address
        self.port = str(port)

    def check_connection(self):
        try:
            r = requests.get("{0}:{1}/color_schemes/".format(self.address, self.port))
        except requests.exceptions.RequestException:
            return False
        else:
            if r.status_code == 200:
                return True
            return False

    def get_color_schemes(self):
        try:
            r = requests.get("{0}:{1}/color_schemes".format(self.address, self.port))
        except requests.exceptions.RequestException:
            print("Server not found. Offline mode.")
        else:
            data = r.json()
            return data

    def get_high_scores(self):
        try:
            r = requests.get("{0}:{1}/high_scores".format(self.address, self.port))
        except requests.exceptions.RequestException:
            print("Server not found. Offline mode.")
        else:
            data = r.json()
            return data

    def add_high_score(self, name, score):
        try:
            data = {"name": name, "score": score}
            requests.post("{0}:{1}/high_scores/".format(self.address, self.port), json=data)
        except requests.exceptions.RequestException:
            print("Server not found. Offline mode.")
