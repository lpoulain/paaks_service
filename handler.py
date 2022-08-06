class Handler:
    def run(self, req):
        return 'Method (branch1): %s\nBody: %s' % (req.method, str(req.json))
