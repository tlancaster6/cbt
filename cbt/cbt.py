import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('pids', type=str, nargs='+')
args = parser.parse_args()

# make sure we're on a PACE node
assert 'pace' in os.environ['HOSTNAME'], 'log into a PACE server before launching analysis'

