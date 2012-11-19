import unittest
import DataEntity as DEM

class ModelTest(unittest.TestCase):
    DE = DEM.DataEntity
    
    def setUp(self):
        self.DE = DEM.DataEntity()
        DEM.DataEntity.loadData(self.DE,'test.csv')
        
    def testLoadDataHeader(self):
        Header = ['ID', 'CAD CDW ID', 'CAD Event Number', \
                  'General Offense Number', 'Event Clearance Code', \
                  'Event Clearance Description', 'Event Clearance SubGroup', \
                  'Event Clearance Group', 'Event Clearance Date', \
                  'Hundred Block Location', 'District/Sector', 'Zone/Beat', \
                  'Census Tract', 'Longitude', 'Latitude', 'Incident Location']
        unittest.TestCase.assertEqual(self, self.DE.Header, Header)
        
    def testChangeRecord(self):
        record = [1, '961352', '12777390432', '2014590432', '205', \
                  'DISTURBANCE1, OTHER1', 'DISTURBANCES1', 'DISTURBANCES1', \
                  '12/14/2012 09:47 AM', '7 AV / PIKE ST', 'L', 'P1', \
                  '8123.2009', '-121.3366873', '49.610212766', \
                  '(47.910212766, -122.3366873)']
        self.DE.changeRecord(record)
        unittest.TestCase.assertEqual(self, self.DE.Data[0], record)
        
    def testChangeRecordNoID(self):
        record = [27, '961352', '12777390432', '2014590432', '205', \
                  'DISTURBANCE1, OTHER1', 'DISTURBANCES1', 'DISTURBANCES1', \
                  '12/14/2012 09:47 AM', '7 AV / PIKE ST', 'L', 'P1', \
                  '8123.2009', '-121.3366873', '49.610212766', \
                  '(47.910212766, -122.3366873)']
        unittest.TestCase.assertEqual(self, self.DE.changeRecord(record), \
                                      "There is no such ID.")
        
    def testDeleteRecord(self):
        initLen = len(self.DE.Data)
        self.DE.deleteRecord(1)
        unittest.TestCase.assertEqual(self, self.DE.Data[0][0], 2)
        unittest.TestCase.assertEqual(self, len(self.DE.Data), initLen-1)
        
    def testDeleteRecordNoID(self):
        unittest.TestCase.assertEqual(self, self.DE.deleteRecord(27), \
                                      "There is no such ID.")
        
    def testDeleteRecordInvalidID(self):
        unittest.TestCase.assertEqual(self, self.DE.deleteRecord('invalid id'),\
                                       "Invalid ID.")
        
    def testNewRecord(self):
        initLen = len(self.DE.Data) 
        self.DE.newRecord()
        Len = len(self.DE.Data) 
        record = [16,'','','','','','','','','','','','','','','']
        unittest.TestCase.assertEqual(self, self.DE.Data[len(self.DE.Data) - 1], \
                                      record)   
        unittest.TestCase.assertEqual(self, Len, initLen + 1)
        
    def testSearchRecordsFoundID(self):
        query = [10,'','','','470','','PARKING VIOLATIONS','','','','','','','','','']
        result = [[9, '961349', '12000390459', '2012390459', '470', \
                   'PARKING VIOLATION (EXCEPT ABANDONED VEHICLES)', \
                   'PARKING VIOLATIONS', 'TRAFFIC RELATED CALLS', \
                   '11/14/2012 09:31 AM', '1XX BLOCK OF 12TH AVE', 'E', \
                   'E3', '8600.3002', '-122.316781664', '47.603100033', \
                   '(47.603100033, -122.316781664)'], \
                       [11, '961339', '12000390428', '2012390428', '470', \
                        'PARKING VIOLATION (EXCEPT ABANDONED VEHICLES)', \
                        'PARKING VIOLATIONS', 'TRAFFIC RELATED CALLS', \
                        '11/14/2012 09:19 AM', '50XX BLOCK OF 40TH AVE NE', \
                        'L', 'L3', '4200.4011', '-122.285198326', '47.734630685', \
                        '(47.734630685, -122.285198326)'], \
                       [12, '961339', '12000390428', '2012390428', '470', \
                        'PARKING VIOLATION (EXCEPT ABANDONED VEHICLES)', \
                        'PARKING VIOLATIONS', 'TRAFFIC RELATED CALLS', \'
                        '11/14/2012 09:19 AM', '50XX BLOCK OF 40TH AVE NE', \
                        'L', 'L3', '4200.4011', '-122.285198326', '47.734630685', \
                        '(47.734630685, -122.285198326)']]
        unittest.TestCase.assertEqual(self, self.DE.searchRecords(query), result)
        
    def testSearchRecordsNotFound(self):
        query = ['','','','','999','','asefsadf','','','','','','','','','']
        unittest.TestCase.assertEqual(self, self.DE.searchRecords(query), \
                                      "There are no such records.")
        
    def testSaveData(self):
        Data = self.DE.Data
        self.DE.deleteRecord(3)
        self.DE.saveData('testsave.csv')
        self.DE.loadData('testsave.csv')
        unittest.TestCase.assertEqual(self, Data, self.DE.Data)
        
    def tearDown(self):
        del(self.DE)
        
class DataTest(unittest.TestCase):
    Data = []
    DE = DEM.DataEntity
    
    def setUp(self):
        self.DE = DEM.DataEntity()
        self.Data = [[1, '961352', '12000390432', '2012390432', '245', 'DISTURBANCE, OTHER', 'DISTURBANCES', 'DISTURBANCES', '11/14/2012 09:49 AM', '4 AV / PIKE ST', 'K', 'K1', '8100.2009', '-122.3366873', '47.610212766', '(47.610212766, -122.3366873)'],\
                       [2, '961351', '12000390328', '2012390328', '63', 'THEFT - CAR PROWL', 'CAR PROWL', 'CAR PROWL', '11/14/2012 09:47 AM', '40XX BLOCK OF 31ST AVE S', 'R', 'R1', '10100.4003', '-122.292454091', '47.566807533', '(47.566807533, -122.292454091)'], \
                       [3, '961350', '12000390494', '2012390494', '177', 'LIQUOR VIOLATION - INTOXICATED PERSON', 'LIQUOR VIOLATIONS', 'LIQUOR VIOLATIONS', '11/14/2012 09:45 AM', '2 AV / PIKE ST', 'K', 'K1', '8100.2010', '-122.338906798', '47.60928404', '(47.60928404, -122.338906798)'], \
                       [4, '961346', '12000390406', '2012390406', '71', 'AUTO THEFT', 'AUTO THEFTS', 'AUTO THEFTS', '11/14/2012 09:36 AM', '21XX BLOCK OF NW 96TH ST', 'B', 'B1', '1600.2011', '-122.384167308', '47.698980802', '(47.698980802, -122.384167308)'], \
                       [5, '961343', '12000390447', '2012390447', '245', 'DISTURBANCE, OTHER', 'DISTURBANCES', 'DISTURBANCES', '11/14/2012 09:32 AM', '10 AV E / E PROSPECT ST', 'C', 'C1', '6500.4000', '-122.320212874', '47.628669022', '(47.628669022, -122.320212874)'], \
                       [6, '961348', '12000390440', '2012390440', '71', 'AUTO THEFT', 'AUTO THEFTS', 'AUTO THEFTS', '11/14/2012 09:32 AM', '26XX BLOCK OF 23RD AVE S', 'O', 'O1', '10000.1000', '-122.303321075', '47.579584689', '(47.579584689, -122.303321075)'], \
                       [7, '961345', '12000390471', '2012390471', '415', 'BLOCKING VEHICLE', 'TRAFFIC RELATED CALLS', 'TRAFFIC RELATED CALLS', '11/14/2012 09:31 AM', 'M L KING JR WY S / S ALASKA ST', 'R', 'R2', '10300.4004', '-122.293240716', '47.560805821', '(47.560805821, -122.293240716)'], \
                       [8, '961347', '12000390430', '2012390430', '430', 'ACCIDENT INVESTIGATION', 'TRAFFIC RELATED CALLS', 'ACCIDENT INVESTIGATION', '11/14/2012 09:31 AM', '23 AV S / S SPOKANE ST', 'R', 'R2', '10000.7023', '-122.303414453', '47.571922362', '(47.571922362, -122.303414453)'], \
                       [9, '961349', '12000390459', '2012390459', '470', 'PARKING VIOLATION (EXCEPT ABANDONED VEHICLES)', 'PARKING VIOLATIONS', 'TRAFFIC RELATED CALLS', '11/14/2012 09:31 AM', '1XX BLOCK OF 12TH AVE', 'E', 'E3', '8600.3002', '-122.316781664', '47.603100033', '(47.603100033, -122.316781664)'], \
                       [10, '961344', '12000390451', '2012390451', '203', 'ALARMS - RESIDENTIAL PANIC (FALSE)', 'PANIC ALARMS (FALSE)', 'FALSE ALARMS', '11/14/2012 09:27 AM', '46XX BLOCK OF SW SEATTLE ST', 'W', 'W1', '9600.4004', '-122.39088434', '47.589395796', '(47.589395796, -122.39088434)'], \
                       [11, '961339', '12000390428', '2012390428', '470', 'PARKING VIOLATION (EXCEPT ABANDONED VEHICLES)', 'PARKING VIOLATIONS', 'TRAFFIC RELATED CALLS', '11/14/2012 09:19 AM', '50XX BLOCK OF 40TH AVE NE', 'L', 'L3', '4200.4011', '-122.285198326', '47.734630685', '(47.734630685, -122.285198326)'], \
                       [12, '961339', '12000390428', '2012390428', '470', 'PARKING VIOLATION (EXCEPT ABANDONED VEHICLES)', 'PARKING VIOLATIONS', 'TRAFFIC RELATED CALLS', '11/14/2012 09:19 AM', '50XX BLOCK OF 40TH AVE NE', 'L', 'L3', '4200.4011', '-122.285198326', '47.734630685', '(47.734630685, -122.285198326)'], \
                       [13, '961340', '12000390439', '2012390439', '280', 'SUSPICIOUS PERSON', 'SUSPICIOUS CIRCUMSTANCES', 'SUSPICIOUS CIRCUMSTANCES', '11/14/2012 09:18 AM', '41XX BLOCK OF 25TH AVE SW', 'W', 'W1', '9900.2012', '-122.36436487', '47.565631771', '(47.565631771, -122.36436487)'], \
                       [14, '961340', '12000390439', '2012390439', '280', 'SUSPICIOUS PERSON', 'SUSPICIOUS CIRCUMSTANCES', 'SUSPICIOUS CIRCUMSTANCES', '11/14/2012 09:18 AM', '41XX BLOCK OF 25TH AVE SW', 'W', 'W1', '9900.2012', '-122.36436487', '47.565631771', '(47.565631771, -122.36436487)'], \
                       [15, '961338', '12000390462', '2012390462', '177', 'LIQUOR VIOLATION - INTOXICATED PERSON', 'LIQUOR VIOLATIONS', 'LIQUOR VIOLATIONS', '11/14/2012 09:14 AM', '4 AV S / S LANDER ST', 'O', 'O2', '9300.3032', '-122.329058009', '47.579808466', '(47.579808466, -122.329058009)']]
        DEM.DataEntity.loadData(self.DE,'test.csv')
        
    def testLoadData(self):
        unittest.TestCase.assertEqual(self, self.DE.Data, self.Data)
        
    def testGetRecords(self):
        unittest.TestCase.assertEqual(self, self.DE.getRecords(), self.Data)
        
    def testSearchRecordsNoQuery(self):
        query = ['','','','','','','','','','','','','','','','']
        unittest.TestCase.assertEqual(self, self.DE.searchRecords(query), \
                                      self.Data) 
        
    def tearDown(self):
        del(self.DE)
        del(self.Data)

class FileTest(unittest.TestCase):
    DE = DEM.DataEntity
    
    def setUp(self):
        self.DE = DEM.DataEntity()
        
    def testLoadDataInvalidFormat(self):
        result = self.DE.loadData('format.doc')
        unittest.TestCase.assertEqual(self, result, \
                               "Invalid file format.")    
    
    def testLoadDataEmptyFile(self):
        result = self.DE.loadData('empty.csv')
        unittest.TestCase.assertEqual(self, result, \
                                      "The file is empty.")

    def testLoadDataNoFile(self):
        unittest.TestCase.assertEqual(self, self.DE.loadData('12356.txt'), \
                                      "No such file or directory: 12356.txt")
    def testLoadDataNoFilePath(self):
        unittest.TestCase.assertEqual(self, self.DE.loadData(''), \
                                      "No file path.")
        
    def testSaveDataNoFilePath(self):
        unittest.TestCase.assertEqual(self, self.DE.saveData(''), \
                                      "No file path.")