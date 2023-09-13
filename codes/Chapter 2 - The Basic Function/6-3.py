class Solution():
    def solve(self, file_1, file_2, file_3):
        # 请在此添加代码，实现将文件file_1和file_2中的数字按从小到大的顺序，写入文件file_3中
        fp1 = open(file_1, "r")
        fp2 = open(file_2, "r")
        fp3 = open(file_3, "w")
        data1 = fp1.readlines()
        data2 = fp2.readlines()
        lst1 = []
        lst2 = []
        for i in data1:
            lst1.append(int(i[:-1]))
        for i in data2:
            lst2.append(int(i[:-1]))
        lst = lst1 + lst2
        lst = sorted(lst)
        for i in lst:
            fp3.write(str(i) + "\n")
        fp1.close()
        fp2.close()
        fp3.close()