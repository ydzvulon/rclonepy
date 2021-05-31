
def test_rclone_tree():
    from pathlib import Path
    from rclonepy import rclonepy_mod as rclone
    
    me_parent_p = Path(__file__).parent
    name = Path(__file__).name

    the_tree = rclone.tree('..')
    
    assert len(the_tree.splitlines()) > 3
    assert name in the_tree
    print(the_tree)


def test_rclone_tree2():
    from rclonepy import rclonepy_mod as rclone
    from pathlib import Path
    
    me_parent_p = Path(__file__).parent
    name = Path(__file__).name

    src = str(Path(__file__).absolute())
    
    rclone.copyto(source=src, dest='lms3:test-b/hw.text.txt')
    the_data = rclone.get_data('lms3:test-b/hw.text.txt')

    assert 'test_rclone_tree2' in the_data

def test_rclone_tree3():
    import urllib.request as urlreq
    from io import StringIO as strio

    class PyProtoHandler(urlreq.BaseHandler):
        def python_open(self, req):
            fullUrl = req.get_full_url()
            return strio(fullUrl)

    opener = urlreq.build_opener(PyProtoHandler())
    urlreq.install_opener(opener)
    print(urlreq.urlopen("python://something/random/file.txt").read())
    print(len(urlreq.urlopen("http://example.com").read()))

if __name__ == '__main__':
    test_rclone_tree2()