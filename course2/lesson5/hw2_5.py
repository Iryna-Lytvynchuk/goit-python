from datetime import datetime
from multiprocessing import Process, Pipe


def calculate(number, pipe):

    numbers = []
    for j in range(1, number+1):
        if not number%j:
            numbers.append(j)
    pipe.send(numbers)

def factorize(*number):

    entered_numbers = number
    results = []
    processes = []
    pipe_receiver = []
        
    for i in entered_numbers:
        pipe_receiver.append(0)
        pipe_receiver[-1], pipe_sender = Pipe()
        processes.append(Process(target = calculate, args = (i,pipe_sender)))
        processes[-1].start()
    
    for i in range(len(entered_numbers)):
        results.append(pipe_receiver[i].recv())

    return results

if __name__ == '__main__':

    time_start = datetime.now()

    a, b, c, d  = factorize(128, 255, 99999, 10651060)

    print(a)
    print(b)
    print(c)
    print(d)
    
    print(time_start-datetime.now())
    