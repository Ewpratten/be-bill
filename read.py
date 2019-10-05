
from textgenrnn import textgenrnn

generator = textgenrnn("./output.hdf5")

while True:
    generator.generate(3, temperature=1.0)