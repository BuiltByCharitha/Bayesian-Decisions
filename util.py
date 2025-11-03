def mean(np_array):
    '''Your code here'''
    sum = 0
    n_samples = 0
    for value in np_array:
        sum += value
        n_samples += 1
    ans = sum/n_samples
    '''Stop coding here'''    
    return ans

def stdev(np_array, mu=None):
    '''Your code here'''
    if mu == None:
        mu = mean(np_array)
    n_samples = len(np_array)
    variance = 0
    for value in np_array:
        variance += (value - mu) ** 2
    variance /= n_samples
    ans = variance ** 0.5
    '''Stop coding here'''    
    return ans

def sampleMean(np_array):
    ''' Each column represents a feature'''
    '''Your code here'''
    ans = []
    n_samples = len(np_array)
    n_features = len(np_array[0]) # Number of features
    for j in range(n_features):
        col_sum = 0
        for i in range(n_samples):
            col_sum += np_array[i][j]
        col_mean = col_sum/n_samples 
        ans.append(col_mean)
    '''Stop coding here'''    
    return ans

def covariance(np_array):
    ''' Each column represents a feature'''
    '''Your code here'''
    n_samples = len(np_array)
    n_features = len(np_array[0])  
    feature_means = sampleMean(np_array)
    ans = [[0 for _ in range(n_features)] for _ in range(n_features)]
    for i in range(n_features):
        for j in range(n_features):
            sum = 0
            for k in range(n_samples):
                sum += (np_array[k][i] - feature_means[i]) * (np_array[k][j] - feature_means[j])
            ans[i][j] = sum/(n_samples - 1)
            # Divide by (n-1) for sample covariance (it matches with the inbuilt method of numpy)
    '''Stop coding here'''    
    return ans
