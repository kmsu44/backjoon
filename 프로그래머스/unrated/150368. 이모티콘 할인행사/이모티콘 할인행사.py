import itertools
def solution(users, emoticons):
    answer = [0,0]
    sale = [10, 20, 30, 40]
    sale_rate = list(itertools.product(sale, repeat = len(emoticons)))
    for i in sale_rate:
        plus = 0
        earn_money = 0 
        for user in users:
            rate, money = user
            tmp = 0
            for idx, e_rate in enumerate(i):
                if rate <= e_rate:
                    tmp += int(emoticons[idx] * (100-e_rate) / 100)
            if money <= tmp:
                plus += 1
            else:
                earn_money += tmp
        if answer[0] < plus:
            answer[0] = plus
            answer[1] = earn_money
        elif answer[0] == plus:
            if answer[1] < earn_money:
                answer[1] = earn_money
        else:
            continue
    print(answer)
    return answer