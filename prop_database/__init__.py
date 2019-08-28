'''
modify excel table into data tables named by property
'''
import sqlite3

conn = sqlite3.connect(('substance_properties.db'))
c = conn.cursor()

def substance_list():
    '''
    returns a list of all known substances
    '''

    c.execute("SELECT * FROM substances")
    dat = c.fetchall()
    return dat    


def request_substance(CAS, conn, c):
    '''
    retrieves property information data from database 
    '''   
    c.execute("SELECT * FROM substances WHERE CAS = '{qq}' ".format(qq =  CAS))
    dat = c.fetchall()
    return dat    


def request_property(CAS, property, conn, c):
    '''
    retrieves cleaned data from database 
    '''    
    c.execute("SELECT * FROM substance_properties WHERE CAS = '{qq}' AND property = '{pp}'".format(qq =  CAS, pp = property.replace("'","''")))
    dat = c.fetchall()
    return dat