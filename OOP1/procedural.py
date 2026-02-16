import openpyxl
import math

def get_data_from_exel(filename):
    dic = {}
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    g = ws.rows

    for name, score in g:
        dic[name.value] = score.value
    
    return dic

def get_score_list(dic):
    scores = list(dic.values())
    
    return scores

s = 0

def get_avrg(scores):
    global s
    for score in scores:
        s += score
    avrg =round((s/len(scores)),1)

    return avrg

def get_v(scores,avrg):
    global s
    for score in scores:
        s += (avrg - score)**2
        v = round(s/len(scores))

    return v

def get_s(v):
    s = round(math.sqrt(v),1)
    
    return s

def evaluate(total_avrg, avrg, v, s):
    if avrg <50 and s>20:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avrg>50 and s>20:
        print("성적은 평균 이상이지만 학생들이 실력 차이가 크다.")
    elif avrg<50 and s<20:
        print("학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다.")
    elif avrg>50 and s<20:
        print("성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.")

if __name__ == "__main__":
    raw_data = get_data_from_exel("class_2.xlsx")
    score_list = get_score_list(raw_data)
    avrg = get_avrg(score_list)
    v = get_v(score_list,avrg)
    s = get_s(v)

    evaluate(50, avrg, v, s)