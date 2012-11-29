import csv


class DataEntity:
    Data = []
    path = ''
    Header = 0

    def __init__(self):
        self.Data = []

    def loadData(self, path):
        if path == '':
            return "No file path."
        self.path = path
        try:
            File = open(self.path, 'r')
        except IOError:
            return "No such file or directory: " + path
        rReader = csv.reader(File)
        try:
            self.readData(rReader)
        except csv.Error:
            return "Invalid file format."
        finally:
            File.close()
        if (len(self.Data) <= 1):
            return "The file is empty."
        else:
            self.createHeader()
        return self.Data

    def readData(self, reader):
        i = 0
        for row in reader:
                if len(row) == 15:
                    row.insert(0, str(i))
                    i += 1
                self.Data.append(row)

    def createHeader(self):
        if self.Data[0][0] == '0':
            self.Header = self.Data[0]
            self.Header[0] = 'ID'
            del(self.Data[0])

    def saveData(self, fpath=path):
        if fpath == '':
            return "No file path."
        File = open(fpath, 'w')
        rWriter = csv.writer(File)
        # rWriter.writerow(self.Header)
        for record in self.Data:
            rWriter.writerow(record)
        File.close()

    def getRecords(self):
        return self.Data

    def searchRecords(self, record):
        searchResult = []
        r = range(len(record))
        found = None
        empty = (record == \
                 ['', '', '', '', '', '', '', '', '', \
                  '', '', '', '', '', '', ''])
        if empty:
            return self.Data
        mask = []
        for i in r:
            if record[i] != '':
                mask.append(i)
        # print str(record)
        for rec in self.Data:
            equal = None
            for i in mask:
                if (rec[i] == record[i]) and (rec[i] != ''):
                    equal = 1
                    break
            # print str(rec)
            if equal:
                searchResult.append(rec)
                found = 1
        if not found:
            return "There are no such records."
        else:
            return searchResult

    def newRecord(self):
        rid = str((int)(self.Data[len(self.Data) - 1][0]) + 1)
        self.Data.append([rid])
        i = 1
        while i < (len(self.Data[0])):
            i += 1
            self.Data[len(self.Data) - 1].append('')
        return rid

    def changeRecord(self, record):
        found = None
        for rec in self.Data:
            print str(rec[0]) + "|" + str(record[0])
            if rec[0] == record[0]:
                found = 1
                r = range(1, len(record))
                for i in r:
                    if record[i] != '':
                        rec[i] = record[i]
        if not found:
            return "There is no such ID."
        return found

    def deleteRecord(self, rid):
        try:
            iid = str(rid)
        except ValueError:
            return "There is no such ID."
        found = None
        for record in self.Data:
            if record[0] == iid:
                self.Data.remove(record)
                found = 1
        if not found:
            return "There is no such ID."
