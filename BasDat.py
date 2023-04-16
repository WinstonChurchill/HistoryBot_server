import json
import datetime

class BasaDate:
    def __init__(self):
        self.data = {}
        with open('files/BaseDate.json', 'r') as f:
            self.data = json.load(f)

    def return_all_len(self):
        alls = 0
        for i in self.data:
            alls += len(self.data[i])
        return alls

    def return_len_period_date(self, period):
        return len(self.data[period])

    def return_len_period(self):
        return len(self.data)

    def return_basa_period(self, period):
        return self.data[period]

    def return_basa_date(self):
        return self.data

    def return_period(self):
        a = []
        for i in self.data:
            a.append(i)
        return a

    def new_period(self, period, dates={}):
        try:
            self.data[period] = dates
            BasaDate.save_date(self)
            return 1
        except:
            return 0

    def new_date(self, period, dates, otvet_date):
        try:
            self.data[period][dates] = otvet_date
            BasaDate.save_date(self)
            return 1
        except:
            return 0

    def delete_period(self, period):
        try:
            self.data.pop(period)
            BasaDate.save_date(self)
            return 1
        except:
            return 0

    def delete_date(self, period, dates):
        try:
            self.data[period].pop(dates)
            BasaDate.save_date(self)
            return 1
        except:
            return 0

    def save_date(self):
        with open('files/BaseDate.json', 'w') as f:
            json.dump(self.data, f)

def datess():
    with open('files/helpfiles.txt', 'r', encoding='utf-8') as file:
        return file.readlines()

if __name__ == '__main__':
    DateBase = BasaDate()
    # print(DateBase.return_all_len())
    # a = {}
    # s = 0
    # for i in datess():
    #     i = i.replace('г.', '')
    #     i = i.replace('г', '')
    #     i = i.replace('гг.', '')
    #     i = i.replace('гг', '')
    #     i = i.replace(' - ', ' – ')
    #     i = i.replace('—', '–')
    #     b = i.replace('\n', '').split(' – ')
    #     if len(b) == 3:
    #         v = b
    #         b = []
    #         b.append(f'{v[0]}-{v[1]}')
    #         b.append(v[2])
    #     if b[1][-1] == ';':
    #         b[1] = b[1][0:-1]
    #     if b[0][-1] == ' ':
    #         b[0] = b[0][:-1]
    #     if b[0][-1] == ' ':
    #         b[0] = b[0][:-1]
    #     b[1] = b[1].title()
    #     a[b[0]] = b[1]
    #     print(b, s)
    #     s += 1
    # print(s)
    # print(a)
    # DateBase.new_period('21 век', a)
    # print(DateBase.return_basa_date())
    print(DateBase.return_all_len())
    print(DateBase.return_period())
    print(DateBase.save_date())