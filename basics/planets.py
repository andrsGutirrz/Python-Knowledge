import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--weight', '-w', type=float, required=False, help='Weight')

# parser.add_argument(name_or_flags=['--age', '-a'], type=int, required=True,
#                     help='Age')

args = parser.parse_args()

print(args.weight)
