import os


def delete_files(file_dir, n):
    try:
        name_out = '%s\output.txt' % file_dir
        os.remove(name_out)
    except:
        print('error delete output.txt')
    list_fold = os.listdir(file_dir)
    k_proc = 1
    for name_fold in list_fold:
        print('delete %d\%d' % (k_proc, len(list_fold)))
        k_proc += 1
        fold_name = '%s\%s' % (file_dir, name_fold)
        list_file = os.listdir(fold_name)
        deli = len(list_file) // n
        i = 1
        for name in list_file:
            if (i % deli) != 0:
                name = '%s\%s' % (fold_name, name)
                try:
                    os.remove(name)
                except:
                    print('error')
            i += 1


''' 
file_dir - путь до папок с знаменитостями в распакованном архиве
n - количество оставляемых фоток
'''
file_dir = 'D:\part9\dir_009'
delete_files(file_dir, 10)

