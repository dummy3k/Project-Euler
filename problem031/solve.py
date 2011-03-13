from euler_tools.misc import StopWatch, LossyPrinter
watch = StopWatch()
lp = LossyPrinter(1)

cnt = 1 # 200p
for a in range(0, 201):
    for b in range(0, 101):
        sum_b = a + 2 * b
        if sum_b > 200:
            break
        for c in range(0, 41):
            sum_c = sum_b + 5 * c
            if sum_c > 200:
                break
            for d in range(0, 21):
                sum_d = sum_c + 10 * d
                if sum_d > 200:
                    break
                for e in range(0, 11):
                    sum_e = sum_d + 20 * e
                    if sum_e > 200:
                        break
                    for f in range(0, 5):
                        sum_f = sum_e + 50 * f
                        if sum_f > 200:
                            break
                        for g in range(0, 3):
                            sum_g = sum_f + 100 * g
                            #~ sum = a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g
                            if sum_g == 200:
                                #~ lp.try_print("a: %s, b: %s, c: %s, d: %s, e: %s, f: %s, f: %s" % (a, b, c, d, e, f, g))
                                print("a: %s, b: %s, c: %s, d: %s, e: %s, f: %s, f: %s" % (a, b, c, d, e, f, g))
                                cnt += 1

watch.print_time()
print cnt
