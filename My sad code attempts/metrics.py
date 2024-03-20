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

# P@n

# AUC ROC

# IREOS

# SIREOS

# EM