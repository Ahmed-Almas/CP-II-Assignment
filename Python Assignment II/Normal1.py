def show_stars(row):
    for i in range(row):
        for j in range(0,i+1):
            print('*',end='')
        print('\n')
num=int(input("Enter rows :"))
show_stars(num)