def move(n, src, tmp, dst):
    if n == 1:
        print('{} --> {}'.format(src, dst))
    else:
        move(n-1, src, dst, tmp)#把src从上到下的n-1个盘子借助tmp移动到dst
        print('{} --> {}'.format(src, dst))#把src第n个盘子移动到dst
        move(n-1, tmp, src, dst)#把tmp上的n-1个盘子借助src移动到dst

n = int(input('please input a number for n: '))
move(n, 'a', 'b', 'c')

