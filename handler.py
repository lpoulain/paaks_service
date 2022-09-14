class Handler:
    def run(self, sdk, path, req):
        return 'Method (branch2) : %s\nBody: %s' % (req.method, str(req.json))
