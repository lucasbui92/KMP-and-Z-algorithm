import sys

#Name: Thuan Anh Bui, Student ID: 25203622


def compute_z_array(a_str):
    z_array = [0]

    for j in range(1, len(a_str)):
        z_array.append(0)

    pos_r = 0
    pos_l = 0
    q = len(a_str)

    for i in range(0, q - 1):
        if a_str[i + 1] == a_str[i]:
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
                if a_str[pos_k] == a_str[pos_k - k]:
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
                while right < q and a_str[right] == a_str[right - k]:
                    right += 1
                if right >= pos_r:
                    z_array[k] = right - k
                    pos_r = right - 1
                    pos_l = k

    return z_array


def edit_distance(s1, s2):
    dist = 1  #Always s1[0] != s2[0]
    if len(s1) == len(s2) and len(s1) == 2:
        if s1[1] != s2[1] and s1[0] != s2[1]:
            dist += 1
    return dist


def compute_prefix(z_prefix, i):
    pos = i - m - 1
    zi = z_prefix[i]
    if pos < 0:
        pos = 0
    if zi == m:
        output_edit_distance[pos] = 0
    elif zi == (m - 1):
        output_edit_distance[pos] = 1
    elif zi == (m - 2):
        mismatch_count = edit_distance(str_pre[(i + zi):(i + m)], pat[zi:m])
        if mismatch_count < edit_rule:
            output_edit_distance[pos] = mismatch_count


def compute_suffix(z_suffix, i):
    k = len(rev_str) - i + m
    zk = z_suffix[k]
    pos_in_str = i - 2 * m
    if pos_in_str < 0:
        pos_in_str = 0
    if zk == m:
        output_edit_distance[pos_in_str] = 0
    elif zk == (m - 1):
        output_edit_distance[pos_in_str] = 1
    elif zk == (m - 2):
        mismatch_count = edit_distance(rev_str[k + zk:k + m], rev_pat[zk:m])
        if mismatch_count < edit_rule:
            output_edit_distance[pos_in_str] = mismatch_count


def search_edit_distance():
    z_prefix = compute_z_array(str_pre)
    z_suffix = compute_z_array(rev_str)

    for i in range(m + 1, len(str_pre)):
        compute_prefix(z_prefix, i)
        compute_suffix(z_suffix, i)

    return output_edit_distance


if __name__ == "__main__":
    if len(sys.argv) == 3:
        txt = open(sys.argv[1], 'r').read()
        pat = open(sys.argv[2], 'r').read()
        n = len(txt)
        m = len(pat)

        str_pre = pat + '$' + txt
        rev_str = pat[::-1] + '$' + txt[::-1]
        rev_pat = pat[::-1]
        edit_rule = 2
        output_edit_distance = {}

        if m <= n:
            output = search_edit_distance()
            output_file = open("output_editdist.txt", "w")

            for i, j in output.items():
                output_file.write(str(i + 1) + "\t" + str(j) + "\n")

            output_file.close()
    else:
        print("Invalid number of arguments")