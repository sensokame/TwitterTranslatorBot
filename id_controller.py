FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file = FILE_NAME):
    f_read = open(file, 'r')
    l = f_read.read().strip()
    last_seen_id = 0
    if l:
        last_seen_id = int(l)
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file = FILE_NAME):
    f_write = open(file, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def _test():
    file = "test_id.txt"
    for i in range(10):
        store_last_seen_id(i,file )
        assert retrieve_last_seen_id(file) == i

if __name__ == '__main__':
    _test()