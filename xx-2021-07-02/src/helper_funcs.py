'''
Helper functions
'''

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm


PATH2DATA = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'data'))

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix'):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    import itertools
    import matplotlib.pyplot as plt

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    cmap = plt.cm.Blues
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
    
def load_chicken():
    df = pd.read_csv(os.path.join(PATH2DATA, "chicken.csv"))
    chicken = pd.DataFrame(df.groupby(["Chick", "Diet"])["weight"].mean().round().astype(int)).reset_index()

    diets = chicken.groupby(["Diet", "Chick"])["weight"].mean().reset_index()
    chick_diet1 = diets.loc[diets["Diet"]==1, "weight"].values
    chick_diet2 = diets.loc[diets["Diet"] == 2, "weight"].values
    chick_diet3 = diets.loc[diets["Diet"] == 3, "weight"].values
    chick_diet4 = diets.loc[diets["Diet"] == 4, "weight"].values

    return chicken, chick_diet1, chick_diet2, chick_diet3, chick_diet4


def data_exponential(y0=2.5, m=-4.0, C=2.0, n=25):
    import numpy as np
    np.random.seed(1234)
    # Generate some data based on these
    x_min, x_max = 0, 1
    x = np.linspace(x_min, x_max, n)

    def model_func(x, y0, m, C):
        return y0 * np.exp(m * x) + C

    y = model_func(x, y0, m, C)
    # Add noise
    y = y + 0.75 * (np.random.random(n) - 0.5)
    return x, y


def data_sigmoid():
    def sigmoid(x, k, x0):
        return 1.0 / (1 + np.exp(-k * (x - x0)))

    # Parameters of the true function
    n_samples = 150
    np.random.seed(42)
    true_x0 = 12 + np.random.normal()
    true_k = 0.5 + np.random.normal()
    sigma = 0.07

    # Build the true function and add some noise
    x = np.linspace(0, 30, num=n_samples)
    y = sigmoid(x, k=true_k, x0=true_x0)
    y_with_noise = y + sigma * np.random.randn(n_samples)
    return x, y_with_noise




def sample_body_heights(n=1, mu=172, sigma=12, return_params=False):
    if return_params:
        return np.round(norm.rvs(loc=mu, scale=sigma, size=n)).astype(int), mu, sigma
    else:
        return np.round(norm.rvs(loc=mu, scale=sigma, size=n)).astype(int)



def visualize_probabilities(p, loc, scale, tails='both', ax=None, xmin=-4, xmax=4, *agrs, **kwargs):
    valid_tails = ['both', 'lower', 'upper', 'inbetween']
    if tails not in valid_tails:
        print('Error: Please specify the "tail" arugment properly!')
        print(valid_tails)
        return
    alpha = 0.4
    x = np.linspace(xmin,xmax, 1000)
    y = norm.pdf(x, loc, scale)

    upper_za = norm.ppf(1-p,loc,scale)
    lower_za = norm.ppf(p,loc,scale)

    if ax is None:
        fig, ax = plt.subplots(*agrs, **kwargs)
    ax.plot(x, y)
    ax.grid(axis='x')

    if tails == 'both':
        upper_za = norm.ppf(1-p/2,loc,scale)
        lower_za = norm.ppf(p/2,loc,scale)
        ax.vlines(upper_za, ymin=0, ymax=norm.pdf(upper_za, loc, scale))
        ax.fill_between(x, y1=0, y2=y, where=x>upper_za, color='b0', alpha=alpha)
        ax.vlines(lower_za, ymin=0, ymax=norm.pdf(lower_za, loc, scale))
        ax.fill_between(x, y1=0, y2=y, where=x<lower_za, color='b0', alpha=alpha)
    elif tails == 'inbetween':
        p = 1-p
        upper_za = norm.ppf(1-(p/2),loc,scale)
        lower_za = norm.ppf(p/2,loc,scale)
        ax.vlines(upper_za, ymin=0, ymax=norm.pdf(upper_za, loc, scale))
        ax.vlines(lower_za, ymin=0, ymax=norm.pdf(lower_za, loc, scale))
        ax.fill_between(x, y1=0, y2=y, where=(x<upper_za) & (x>lower_za), color='b0', alpha=alpha)
        p = 1-p
    elif tails == 'upper':
        ax.vlines(upper_za, ymin=0, ymax=norm.pdf(upper_za, loc, scale))
        ax.fill_between(x, y1=0, y2=y, where=x>upper_za, color='b0', alpha=alpha)
    elif tails == 'lower':
        ax.vlines(lower_za, ymin=0, ymax=norm.pdf(lower_za, loc, scale))
        ax.fill_between(x, y1=0, y2=y, where=x<lower_za, color='b0', alpha=alpha)
    else:
        pass
    ax.set_title(f'The marked area correspsonds to {np.round(p*100,1)}% of the total area under the curve', size=18)
