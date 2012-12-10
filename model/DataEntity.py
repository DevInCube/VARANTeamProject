import csv
import gettext


class DataEntity:
    """
    DataEntity class
    """
    Data = []
    path = ''
    Header = 0

    def __init__(self):
        self.Data = []
        """
        Installing the _() function.
        """
        gettext.install('DEMsg', './locale', unicode=True)

    def loadData(self, path):
    """
    Loading data.
    """
        if path == '':
            print _("No file path.")
            return _("No file path.")
        self.path = path
        """
        Checking if file or directory exists and opening file.
        """
        try:
            File = open(self.path, 'r')
        except IOError:
            return _("No such file or directory: ") + path
        rReader = csv.reader(File)
        """
        Validation of file format and reading data.
        """
        try:
            self.readData(rReader)
        except csv.Error:
            return _("Invalid file format.")
        finally:
            File.close()
        """
        Checking whether the file is empty and creating a header.
        """
        if (len(self.Data) <= 1):
            return _("The file is empty.")
        else:
            self.createHeader()
        return self.Data

    def readData(self, reader):
    """
    Reading data from file.
    """
        i = 0
        for row in reader:
                if len(row) == 15:
                    row.insert(0, str(i))
                    i += 1
                self.Data.append(row)

    def createHeader(self):
    """
    Creating header from data.
    """
        if self.Data[0][0] == '0':
            self.Header = self.Data[0]
            self.Header[0] = 'ID'
            del(self.Data[0])

    def saveData(self, fpath=path):
    """
    Saving data to file.
    """
        if fpath == '':
            return _("No file path.")
        File = open(fpath, 'w')
        rWriter = csv.writer(File)
        # rWriter.writerow(self.Header)
        for record in self.Data:
            rWriter.writerow(record)
        File.close()

    def getRecords(self):
    """
    Returns records that are in memory.
    """
        return self.Data

    def searchRecords(self, record):
    """
    Records search.
    Returns all records, in which at least one element matches the specified record.
    """
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
            return _("There are no such records.")
        else:
            return searchResult

    def newRecord(self):
    """
    Create a new blank record.
    """
        rid = str((int)(self.Data[len(self.Data) - 1][0]) + 1)
        self.Data.append([rid])
        i = 1
        while i < (len(self.Data[0])):
            i += 1
            self.Data[len(self.Data) - 1].append('')
        return rid

    def changeRecord(self, record):
    """
    Сhange record with a specified ID.
    """
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
            return _("There is no such ID.")
        return found

    def deleteRecord(self, rid):
    """
    Delete record with a specified ID.
    """
        try:
            iid = str(rid)
        except ValueError:
            return _("There is no such ID.")
        found = None
        for record in self.Data:
            if record[0] == iid:
                self.Data.remove(record)
                found = 1
        if not found:
            return _("There is no such ID.")