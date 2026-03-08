# Copied from datascience/util.py at https://github.com/data-8/datascience

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def plot_normal_cdf(rbound=None, lbound=None, mean=0, sd=1):
    """Plots a normal curve with specified parameters and area below curve shaded
    between ``lbound`` and ``rbound``.

    Args:
        ``rbound`` (numeric): right boundary of shaded region

        ``lbound`` (numeric): left boundary of shaded region; by default is negative infinity

        ``mean`` (numeric): mean/expectation of normal distribution

        ``sd`` (numeric): standard deviation of normal distribution
    """
    shade = rbound is not None or lbound is not None
    shade_left = rbound is not None and lbound is not None
    inf = 3.5 * sd
    step = 0.1
    rlabel = rbound
    llabel = lbound
    if rbound is None:
        rbound = inf + mean
        rlabel = r"$\infty$"
    if lbound is None:
        lbound = -inf + mean
        llabel = r"-$\infty$"
    pdf_range = np.arange(-inf + mean, inf + mean, step)
    plt.plot(pdf_range, stats.norm.pdf(pdf_range, loc=mean, scale=sd), color='k', lw=1)
    cdf_range = np.arange(lbound, rbound + step, step)
    if shade:
        plt.fill_between(cdf_range, stats.norm.pdf(cdf_range, loc=mean, scale=sd), color='gold')
    if shade_left:
        cdf_range = np.arange(-inf+mean, lbound + step, step)
        plt.fill_between(cdf_range, stats.norm.pdf(cdf_range, loc=mean, scale=sd), color='darkblue')
    plt.ylim(0, stats.norm.pdf(0, loc=0, scale=sd) * 1.25)
    plt.xlabel('z')
    plt.ylabel(r'$\phi$(z)', rotation=90)
    plt.title(r"Normal Curve ~ ($\mu$ = {0}, $\sigma$ = {1}) "
              "{2} < z < {3}".format(mean, sd, llabel, rlabel), fontsize=16)
    plt.show()


