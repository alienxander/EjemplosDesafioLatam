class LazyParameter(object):
    def __init__(self, parameter_path:str, region: str) -> None:
        print("init")
        self.parameter_path = parameter_path
        self.region = region
        self.value = None
        
    def __get__(self, obj, objtype=None):
        print("get")
        self.value = "Valor Url"
        return self.value