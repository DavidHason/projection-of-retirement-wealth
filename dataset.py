import os
from  tqdm import tqdm
from util.Customer import Customer, Gender

import xlrd

COLUM_ID = 'A'      # colum name of ID
COLUM_POST = 'B'    # colum name of post code
COLUM_SEIFA = 'C'   # colum name of seifa
COLUM_GEN = 'D'     # colum name of gender
COLUM_AGE = 'E'     # colum name of age
COLUM_PREV_ACC = 'F'    # colum of prev acc balance
COLUM_ACC = 'G'     # colum name of acc balance
COLUM_GROWTH = 'H'  # colum name of acc growth

class Dataset():
    def __init__(self, dataset_path):
        self.customs = dict()
        if not os.path.isfile(dataset_path) :
            print('Cannot fine dataset file')
        else:
            self.data_path= dataset_path
            self.nID = -1
            self.nPost = -1
            self.nSeifa = -1
            self.nGend = -1
            self.nAge = -1
            self.nPrevAcc = -1
            self.nAcc = -1
            self.nGrowth = -1
            self.load_dataset()

    '''
    @load dataset from exel dataset
    @ return: customers
    '''
    def load_dataset(self):
        # read a dataset of present year
        print('loading dataset files...')
        wb = xlrd.open_workbook(self.data_path)
        print('success to load dataset files')
        sheet_pres = wb.sheet_by_index(0)
        ncols= sheet_pres.ncols
        nrows = sheet_pres.nrows

        res = self.get_cols_id(nCols = ncols)
        if not res:
            return []
        # read colum
        try:
            cnt_cust = 0
            for r in tqdm(range(1, nrows), desc = 'loading dataset'):
                id = int(sheet_pres.cell_value(r, self.nID))        # bank id
                if id <= 0: continue
                post = int(sheet_pres.cell_value(r, self.nPost))    # post code
                if post < 0: continue

                seifa = int(sheet_pres.cell_value(r, self.nSeifa))  # seifa
                if seifa < 1 or seifa > 10: continue

                age = int(sheet_pres.cell_value(r, self.nAge) + 0.5)      # age
                if age <= 0 or age > 68:
                    continue
                gend = sheet_pres.cell_value(r, self.nGend)         # gender
                if gend != 'F' and gend != 'M':
                    continue

                prev_acc = float(sheet_pres.cell_value(r, self.nPrevAcc))
                acc = float(sheet_pres.cell_value(r, self.nAcc))    # current balance
                growth = float(sheet_pres.cell_value(r, self.nGrowth))  # growth balance

                custom = Customer(id = id, post = post, seifa = seifa, acc_bal= acc,age = age, gender=gend, growth = growth, prev_acc = prev_acc)
                self.customs[id] = custom
                cnt_cust += 1
        except:
            print('Failed to pass dataset')
            return
        if cnt_cust <= 0:
            print('Cannot find valid customers data')
            return
        print('Success to pass dataset. Passed customers = {}'.format(cnt_cust))
        return

    def get_data(self):
        return self.customs

    # @conver column name into zero-based index
    # @ params: col_name: name of colum in exel file
    #           nCols: a number of totla colums
    # @ return: if col_name is sucess, return(True, index),
    #           if not correct, return(False, -1)
    def get_col_index(self, col_name, nCols):
        if len(col_name) > 2 or len(col_name) <= 0:
            print('{}: invalid colum name'.format(col_name))
            return False, -1
        if len(col_name) == 1:
            id = ord(col_name) - ord('A')
            if id > nCols - 1:
                print('{}: invalid colum name'.format(col_name))
                return False, -1
            return True, id
        cols = col_name[:]
        char_1 = cols[0]
        char_2 = cols[2]
        id = (ord(char_1) - ord('A')) * 26 +  (ord(char_2) - ord('A'))
        if id >= nCols - 1:
            print('{}: invalid colum name'.format(col_name))
            return False, -1
        return True, id
    '''
    @ prepare indes of feature colums
    '''
    def get_cols_id(self, nCols):

        res, self.nID = self.get_col_index(COLUM_ID, nCols)
        if not res: return False
        res, self.nPost = self.get_col_index(COLUM_POST, nCols)
        if not res: return False
        res, self.nSeifa = self.get_col_index(COLUM_SEIFA, nCols)
        if not res: return False
        res, self.nGend= self.get_col_index(COLUM_GEN, nCols)
        if not res: return False
        res, self.nAge= self.get_col_index(COLUM_AGE, nCols)
        if not res: return False
        res, self.nPrevAcc = self.get_col_index(COLUM_PREV_ACC, nCols)
        if not res: return False
        res, self.nAcc= self.get_col_index(COLUM_ACC, nCols)
        if not res: return False
        res, self.nGrowth = self.get_col_index(COLUM_GROWTH, nCols)
        if not res: return False

        return True

    def __len__(self):
        return self.customs.len
    def get_projection(self, _id, _age, _gen, _seifa, _bal):
        results = []
        for id, cust in self.customs.items():
            if id == _id:
                continue
            if cust.age != _age:
                continue
            if cust.gender != _gen:
                continue
            if cust.seifa != _seifa:
                continue
            results.append(cust)
        if len(results) <= 0:
            return False, -1
        results.sort(key = lambda x: x.prev_acc - _bal, reverse=False)
        if len(results) >= 100:
            results = results[:100]

        # calc projection value
        cent_id = int(min((len(results) - 1)/2 + 0.5, len(results) - 1))
        growth = results[cent_id].growth
        return True, growth

    def isValidID(self, id):
        if id in self.customs.keys():
            return True
        return False


    def get_data(self, id):
        if not self.isValidID(id):
            return None
        return self.customs[id]



