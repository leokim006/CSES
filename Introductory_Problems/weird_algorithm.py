def main():
    n = int(input())

    while True:
        if n == 1:
            print(n)
            break
        print(n, end = " ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    
if __name__ == "__main__":
    main()
