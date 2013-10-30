import psycopg2

class DatabaseManager:
    # CONSTANTS
    conn_string = "host='localhost' dbname='TwitterDB' user='postgres' password='261286'"
    ID = 0
    COUNTRY = 1
    DATE_START = 2
    TIME_START  = 3
    DURATION = 4
    CHANNEL_NAME = 5
    PROGRAM_NAME = 6
    DESCRIPTOR = 7
    
    
    #DEFINES
    def __init__(self):
        # print the connection string we will use to connect
        print "Connecting to database\n    ->%s" % (self.conn_string)
     
        # get a connection, if a connect cannot be made an exception will be raised here
        self.conn = psycopg2.connect(self.conn_string)
    
    def getConnection(self):
        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = self.conn.cursor()
        return cursor
    
    def select(self, table):
        cursor = self.getConnection()
     
        # execute our Query
        cursor.execute("SELECT * FROM "+table)
        
        # retrieve the records from the database
        return cursor.fetchall()
    
    def filterEPGByChannelName(self,channel_name):
        list_epg = self.select("epg")
        rowlist = []
        for row in list_epg:
            if row[self.CHANNEL_NAME].lower() == channel_name.lower():
                rowlist.append(row)
                #print "Channel: %s - Program: %s " %(row[data.CHANNEL_NAME], row[data.PROGRAM_NAME])
        
        return rowlist

#print "Qnt of programs for SBT: %d"  %(len(data.filterEPGByChannelName("SBT")))
#print "Qnt of programs for Globo: %d"  %(len(data.filterEPGByChannelName("Globo")))
#print "Qnt of programs for Rede Vida: %d"  %(len(data.filterEPGByChannelName("RedeVida")))
    
    
"""
        # retrieve the records from the database
        #records = cursor.fetchall()
        #for record in records:
        #    print record
        # print out the records using pretty print
        # note that the NAMES of the columns are not shown, instead just indexes.
        # for most people this isn't very useful so we'll show you how to return
        # columns as a dictionary (hash) in the next example.
        #pprint.pprint(records.location)
"""
