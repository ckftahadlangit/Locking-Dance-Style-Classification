"""
Given a training log file, plot something.
"""
import csv
import matplotlib.pyplot as plt

def main(training_log):
    with open(training_log) as fin:
        reader = csv.reader(fin)
        next(reader, None)  # skip the header
        val_accuracies = []
        val_losses = []
        accs = []
        losss = []
        top_5_accuracies = []
        top_5_loss = []
        ep = []
        cnn_benchmark = []  # this is ridiculous
        for epoch,acc,loss,top_k_categorical_accuracy,val_acc,val_loss,val_top_k_categorical_accuracy in reader:
            val_accuracies.append(float(val_acc))
            top_5_accuracies.append(float(val_top_k_categorical_accuracy))
            val_losses.append(float(val_loss))
            accs.append(float(acc))
            losss.append(float(loss))
            ep.append(int(epoch))

        # plt.plot(val_accuracies)
        # plt.plot(accs)
        # plt.xlabel("epoch")
        # plt.ylabel("accuracy")
        # plt.title("Accuracy of a 100-Frame Sequence")
        # plt.legend(['validation','training'], loc='lower right')

        plt.title("Loss of a 100-Frame Sequence")
        plt.plot(val_losses)
        plt.plot(losss)
        plt.ylabel("loss")
        plt.xlabel("epoch")
        plt.legend(['validation','training'], loc='upper right')

        # plt.plot(top_5_accuracies)
        plt.show()

if __name__ == '__main__':
# 80
    # lstm-training-1559101864.9963527
    # lstm-training-1559111706.9777737

# 90
    # lstm-training-1557119933.7469792
    # lstm-training-1557084128.406245

# 100
    # lstm-training-1559536009.4090457
    # lstm-training-1559532020.046076
    # # lstm-training-1559258359.0995955
    # # lstm-training-1559528792.43136

    training_log = 'data/logs/lstm-training-1559536009.4090457.log'
    main(training_log)