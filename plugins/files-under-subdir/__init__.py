def build_filter(args):
    return Filter(args)

class Filter():
    def __init__(self, args):
        if args == "":
            raise Exception('Must define path prefix')
        self.prefix = args

    def file_data_filter(self,file_data):
            file_data['filename'] = self.prefix + file_data['filename']

