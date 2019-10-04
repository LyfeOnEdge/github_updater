import configparser, os
from .updater import updater_object
#get parent directory of parent directory
parent_parent = os.path.dirname(os.path.dirname(__file__))
downloader_config = os.path.join(parent_parent, "update.ini")
parser = configparser.ConfigParser()
parser.read(downloader_config)

updater = updater_object(parser["DEFAULT"]["UPDATE_NAME"], parser["DEFAULT"]["UPDATEURL"], parser["DEFAULT"]["ASSET_PATTERN"],)