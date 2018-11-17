d = dict()  # dictionary
d['I'] = 1
d['V'] = 5
d['X'] = 10
d['L'] = 50
d['C'] = 100
d['D'] = 500
d['M'] = 1000
while True:
    try:
        a = input('请输入规范的罗马数字（大小写均可）或阿拉伯数字（不能太大）：')
        try:
            n = int(a)
            r = ''
            q = n // 1000
            b = n % 1000 // 100
            s = n % 100 // 10
            g = n % 10
            while q > 0:
                r = r + 'M'
                q -= 1
            while b > 0:
                if b == 9:
                    r = r + 'CM'
                    b = 0
                elif b >= 5:
                    r = r + 'D'
                    b = b - 5
                elif b == 4:
                    r = r + 'CD'
                    b = 0
                else:
                    r = r + 'C'
                    b -= 1
            while s > 0:
                if s == 9:
                    r = r + 'XC'
                    s = 0
                elif s >= 5:
                    r = r + 'L'
                    s = s - 5
                elif s == 4:
                    r = r + 'XL'
                    s = 0
                else:
                    r = r + 'X'
                    s -= 1
            while g > 0:
                if g == 9:
                    r = r + 'IX'
                    g = 0
                elif g >= 5:
                    r = r + 'V'
                    g = g - 5
                elif g == 4:
                    r = r + 'IV'
                    g = 0
                else:
                    r = r + 'I'
                    g -= 1
            print(r)
        except:
            r = a
            r = r.upper()
            l = len(r)
            n = 0
            for a in range(l - 1, -1, -1):
                if a == l - 1 or d[r[a]] >= d[r[a + 1]]:
                    n = n + d[r[a]]
                else:
                    n = n - d[r[a]]
            print('阿拉伯数字是：', n, '\n')
    except:
        print('\n输入错误，请重新输入：')
