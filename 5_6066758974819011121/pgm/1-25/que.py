# python queue tutorial

# implementing FIFO (First-in-First-out queue)


# importing the queue module
from queue import Queue


def add(q):
    for i in range(1, 6):
        # adding elements to the queue
        q.put(i)

    # printing elements present in the queue
    print_ele(q)


def print_ele(q):
    # checking if the queue is empty
    if not q.empty():
        queue_size = q.qsize()
        print('Queue size = {}. Printing elements.'.format(queue_size))
        for i in range(queue_size):
            print('{}'.format(q.get()))  # printing the item that we are removing
    else:
        # if the queue is empty print the queue size
        print('Queue empty! Size = {}'.format(q.qsize()))


# driver code
if __name__ == '__main__':
    # optional parameter to specify the max size of the queue
    # maxsize = 10
    # taking an object of Queue
    q = Queue()
    add(q)
