import numpy as np
from scipy.special import gamma

def t_distribution_pdf(x, nu):
    ceff = gamma((nu+1)/2.0)/(np.sqrt(nu*np.pi)*gamma(nu/2))
    density = ceff*(1+x**2/nu)**(-0.5*(nu+1))
    return density

def mean(data_points):
    return np.sum(data_points) / len(data_points)

def standard_deviation_of_means(data_points):
    return np.sqrt(np.sum((data_points-mean(data_points))**2)/(len(data_points)-1))/np.sqrt(len(data_points))

def find_t_crit(confidence_level, nu, x_start=0, x_end=20, num_points=10000):
    # continues adding to integral till reading t_crit for which the integral = 0.95
    x=np.linspace(x_start, x_end, num_points)
    y=t_distribution_pdf(x, nu)
    cdf=np.cumsum(y) * (x[1] - x[0])  # works bc all dx same size and this is what a loop would do
    target_half_prob=confidence_level / 2
    index = np.where(cdf >= target_half_prob)[0][0]
    return x[index]

def calc_t_score(sample_mean, pop_mean, sample_sigma):
    return (sample_mean - pop_mean) / sample_sigma

def hypothesis_test_1(data_points, pop_mean, confidence_level):
    sample_mean = mean(data_points)
    sample_std_dev = standard_deviation_of_means(data_points)
    t_crit = find_t_crit(confidence_level, len(data_points) - 1)
    t_score = calc_t_score(sample_mean, pop_mean, sample_std_dev)

    return abs(t_score) <= t_crit

def hypothesis_test_2(data_points, pop_mean, confidence_level):
    sample_mean = mean(data_points)
    sample_std_dev = standard_deviation_of_means(data_points)
    t_crit = find_t_crit(confidence_level, len(data_points) - 1)
    t_score = calc_t_score(sample_mean, pop_mean, sample_std_dev)
    
    if abs(t_score) > t_crit:
        if t_score > 0:
            return 1  #if mu >= mu_naught
        else:
            return -1  #if mu <= mu_naught
    else:
        return 0  # ifmu == mu_naught

math_test_scores = [92.64, 79.00, 84.79, 97.41, 93.68, 65.23, 84.50, 73.49, 73.97, 79.11]

hypothesis_test_1_result = hypothesis_test_1(math_test_scores, 75, 0.95)
hypothesis_test_2_result = hypothesis_test_2(math_test_scores, 75, 0.95)

if not hypothesis_test_1_result:
    if hypothesis_test_2_result == 1:
        print("Yay!")
    elif hypothesis_test_2_result == -1:
        print("Nay!")
else:
    print("No one cares!")