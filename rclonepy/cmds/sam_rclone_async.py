
def when_encoding_is_set_then_stdout_is_decoded_before_writing_to_stdout_argument():
    import io
    import time
    import spur
    
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
