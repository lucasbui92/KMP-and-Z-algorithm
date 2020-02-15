import sys

#Name: Thuan Anh Bui, Student ID: 25203622


def compute_z_array(processed_pat):
    z_array = [0]

    for i in range(1, len(pat)):
        z_array.append(0)

    pos_r = 0
    pos_l = 0
    q = len(processed_pat)

    for i in range(0, q - 1):
        if processed_pat[i + 1] == processed_pat[i]:
            z_array[1] += 1
        else:
            break
    if z_array[1] > 0:
        pos_r = z_array[1] + 1
        pos_l = 1

    for k in range(2, q):
        if k > pos_r:
            pos_k = k
            while pos_k < q:
                if processed_pat[pos_k] == processed_pat[pos_k - k]:
                    z_array[k] += 1
                    pos_k += 1
                else:
                    break
            if z_array[k] > 0:
                pos_r = pos_k - 1
                pos_l = k
        else:
            if z_array[k - pos_l] < (pos_r - k):
                z_array[k] = z_array[k - pos_l]
            else:
                right = pos_r
                while right < q and processed_pat[right] == processed_pat[right - k]:
                    right += 1
                if right >= pos_r:
                    z_array[k] = right - k
                    pos_r = right - 1
                    pos_l = k

    return z_array


def compute_sp_array(m_pat, Z_arr):
    sp_array = [0]

    for i in range(1, m_pat):
        sp_array.append(0)

    for j in range(m_pat - 1, 0, -1):   # if 1, it misses a value
        i = j + Z_arr[j] - 1
        sp_array[i] = Z_arr[j]

    return sp_array


def kmp_method(pat, txt, z_array):
    if len(pat) > len(txt):
        return

    sp = compute_sp_array(len(pat), z_array)

    j = 0
    i = 0
    while j < n:
        while i > 0 and j < n and pat[i] != txt[j]:
            if pat[sp[i-1]] == txt[j]:
                i = sp[i - 1] + 1  # shift i to SPi(x) = SPi + 1
                j += 1             # increase j to next position
            else:
                i = sp[i - 1]
        if pat[i] == txt[j]:  # next character matched
            i += 1
        if i == m:
            k = j - i + 2
            output_file.write(str(k) + "\n")
            i = sp[i-1]
        j += 1


if __name__ == "__main__":
    if len(sys.argv) == 3:
        txt = open(sys.argv[1], 'r').read()
        pat = open(sys.argv[2], 'r').read()
        n = len(txt)
        m = len(pat)
        if m <= n:
            Z_array = compute_z_array(pat)

            output_file = open("output_kmp.txt", "w")
            kmp_method(pat, txt, Z_array)
            output_file.close()
    else:
        print("Invalid number of arguments")