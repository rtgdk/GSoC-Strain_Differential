import hashlib 

def hash(filename):
    hasher = hashlib.md5()
    with open(filename, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
        a = hasher.hexdigest()
        digests.append(a)
        return a
