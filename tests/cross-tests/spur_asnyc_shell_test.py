
def test_async_shell_with_spur():
    import io
    import time
    import spur
    
    shell = spur.LocalShell()

    output_file = io.StringIO()
    process = shell.spawn(
        ["bash", "-c", r'echo 3; sleep 3; echo -e "\u2603"hello; read dont_care'],
        stdout=output_file,
        encoding="utf-8",
    )
    line = ""
    while not ('hello' in line):
        line = output_file.getvalue()
        time.sleep(1)
        print(line)
    assert 'hello' in line
    print(output_file.getvalue())
    assert process.is_running()
    process.stdin_write(b"\n")
    
    assert u"3\n☃hello\n" == process.wait_for_result().output
