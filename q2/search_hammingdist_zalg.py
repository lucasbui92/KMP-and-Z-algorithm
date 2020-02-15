import sys

#Name: Thuan Anh Bui, Student ID: 25203622


def compute_z_array(pre_str):
    z_array = [0]

    for i in range(1, len(pre_str)):
        z_array.append(0)

    pos_r = 0
    pos_l = 0
    q = len(pre_str)

    for i in range(0, q - 1):
        if pre_str[i + 1] == pre_str[i]:
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
                if pre_str[pos_k] == pre_str[pos_k - k]:
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
                while right < q and pre_str[right] == pre_str[right - k]:
                    right += 1
                if right >= pos_r:
                    z_array[k] = right - k
                    pos_r = right - 1
                    pos_l = k

    return z_array


def hamming(s1, s2):
    if len(s1) != len(s2):
        return -1

    mismatch_count = 0
    for r in range(0, len(s1)):
        if s1[r] != s2[r]:
            mismatch_count += 1
    return mismatch_count


def compute_prefix(z_prefix, i):
    pos = i - m - 1
    zi = z_prefix[i]
    if zi == m:
        output_hamming[pos] = 0
    elif zi == (m - 1):
        output_hamming[pos] = 1
    elif zi == (m - 2):
        mismatch_count = hamming(pat[zi:m], str_pre[(i + zi):(i + m)])
        if mismatch_count == hamming_rule:
            output_hamming[pos] = mismatch_count


def compute_suffix(z_suffix, i):
    k = len(rev_str) - i + m
    zk = z_suffix[k]
    pos_in_str = i - 2 * m
    if zk == m:
        output_hamming[pos_in_str] = 0
    elif zk == (m - 1):
        output_hamming[pos_in_str] = 1
    elif zk == (m - 2):
        mismatch_count = hamming(rev_pat[zk:m], rev_str[k + zk:k + m])
        if mismatch_count == hamming_rule:
            output_hamming[pos_in_str] = mismatch_count


def search_hamming_position():
    z_prefix = compute_z_array(str_pre)
    z_suffix = compute_z_array(rev_str)

    for i in range(m + 1, len(str_pre)):
        compute_prefix(z_prefix, i)
        compute_suffix(z_suffix, i)

    return output_hamming


if __name__ == "__main__":
    if len(sys.argv) == 3:
        txt = open(sys.argv[1], 'r').read()
        pat = open(sys.argv[2], 'r').read()

        str_pre = pat + '$' + txt
        rev_str = pat[::-1] + '$' + txt[::-1]
        rev_pat = pat[::-1]
        hamming_rule = 1
        output_hamming = {}
        m = len(pat)

        if m <= len(txt):
            output = search_hamming_position()
            output_file = open("output_hammingdist.txt", "w")

            for i, j in output.items():
                output_file.write(str(i + 1) + "\t" + str(j) + "\n")
            output_file.close()
    else:
        print("Invalid number of arguments")