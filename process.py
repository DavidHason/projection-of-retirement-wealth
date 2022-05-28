import os
import argparse
from util.dataset import Dataset
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.ticker import MaxNLocator

def process(args):
    dataset_path = args.dataset

    if not os.path.isfile(dataset_path):
        print('cannot find dataset files')
        return
    save_dir = args.save
    if not os.path.isdir(save_dir):
        os.mkdir(save_dir)

    # prepare dataset
    dataset = Dataset(dataset_path)
    while True:
        print('input a ID of query customer or press "q" to exit')
        query_id = input()
        if query_id == 'q':
            break
        try:
            query_id = int(query_id)
        except:
            print('please input a ID of customer')
            continue

        query = dataset.get_data(query_id)
        if query is None:
            print('Cannot find customer with {}'.format(query_id))
            continue

        age0 = int(query.age)
        gen0 = query.gender
        bal0 = query.acc
        seifa0 = query.seifa
        if age0 >= 68:
            print('Age is {}, continue'.format(age))

        ages = [age0]
        balances = [bal0]
        bal = bal0
        for age in range(age0 + 1, 69):
            res, grw = dataset.get_projection(_id = query_id, _age=age, _gen = gen0, _seifa=seifa0, _bal = bal)
            if not res:
                print('Cannot find matched dataset in age = {}, gen = {}, seifa = {}'.format(age, gen0, seifa0))
                break
            bal += grw
            ages.append(age)
            balances.append(bal)

        # draw graph
        plt.plot(ages, balances, 'ro', color='blue')
        plt.xlabel('Age')
        plt.ylabel('Balance')
        plt.xticks(ages)
        plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('$%d'))
        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
        title = 'ID = {}, Age = {}, Gender = {}, Seifa = {}'.format(query_id, age0, gen0, seifa0)
        plt.title(title)
        save_name = '{}/{}.png'.format(save_dir, query_id)
        plt.savefig(save_name)
        plt.show()
        continue

def main():
    param = argparse.ArgumentParser()
    param.add_argument('--dataset', type = str, default= '../data/features_201712.xlsx', help = 'file name of feature excel file of previous year')
    param.add_argument('--save', type = str, default= 'projections', help = 'save directory for projection image')
    args = param.parse_args()
    return args

if __name__ == '__main__':
    args = main()
    process(args)

