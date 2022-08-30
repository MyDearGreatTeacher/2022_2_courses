from multiprocessing import Pool
import k2  # 那个有道词典翻译的py文件名

words = '''
    一
    二
    三
    四
    五
    六
    七
    八
    九
    十
    十一
'''

if __name__ == '__main__':
    pool = Pool()
    pool.map(k2.get_translate_data, words.split())
