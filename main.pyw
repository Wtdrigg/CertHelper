from cert_iterator import CertIterator
from cert_parser import CertParser
from cert_parser_gui import ParserGUI

if __name__ == '__main__':
    iterator = CertIterator()
    parser = CertParser()
    ParserGUI(iterator, parser)
