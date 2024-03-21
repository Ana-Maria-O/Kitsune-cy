import matplotlib.pyplot as plt
import something1
import sklearn.metrics

# The labeled dataset
LABELED_DATA = ""

# The dataset with results
RESULT_DATA = ""

# Open the file with labeled data
ld = open(LABELED_DATA, 'r')

# Open the file with result data
rd = open(RESULT_DATA, 'r')

def number_of_true_positives(results, truth) -> float:
    # Implementation requires to know the format of the results and the labeled data
    return 0

def number_of_positives(data) -> float:
    # Implementation requires to know the format of the results data
    return 0

def number_of_true_negatives(results, truth) -> float:
    # Implementation requires to know the format of the results and the labeled data
    return 0

def number_of_negatives(data) -> float:
    # Implementation requires to know the format of the results data
    return 0

def number_of_false_positives(results, truth) -> float:
    # Implementation requires to know the format of the results and the labeled data
    return 0

def number_of_false_negatives(results, truth) -> float:
    # Implementation requires to know the format of the results and the labeled data
    return 0

# Function for plotting and saving some data in a simple  line graph
def plot_data(x_axis: list, y_axis: list, destination_file: str):
    # Make the plot
    plt.plot(x_axis, y_axis)

    # Save the plot in a file
    plt.savefig(destination_file)

# Call Kitsune and output the file name of the results. Kept in a separate function for easy changes based on output format
def call_Kitsune(dim=0, process_number=0, file_name="", fm=0, ad=0):
    return None


# True positive rate
def true_positive_rate(results, truth) -> float:
    # Get the number of true positives in the results
    true_pos = number_of_true_positives(results, truth)

    # Get the number of all positives in ground truth data
    all_pos = number_of_positives(truth)

    # Return the true positive rate
    return true_pos / all_pos

# True negative rate
def true_negative_rate(results, truth) -> float:
    # Get the number of true negatives
    true_neg = number_of_true_negatives(results, truth)

    # Get the number of all negatives in ground truth data
    all_neg = number_of_negatives(truth)

    # Return the true negative rate
    return true_neg / all_neg

# False positive rate
def false_positive_rate(results, truth) -> float:
    # Get the number of false positives in the results
    false_pos = number_of_false_positives(results, truth)

    # Get the number of all negatives in ground truth data
    all_neg = number_of_negatives(truth)

    # Return the false positive rate
    return false_pos / all_neg

# False negative rate
def false_negative_rate(results, truth) -> float:
    # Get the number of false negatives in the results
    false_neg = number_of_false_negatives(results, truth)

    # Get the number of all positives in ground truth data
    all_pos = number_of_positives(truth)

    # Return the false positive rate
    return false_neg / all_pos

# Accuracy
def accuracy(results, truth) -> float:
    # Get number of true negatives in results
    true_neg = number_of_true_negatives(results, truth)

    # Get the number of true positives in results
    true_pos = number_of_true_positives(results, truth)

    # Size of the dataset
    # depends on the format of the results and ground truth data
    total_data_number = 0

    # Return the accuracy of the results
    return (true_neg + true_pos) / total_data_number

# Precision
def precision(results, truth) -> float:
    # Get the number of true positives in results
    true_pos = number_of_true_positives(results, truth)

    # Get the number of all positives in results
    all_pos = number_of_positives(results)

    # Return the precision of the results
    return true_pos / all_pos

# F1-score
# Recall = True Positive Rate
def f1_score(precision, recall) -> float:
    return 2 * (precision * recall) / (precision + recall)

# Robustness

# Need to figure out if I want to replace this with AE size
# truth is the same as with the previous functions
# dim_start and dim_end form the range of dimensionalities to be used
def dim_robustness(truth, dim_start: int, dim_end: int):
    precisions = []
    dims = range(dim_start, dim_end + 1)

    # For each dimension to be tested, we get the Kitsune result data and compute its precision, then we add it to a list of precision values
    for dim in dims:
        result = call_Kitsune(dim=dim)
        precisions.append(precision(result, truth))
    
    # We make the robustness plot
    plot_data(dims, precisions, "dim_robustness.png")

# truth is as with the previous functions
# I think i need to know the format of the results first lol
# size_start and size_end form the range of sizes of the test data to be used
# 0 <= outlier_proportion <= 1 is the constant that shows what % of the training data is malignant data
def size_robustness(truth, size_start: int, size_end: int):
    precisions = []
    sizes = range(size_start, size_end + 1)

    # For each size to be tested, we get the Kitsune result data and compute its precision, then we add it to a list of precision values
    for size in sizes:
        result = call_Kitsune(process_number=size)
        precisions.append(precision(result, truth))
    
    # We make the robustness plot
    plot_data(sizes, precisions, "size_robustness.png")

# results and truth are as with the previous functions
# datas is a n array with the different files that correspond to different outlier proportions
# noise_range is the list of noise proportion in the training data to be used
# fms and ads are the lists with the numbers of instances for learning the feature mapping and the numbers for instances for training the anomaly detector respectively for each file
def noise_robustness(datas: list, truth, noise_range: list, fms: list, ads: list):
    precisions = []
    index = 0

    # For each dataset with different noise proportions, get the Kitsune result data and compute its precision, then we add it to a list of precision values
    for data in datas:
        result = call_Kitsune(file_name= data, fm=fms[index], ad=ads[index])
        precisions.append(precision(result, truth))
        index += 1

    # We make the robustness plot
    plot_data(noise_range, precisions, "noise_robustness.png")

# P@n
def p_at_n(results, truth) -> float:
    # Get the number of malicious packets from the data
    malicious_number = number_of_negatives(truth)

    # Get the malicious_number packets with the highest anomaly score in the result data
    # Depends on the implementation of the result data???
    result_negatives = []

    # Get how many of the top most outlier-y packets are actually malicious
    real_negatives = number_of_true_negatives(result_negatives, truth)

    # Compute P@n
    return real_negatives / malicious_number

# AUC ROC
def auc_roc(results, truth) -> float:
    # May need to do some pre-processing herer or smth
    return sklearn.metrics.roc_auc_score(results, truth)

# IREOS

# SIREOS

# EM