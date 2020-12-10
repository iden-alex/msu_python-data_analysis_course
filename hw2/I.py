import copy


class FragileDict:
    
    def __init__(self, value=None, **kwargs):
        if value is None:
            self._data = copy.deepcopy(kwargs)
        else:
            self._data = copy.deepcopy(value)
        self._lock = False
        
    def __contains__(self, key):
        return key in self._data
    
    def __getitem__(self, key):
        if key in self._data:
            if self._lock:
                return self._data[key]
            else:
                return copy.deepcopy(self._data[key])
        else:
            raise KeyError(key)
        
    def __setitem__(self, key, value):
        if self._lock:
            self._data[key] = value
        else:
            raise RuntimeError("Protected state")
        
    def __enter__(self):
        self._lock = True
        self.begin_data = copy.deepcopy(self._data)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lock = False
        if exc_val is None:
            self._data = copy.deepcopy(self._data)
        else:
            self._data = copy.deepcopy(self.begin_data)
            print("Exception has been suppressed.")
        del self.__dict__['begin_data']
        return True
