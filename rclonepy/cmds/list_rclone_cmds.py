from rclonepy.cmds.rclone_size import size
from rclonepy.cmds.rclone_tree import tree
from rclonepy.cmds.rclone_cat import cat
from rclonepy.cmds.rclone_lsjson import lsjson

class RcloneCmdsMixin:
    size = size
    tree = tree
    cat = cat
    lsjson = lsjson
