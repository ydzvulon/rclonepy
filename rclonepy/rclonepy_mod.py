
import spur
# https://docs.python.org/3/library/shlex.html
import shlex

# from pathlib import Path
Path = str
def sh(cmd, **kw):
    shell = spur.LocalShell()
    cmd_tokens=shlex.split(cmd)
    import os
    update_env = {
        'RCLONE_CONFIG': os.environ.get('RCLONE_CONFIG_FILE__HOST_EXT'),
    }
    res = shell.run(cmd_tokens, update_env=update_env)
    return res.output.decode()

def tree(source:Path) -> str:
    """
    rclone tree lists the contents of a remote in a similar way to the
    unix tree command.

    For example

        $ rclone tree remote:path
        /
        ├── file1
        ├── file2
        ├── file3
        └── subdir
            ├── file4
            └── file5
        
        1 directories, 5 files

    You can use any of the filtering options with the tree command (e.g.
    --include and --exclude).  You can also use --fast-list.

    The tree command has many options for controlling the listing which
    are compatible with the tree command.  Note that not all of them have
    short options as they conflict with rclone's short options.
    """
    return sh(f"rclone tree {source}")

def lsjson(source:Path, recursive=False):
    """  * `lsjson` to list objects and directories in JSON format
    """
    recursive_opt = recursive and "--recursive" or ""
    cmd = f"rclone lsjson {recursive_opt} {source}"
    return sh(cmd)


def copy(source:Path, dest:Path):
    return sh(f"rclone copy {source} {dest}")

def copyto(source:Path, dest:Path):
    return sh(f"rclone copyto {source} {dest}")

def get_data(source):
    import io
    import time
    import os
    shell = spur.LocalShell()

    output_file = io.StringIO()
    update_env = {
        'RCLONE_CONFIG': os.environ.get('RCLONE_CONFIG_FILE__HOST_EXT'),
    }    
    process = shell.spawn(
        ["rclone", "cat", source],
        stdout=output_file,
        encoding="utf-8",
        update_env=update_env
    )

    process.wait_for_result()
    data = output_file.getvalue()
    # print(data)
    return data



def when_encoding_is_set_then_stdout_is_decoded_before_writing_to_stdout_argument():
    import io
    import time
    
    shell = spur.LocalShell()

    output_file = io.StringIO()
    process = shell.spawn(
        ["bash", "-c", r'echo -e "\u2603"hello; read dont_care'],
        stdout=output_file,
        encoding="utf-8",
    )
    time.sleep(1)
    # _wait_for_assertion(lambda: assert_equal(_u("☃hello\n"), output_file.getvalue()))
    print(output_file.getvalue())
    assert process.is_running()
    process.stdin_write(b"\n")
    # assert_equal(_u("☃hello\n"), process.wait_for_result().output)

def main_():
    import fire
    fire.Fire()

if __name__ == "__main__":
    main_()

    
