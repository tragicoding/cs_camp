import math
import openpyxl

#기본 계산기
class Stat:
    #평균
    def average(self, scores):
        s = 0
        for score in scores:
            s += score
            average = round(s/len(scores),1)
        return average
    #분산
    def variance(self, scores, avrg):
        s = 0
        for score in scores:
            s += (score - avrg)**2
            v = round(s/len(scores),1)
        return v
    #표준편차
    def std_dev(self, var):
        s = round(math.sqrt(self.variance),1)
        return s

#데이터 수집 클래스
class DataHandler:
    evaluator = Stat()
    
    @classmethod
    def get_data_exel(cls,filename):
        
    