# stack single 
Class SingleStack:
    Initialize: stack = empty list

    Push(item):
        stack.append(item)

    Pop():
        if stack is not empty:
            return stack.remove_last()
        else:
            return error (underflow)

    Peek():
        if stack is not empty:
            return stack.last()
        else:
            return error

    IsEmpty():
        return stack.length == 0

    Size():
        return stack.length

# double stack
Class DoubleStack:
    Initialize: array of size N, top1 = -1, top2 = N

    Push1(item):
        if top1 + 1 < top2:
            top1 += 1
            array[top1] = item
        else:
            error (overflow)

    Push2(item):
        if top2 - 1 > top1:
            top2 -= 1
            array[top2] = item
        else:
            error (overflow)

    Pop1():
        if top1 >= 0:
            item = array[top1]
            top1 -= 1
            return item
        else:
            error (underflow)

    Pop2():
        if top2 < N:
            item = array[top2]
            top2 += 1
            return item
        else:
            error (underflow)

    IsEmpty1():
        return top1 == -1

    IsEmpty2():
        return top2 == N
