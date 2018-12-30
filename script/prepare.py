import sys
import logging 
import csv

def parseTrainData(train_file, save_to_train_file):
    try:
        train_obj = open(train_file, 'r').readlines()
        save = open(save_to_train_file, 'w')
    except FileNotFoundError:
        logging.error("Wrong file or file path")
    
    save_to = csv.writer(save, delimiter='\t')
    trains = []
    for obj in train_obj:
        for line in obj.split(" "):
            trains.append([line.split('/')[0], line.split('/')[1].strip()])
    save_to.writerows(trains)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        logging.error("Wrong parameter!")
        exit(0)
    train_file = sys.argv[1]
    save_to_train_file = sys.argv[2]
    parseTrainData(train_file, save_to_train_file)
