

def test_rclone_with_minio_links():
    from rclonepy import rclonepy_mod as rclone
    from pathlib import Path
    
    me_parent_p = Path(__file__).parent
    name = Path(__file__).name

    src = str(Path(__file__).absolute())
    
    rclone.copyto(source=src, dest='lms3:test-b/hw.text.txt')
    the_data = rclone.get_data('lms3:test-b/hw.text.txt')

    assert 'test_rclone_tree2' in the_data
