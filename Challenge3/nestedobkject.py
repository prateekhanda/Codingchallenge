nestedObject1 = {"a":{"b":{"c":"d"}}}
nestedObject2 = {"x":{"y":{"z":"a"}}}
key1 = "a/b/c"
key2 = "x/y/z"
def getValue(obj,keys):
    res = obj
    keySplit = keys.split("/")
    for key in keySplit:
        if key in res.keys():
            res = res[key]
    return res;

getValue(nestedObject1,key1)

getValue(nestedObject2,key2)

