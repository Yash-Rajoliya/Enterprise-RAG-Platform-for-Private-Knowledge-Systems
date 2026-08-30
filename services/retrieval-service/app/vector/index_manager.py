import pickle


class IndexManager:

    @staticmethod
    def save(index, path):
        with open(path, "wb") as f:
            pickle.dump(index, f)

    @staticmethod
    def load(path):
        with open(path, "rb") as f:
            return pickle.load(f)