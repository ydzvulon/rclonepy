def gen_command(cmd_name):
    from pathlib import Path
    src_p = Path(__file__).parent / 'template_command.py'
    filename = f'rclone_{cmd_name}.py'
    dsr_p = Path(__file__).parent.parent / filename
    text = src_p.read_text()
    text_new = text.replace("_CMD_NAME_", cmd_name)
    return dsr_p.write_text(text_new)

if __name__ == '__main__':
    import fire
    fire.Fire(gen_command)
