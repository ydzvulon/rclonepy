from rclonepy.cmds.rclone_copyto import copyto
from rclonepy.cmds.rclone_size import size
from rclonepy.cmds.rclone_tree import tree
from rclonepy.cmds.rclone_cat import cat
from rclonepy.cmds.rclone_lsjson import lsjson
from rclonepy.cmds.rclone_copy import copy
from rclonepy.cmds.rclone_copyto import copyto

class RcloneCmdsMixin:
    # single arg commands
    size = size
    tree = tree
    cat = cat
    lsjson = lsjson

    # double arg commands
    copyto = copyto
    copy = copy
