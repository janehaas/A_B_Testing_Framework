import numpy as np
from scipy import stats

control = np.random.normal(50, 5, 100)  # adoption baseline
test = np.random.normal(55, 5, 100)     # adoption with new pricing

t_stat, p_val = stats.ttest_ind(control, test)
print(f"T-Statistic: {t_stat}, P-Value: {p_val}")
