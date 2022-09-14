class Handler:
    def run(self, sdk, path, req):
        return 'Method (branch1): %s\nBody: %s' % (req.method, str(req.json))
