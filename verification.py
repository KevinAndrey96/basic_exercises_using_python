digit_list = list([41, 37, 29, 23, 19, 17, 13, 7, 3])


def products_sum(n_list, d_list):
    sum_result = n_list[0] * d_list[0]
    sum_result += n_list[1] * d_list[1]
    sum_result += n_list[2] * d_list[2]
    sum_result += n_list[3] * d_list[3]
    sum_result += n_list[4] * d_list[4]
    sum_result += n_list[5] * d_list[5]
    sum_result += n_list[6] * d_list[6]
    sum_result += n_list[7] * d_list[7]
    sum_result += n_list[8] * d_list[8]
    return sum_result


def verificar_nit(NIT, digito):
    verification = 0
    nit_list = list(map(int, str(NIT)))
    verification += products_sum(nit_list, digit_list)
    verification = verification % 11
    if verification == digito or verification == 0:
        return True
    return False


if __name__ == '__main__':
    print(verificar_nit(860007386, 1))
