import configparser
import os

config = configparser.RawConfigParser()
thisfolder = os.path.dirname(os.path.abspath(__file__))
config.read(f'{thisfolder}/kotlin.cfg')


details_dict = dict(config.items('OTTO'))
print(details_dict)
