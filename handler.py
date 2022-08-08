class Handler:
    def run(self, req):
        return 'Method (branch2) : %s\nBody: %s' % (req.method, str(req.json))
