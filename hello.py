print('Hello Python!')

result = []
for num1 in range(1, 10):
    tmp = []
    for num2 in range(1, 10):
        tmp.append(f'{num1 * num2:2}')
    result.append(tmp)

for row in result:
    print(', '.join(row))



def fit(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)

    x_centered = [item - x_mean for item in x]
    y_centered = [item - y_mean for item in y]

    xy = [item_x * item_y for item_x, item_y in zip(x_centered, y_centered)]
    xx = [item * item for item in x_centered]
    sum_xy = sum(xy)
    sum_xx = sum(xx)

    a = sum_xy / sum_xx
    b = y_mean - a * x_mean

    return (a, b)

# サンプルデータ
x = [-0.03, 0.78, 2.07, 2.77, 4.10, 5.38, 5.99, 6.84, 8.12, 8.89, 9.43]
y = [0.88, 2.45, 2.43, 4.07, 5.49, 6.46, 7.02, 8.27, 8.70, 10.23, 10.65]

# 一次関数の推測を行う
print(fit(x, y))  # 出力：(1.0037317148789446, 1.1006562375889226)
