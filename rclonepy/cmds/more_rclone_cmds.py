


def get_data(source):
    import io
    import time
    import os
    import spur
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
