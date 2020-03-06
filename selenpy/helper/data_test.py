import os
import configparser
import logging

def get_data(section):
    data =  configparser.ConfigParser() 
    base_path =  os.getcwd()
    path_file = base_path + '\\tests\\data.ini' 
    
    data.read(path_file)
    dict_data = {}
    options = data.options(section)
    for option in options:
        try:
            dict_data[option] = data.get(section, option)
            if dict_data[option] == -1:
                logging.warning("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict_data[option] = None
    return dict_data