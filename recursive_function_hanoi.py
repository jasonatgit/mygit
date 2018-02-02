def hanoi(n, src, tmp, dst):
    if n == 1:
        print('{} --> {}'.format(src, dst))
    else:
        hanoi(n-1, src, dst, tmp)#把src从上到下的n-1个盘子借助tmp移动到dst
        print('{} --> {}'.format(src, dst))#把src第n个盘子移动到dst
        hanoi(n-1, tmp, src, dst)#把tmp上的n-1个盘子借助src移动到dst

n = int(input('please input a integer number for n: '))
hanoi(n, 'a', 'b', 'c')

