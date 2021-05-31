import sys, time
from multiprocessing import Process, Pipe

def factorize(canal_recive, canal_trans):
    res = []
    number = canal_recive.recv()
    res.append(1)
    for n in range(2, number + 1):
        for m in range(2, n):
            if number % m == 0 and m not in res:
                res.append(m)
    res.append(number)
    canal_trans.send(res)
    sys.exit(0)

def main():
    #----------Закоментовані числа завеликі для моєго процесора та осі----------
    
    time_start = time.process_time()
    a = [1, 2, 4, 8, 16, 32, 64, 128]
    b = [1, 3, 5, 15, 17, 51, 85, 255]
    #c = [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    #d = [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    c = [1, 3, 9, 27, 37, 111, 333, 999]
    d = [1, 3, 9, 11, 33, 99, 101, 303, 909, 1111, 3333, 9999]
    my_1_recive, my_1_trans = Pipe()
    my_2_recive, my_2_trans = Pipe()
    my_3_recive, my_3_trans = Pipe()
    my_4_recive, my_4_trans = Pipe()
    my_process_1 = Process(target=factorize, args=(my_1_recive, my_1_trans))
    my_process_2 = Process(target=factorize, args=(my_2_recive, my_2_trans))
    my_process_3 = Process(target=factorize, args=(my_3_recive, my_3_trans))
    my_process_4 = Process(target=factorize, args=(my_4_recive, my_4_trans))
    my_process_1.start()
    my_process_2.start()
    my_process_3.start()
    my_process_4.start()
    my_1_trans.send(128)
    my_2_trans.send(255)
    my_3_trans.send(999)
    my_4_trans.send(9999)
    print(my_1_recive.recv())
    print(my_2_recive.recv())
    print(my_3_recive.recv())
    print(my_4_recive.recv())
    time_end = time.process_time()
    print("CPU time - ", time_end - time_start)

if __name__ == "__main__":
    main()