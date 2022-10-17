import glob


class CertIterator:

    def __init__(self):
        self.cert_folder = glob. glob('C:/Users/driggerst/Python/CertHelper/certificates/*.pdf')

    def process_iteration(self):
        return self.cert_folder
