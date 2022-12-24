import pickle
import json
import config
import numpy as np

class MobilePrice():
    
    def __init__(self,user_data):
        
        self.user_data = user_data
        self.model_file_path = config.MODEL_FILE_PATH
        self.proj_file_path = config.PROJECT_FILE_PATH
    
    def load_save_data(self):
        
        with open (self.model_file_path,"rb") as f:
            self.model = pickle.load(f)
            
        with open ( self.proj_file_path,"r") as f:
            self.proj_data = json.load(f)
            
    def get_pred_price(self):
        
        self.load_save_data()
        
        col_count = len(self.proj_data["columns"])
        test_array = np.zeros(col_count)
        test_array[0] = eval(self.user_data["weight"])
        test_array[1] = eval(self.user_data["resoloution"])
        test_array[2] = eval(self.user_data["int_Memory"])
        test_array[3] = eval(self.user_data["Ram"])
        test_array[4] = eval(self.user_data["RearCam"])
        test_array[4] = eval(self.user_data["Front_Cam"])
        test_array[4] = eval(self.user_data["Battery"])
        
        predicted_price = np.around(self.model.predict([test_array])[0],3)
        print("Predicted Price :",predicted_price)
        return predicted_price
    
if __name__ == "__main__":
    obj = MobilePrice()
    obj
                
                
        
        
        