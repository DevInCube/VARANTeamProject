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
            return "No such file or directory: "+path
        rReader = csv.reader(File)
        try:
            self.readData(rReader)
        except csv.Error:
            return "Invalid file format."
        finally:
            File.close()
        if ((len(self.Data) == 1) and ((len(self.Data[0])) == 0)):
            return "The file is empty."
        else:
            self.createHeader()

    def readData(self, reader):
        i = 0
        for row in reader:
                if len(row) == 15:
                    row.insert(0, i)
                    i += 1
                self.Data.append(row)
    
    def createHeader(self):
        if self.Data[0][0] == 0:
            self.Header = self.Data[0]
            self.Header[0] = 'ID'
            del(self.Data[0])

    def saveData(self, fpath=path):
        if fpath == '':
            return "No file path."
        File = open(fpath, 'w')
        rWriter = csv.writer(File)
        for record in self.Data:
            rWriter.writerow(record)
        File.close()

    def getRecords(self):                  
        return self.Data

    def searchRecords(self, record):               
        searchResult = []
        r = range(1, len(record)-1)
        found = None
        empty = (record == \
                 ['','','','','','','','','','','','','','','',''])
        if empty:
            return self.Data
        for rec in self.Data:
            equal = None
            for i in r:
                if rec[i] == record[i]:
                    equal = 1
            if equal:
                searchResult.append(rec)
                found = 1
        if not found:
            return "There are no such records."
        else:
            return searchResult

    def newRecord(self):
        rid = (int)(self.Data[len(self.Data) - 1][0]) + 1
        self.Data.append([rid])
        i = 1
        while i < (len(self.Data[0])):
            i += 1
            self.Data[len(self.Data) - 1].append('')
        return rid

    def changeRecord(self, record):
        found = None
        for rec in self.Data:
            if rec[0] == record[0]:
                found = 1
                r = range(1, len(record))
                for i in r:
                    if record[i] != '':
                        rec[i] = record[i]
        if not found:
            return "There is no such ID."
        
    def deleteRecord(self,rid):
        try:
            iid = (int)(rid)
        except ValueError:
            return "Invalid ID."
        found = None
        for record in self.Data:
            if record[0] == iid:
                self.Data.remove(record)
                found = 1
        if not found:
            return "There is no such ID."