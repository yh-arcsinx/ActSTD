import argparse

parser = argparse.ArgumentParser(description='test')

parser.add_argument('--sparse', action='store_true', default=False, help='GAT with sparse version or not.')
parser.add_argument('--seed', type=int, default=72, help='Random seed.')
parser.add_argument('--epochs', type=int, default=10000, help='Number of epochs to train.')
parser.add_argument("--tpp", type=str, choices=["poisson", "hawkes", "correcting", "neural"], default="neural")
parser.add_argument("--tpp_nocond", action="store_false", dest='tpp_cond')
args = parser.parse_args()

print(args.sparse)
print(args.seed)
print(args.epochs)
print(args.tpp)
print(args.tpp_cond)
#python test.py --tpp_nocond是用来激活或者不激活 在代码里面他叫tpp_cond