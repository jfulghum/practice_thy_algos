dict1 = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }
output = {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }

def flatten_dictionary(dictionary, lkey = ""):
    ret = {}
    for rkey, val in dictionary.items():
        key = lkey+rkey
        if type(val) == dict:
          if rkey == "" or rkey == None:
            ret.update(flatten_dictionary(val, key))
          else:
            ret.update(flatten_dictionary(val, key+'.'))
        else:
            ret[key] = val
    return ret


print(flatten_dictionary(dict1))
