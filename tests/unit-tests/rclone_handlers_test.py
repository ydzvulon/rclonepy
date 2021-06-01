
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
