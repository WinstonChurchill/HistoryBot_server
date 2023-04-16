import json
import os
import datetime

class FilePeop:
    def __init__(self, id):
        self.id = id
        with open(f'files\Peopl\{id}.json', 'r') as file:
            self.data = json.load(file)        

    def new_quast(self, seed, time, vopr):        
        self.data[seed] = {'time': time, 'vopr': vopr, 'vopros_true': 0}
        FilePeop.save_base(self)

    def prav_otvet(self, seed):
        self.data[seed]['vopros_true'] += 1
        FilePeop.save_base(self)

    def final_quast(self, seed, time):
        self.data[seed]['final_time'] = time

    def state(self):
        reg = self.data['data_reg']
        reg = datetime.datetime.strptime(reg, "%Y/%m/%d/%H/%M/%S")
        reg = reg.strftime("%d.%m.%Y")
        col_opr = len(list(self.data)) - 1
        prav_col = 0
        vopros_col = 0
        prav = list(self.data)
        for i in prav:
            if i == 'data_reg':
                continue
            vopros_col += int(self.data[i]["vopr"])
            prav_col += int(self.data[i]['vopros_true'])
        return [reg, col_opr, vopros_col, prav_col, vopros_col - prav_col]

    def save_base(self):
        with open(f'files\Peopl\{self.id}.json', 'w') as f:
            json.dump(self.data, f, indent=4)

    def return_len_vopros(self):
        return len(self.data)

class DataPeople:
    def __init__(self):
        self.data = {}
        with open('files\DataPeople.json', 'r') as file:
            self.data = json.load(file)

    def new_file(self, id):
        self.data[str(id)]['file'] = 1
        now = datetime.datetime.now()
        stand = {'data_reg': now.strftime("%Y/%m/%d/%H/%M/%S")}
        with open(f'files\Peopl\{id}.json', 'w') as f:
            json.dump(stand, f, indent=4)
        with open('files\DataPeople.json', 'w') as files:
            json.dump(self.data, files,  indent=4)

    def return_data(self):
        return self.data

    def new_data(self, id):
        now = datetime.datetime.now()
        self.data[id] = {'admin': 0, 'file': 0}
        with open('files\DataPeople.json', 'w') as files:
            json.dump(self.data, files,  indent=4)

    def admin_prov(self, id):
        return self.data[str(id)]['admin']

    def file_prov(self, id):
        return self.data[str(id)]['file']

    def proverka_in(self, id):
        if id in self.data:
            return 1
        else:
            return 0

    def admin_redit(self, id):
        if self.data[id]['admin']:
            self.data[id]['admin'] = 0
        else:
            self.data[id]['admin'] = 1
        with open('files\DataPeople.json', 'w') as files:
            json.dump(self.data, files,  indent=4)

    def reset_id(self, id):
        try:
            self.data[id]['file'] = 0
            os.remove(f'files\Peopl\{id}.json')
            return 1
        except:
            return 0


def standartbaze():
    a = {'Testing id': {'admin': 0, 'file': 0}}
    with open('files\DataPeople.json', 'w') as file:
        json.dump(a, file,  indent=4)


if __name__ == '__main__':
    # DateBaze = DataPeople()
    # print(DateBaze.return_data())
    # DateBaze.new_data('Test')
    # print(DateBaze.return_data())
    # print(DateBaze.proverka_in('Test'))
    # print(DateBaze.reset_id('Test'))
    # standartbaze()
    Staticc = FilePeop(1118498500)
    print(Staticc.state())