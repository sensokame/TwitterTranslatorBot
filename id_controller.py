"""Module to store and retrive last seen id"""
FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file = FILE_NAME):
    """function to retrieve last seen id from a file"""
    last_seen_id = 0
    with open(file, 'r') as f_read:
        last_seen_id_line = f_read.read().strip()
        if last_seen_id_line:
            last_seen_id = int(last_seen_id_line)
    return last_seen_id

def store_last_seen_id(last_seen_id, file = FILE_NAME):
    """function to store last seen id to a file"""
    with open(file, 'w') as f_write:
        f_write.write(str(last_seen_id))

def _test():
    file = "test_id.txt"
    for i in range(10):
        store_last_seen_id(i,file )
        assert retrieve_last_seen_id(file) == i

if __name__ == '__main__':
    _test()
