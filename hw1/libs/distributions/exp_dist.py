import numpy as np
import matplotlib.pyplot as plt

class ExpDist():
    def __init__(self, **kwargs):
        self.__data_initialization(**kwargs)
        self.__generate_dataset()

    def __data_initialization(self, **kwargs):
        self.size = kwargs["size"]
        self.lam = kwargs["lam"]
        self.st_range = kwargs["st_range"]

        # optional: used only in hw1c.ipynb and hw2d.ipnyb
        self.alpha = kwargs["alpha"]
        self.beta = kwargs["beta"]

    def get_size(self):
        return self.size

    def get_lambda(self):
        return self.lam

    def __generate_dataset(self):
        """
        According to the docs for numpy.random.exponential,
        the input parameter beta, is 1/lambda
        for the definition of the exponential described in wikipedia.
        So, beta = 1 / lambda
        """
        beta = 1/ self.lam
        self.rand_exp = np.random.exponential(beta, self.size)

    def regenerate_dataset(self, new_alpha=None, n_size=None):
        if new_alpha is not None:
            self.alpha = new_alpha
        if n_size is not None:
            self.size = n_size
        self.__generate_dataset()

    def get_dataset(self):
        return self.rand_exp

    # optional usage
    def get_alpha(self):
        return self.alpha

    # optional usage
    def get_beta(self):
        return self.beta

    def plot_dataset(self):
        plt.hist(self.rand_exp, density=True, bins=self.size * 2, lw=100, alpha=.9)
        plt.show()
