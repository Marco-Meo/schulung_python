# Importe
from argparse import ArgumentParser
from googlesearch import search

# Run on commandline: python search.py -q meonet

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.description = "Suchanfrage bei Google"
    parser.add_argument("-q", "--query", dest="query", default="meonet")
    args = parser.parse_args()
    query = args.query
    for j in search(query, tld="ch", num=10, stop=10, pause=2, lang='de'):
        print(j)