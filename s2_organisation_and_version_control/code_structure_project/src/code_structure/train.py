from code_structure.data import MyDataset
from code_structure.model import Model


def train():
    dataset = MyDataset("data/raw")
    model = Model()
    # add rest of your training code here


if __name__ == "__main__":
    train()
