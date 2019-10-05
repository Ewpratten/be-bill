from textgenrnn import textgenrnn
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", help="Input file containing text data", default="./allposts.txt")
ap.add_argument("-e", "--epochs", help="Number of epochs to train", default=3)
args = ap.parse_args()

args.epochs = int(args.epochs)

generator = textgenrnn()
generator.train_from_file(args.file, num_epochs=int(args.epochs))