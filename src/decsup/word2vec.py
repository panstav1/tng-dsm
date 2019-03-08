import logging
import os
from surprise import Dataset, Reader, KNNBasic, dump, SVDpp

log = logging.getLogger(os.path.basename(__file__))


class TrainModel:

    # def __init__(self, method='als', n_epochs=20, sim_option='pearson_baseline'):
    #
    #     self.algo = KNNBasic(bsl_options={'method': method,'n_epochs': n_epochs},
    #                          sim_options={'name': sim_option, 'user_based': False})
    def __init__(self, lr_all = 0.006, n_epochs=40):
        self.algo = SVDpp(lr_all=lr_all, n_epochs=n_epochs)
        self.reader = Reader(rating_scale=(0,1))
        self.filename = 'trained_model.pkl'

    def read_from_df(self, dataframe, user_col, item_col, rating_col):
        data = Dataset.load_from_df(dataframe[[user_col, item_col, rating_col]], self.reader)
        trainset = data.build_full_trainset()
        return trainset

    def train_mod(self, dataframe, user_col, item_col, rating_col):
        self.algo.fit(self.read_from_df(dataframe, user_col, item_col, rating_col))

    def dump_model(self, predictions):
        saved_ent = dump.dump(self.filename, algo = self.algo, predictions=predictions)
        return saved_ent

    def load_model(self):
        predictions, loaded_ent = dump.load(self.filename)
        return predictions, loaded_ent

    def get_user_pred(self, user_id, dataframe, user_col, item_col, rating_col, n=2):
        data = Dataset.load_from_df(dataframe[[user_col,item_col,rating_col]],self.reader)
        testset = data.build_full_trainset().build_anti_testset()
        predictions = self.algo.test(testset)
        top_n = dict()
        for uid, iid, _, est, _ in predictions:
            if uid == user_id: top_n[iid] = est
        top_n = sorted(top_n.items(),key=lambda kv: kv[ 1 ],reverse=True)
        return predictions, top_n[:n]

    def get_user_pred_stable(self, user_id, predictions, n=2):
        top_n = dict()
        for uid, iid, _, est, _ in predictions:
            if uid == user_id: top_n[iid] = est;
        top_n = sorted(top_n.items(), key=lambda kv: kv[1], reverse=True)
        # top_nn = {k: top_n[k] for k in top_n.keys()[0][:n]}
        return top_n[:n]
