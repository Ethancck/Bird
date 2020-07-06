import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-t', required=False, dest="threads",default=10, help='Enter threads - Default is 10')
parser.add_argument('--file','-f',required=True, dest="url_file",help='Enter path for domain/subdomain list')
parser.add_argument('--search', required=False, dest="flag",help='Give a flag for fitering ')
parser.add_argument('--output', required=False, dest="report", help='Enter report name for output')
args = parser.parse_args()