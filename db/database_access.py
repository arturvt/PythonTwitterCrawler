import psycopg2
from util.time_parser import DateHandler

class DatabaseManager:
    # CONSTANTS
    conn_string = "host='localhost' dbname='TwitterDB' user='postgres' password='261286'"
    
    #DEFINES
    def __init__(self):
        # print the connection string we will use to connect
        print "Connecting to database\n    ->%s" % (self.conn_string)
     
        # get a connection, if a connect cannot be made an exception will be raised here
        self.conn = psycopg2.connect(self.conn_string)
        self.cursor = self.conn.cursor()
    
    def select(self, table):
        # execute our Query
        self.cursor.execute("SELECT * FROM "+table)
        
        # retrieve the records from the database
        return self.cursor.fetchall()
    
    def filterEPGByChannelName(self,channel_name):
        self.cursor.execute("""
        SELECT 
          broadcaster.name, program.name, epg_event.descriptor 
        FROM 
          public.epg_event, 
          public.program, 
          public.broadcaster
        WHERE 
          program.id = epg_event.program AND broadcaster.id = program.broadcaster AND
          broadcaster.name = '%s';
        """ %(channel_name)
        )
        list_epg = self.cursor.fetchall()
        return list_epg

    def filterEPGByChannelNameDateTime(self, channel_name, date_time):
        date = DateHandler(date_time)
        query = """ 
          SELECT 
          epg_event.startdate, epg_event.starttime, broadcaster.name, program.name, epg_event.descriptor
        FROM 
          public.epg_event, 
          public.program, 
          public.broadcaster
        WHERE 
          program.id = epg_event.program AND broadcaster.id = program.broadcaster AND
          broadcaster.name = '%s' AND
          epg_event.startdate = '%s'
        ORDER BY
          epg_event.starttime    

        """ %(channel_name, date.getDate())
        self.cursor.execute(query)       
        return self.cursor.fetchall()
    
data = DatabaseManager()
list_epg = data.filterEPGByChannelNameDateTime('Globo', '29/10/2013 - 16:00:00')
for epg in list_epg:
    print epg[0], epg[1], epg[2], epg[3], epg[4]
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
