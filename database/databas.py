from sqlite3 import connect,Error


def createelontable():
    try:
        conn = connect('avtoelon.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE ELONLAR (
            ID integer primary key,
            user_id  integer not null,
            mashina_model text not null,
            mashina_yili integer not null,
            mashina_proberg integer not null,
            mashina_ranggi text not null,
            mashina_yoqilgisi text not null,
            Manzil text not null,
            mashina_narxi text not null,
            egasi_tel_raqami integer not null
                );

    ''')
        conn.commit()
        return 'bajarildi'
    except(Error,Exception) as e:
        print("xato",e)
    finally:
        if conn:
            c.close()
            conn.close()
    return 'bajarildi'


import sqlite3
from sqlite3 import Error

def delete_elon_from_db(elon_id ,user_id):

    try:
        conn = sqlite3.connect('avtoelon.db')
        c = conn.cursor()

        c.execute(
            "DELETE FROM ELONLAR WHERE ID = ? AND user_id = ?",
            (elon_id, user_id)
        )

        conn.commit()

        if c.rowcount > 0:
            return True
        return False
    except (Error, Exception) as e:
        print("Xatolik:", e)
        return False
    finally:
        if conn:
            c.close()
            conn.close()

# createelontable()
def createtableizohlar():
    try:
        conn = connect('avtoelon.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IZOHLAR (
            ID integer primary key,
            user_id  integer not null,
            yuborgan_izoh text not null
                );

    ''')
        conn.commit()
        return 'bajarildi'
    except(Error,Exception) as e:
        print("xato",e)
    finally:
        if conn:
            c.close()
            conn.close()
    return 'bajarildi'
# createtableizohlar()
def insertizohlar(user_id,izohi):
    try:
        conn = connect('avtoelon.db')
        c = conn.cursor() 
        c.execute("INSERT INTO IZOHLAR (user_id,yuborgan_izoh) VALUES (?, ?)", (user_id,izohi))
        conn.commit()
        return 'bajarildi'
    except(Error,Exception) as e:
        print("xato",e)
    finally:
        if conn:
            c.close()
            conn.close()
    return 'bajarildi'
def readizobtable():
    try:
        conn = connect('avtoelon.db')
        c = conn.cursor()
        c.execute("SELECT * FROM IZOHLAR")
        rows = c.fetchall()
        return rows
    except(Error,Exception) as e:
        print("xato",e)
    finally:
        if conn:
            c.close()
            conn.close()
def inserttableelonlar(user_id, mashina_model, mashina_yili, mashina_proberg, mashina_ranggi, mashina_yoqilgisi, manzil, mashina_narxi, egasi_tel_raqami):
    try:
        conn = connect('avtoelon.db')
        c = conn.cursor()
        c.execute("INSERT INTO ELONLAR (user_id, mashina_model, mashina_yili, mashina_proberg, mashina_ranggi, mashina_yoqilgisi, manzil, mashina_narxi, egasi_tel_raqami) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                  (user_id, mashina_model, mashina_yili, mashina_proberg, mashina_ranggi, mashina_yoqilgisi, manzil, mashina_narxi, egasi_tel_raqami))
        conn.commit()
        return 'bajarildi'
    except (Error, Exception) as e:
        print("xato:", e)
    finally:
        if conn:
            c.close()
            conn.close()
        return 'bajarildi'
def readtableelonlar():
    try:
        conn = connect('avtoelon.db')
        c = conn.cursor()
        c.execute("SELECT * FROM ELONLAR")
        rows = c.fetchall()
        return rows
    except(Error, Exception) as e:
        print("xato",e)
    finally:
        if conn:
            c.close()
            conn.close()

def userscretetable():
    try:
        conn = connect('avtoelon.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE USERS (
            ID integer primary key,
            USERNAME text not null,
            USER_ID text not null
                  
                );
                   ''')
        conn.commit()
    except(Error,Exception) as e:
        print("xato",e)
    finally:
        if conn:
            c.close()
            conn.close()
# userscretetable()
def readusertable():
    try:
        conn = connect('avtoelon.db')
        c = conn.cursor()
        c.execute("SELECT * FROM USERS")
        rows = c.fetchall()
        return rows
    except(Error,Exception) as e:
        print("xato",e)
    finally:
        if conn:
            c.close()
            conn.close()

def insertusertable(username,user_id):
    try:
        conn = connect('avtoelon.db')
        c = conn.cursor()
        c.execute("INSERT INTO USERS (USERNAME, USER_ID) VALUES (?, ?)", (username, user_id))
        conn.commit()
        return 'bajarildi'
    except(Error,Exception) as e:
        print("xato",e)
    finally:
        if conn:
            c.close()
            conn.close()
        return 'bajarildi'
    

def adminscreatetable():
    try:
        conn = connect('avtoelon.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS ADMINS (
            ID integer primary key,
            admin_name text not null,
            USER_ID integer not null
            );
        ''')
        conn.commit()
    except (Error, Exception) as e:
        print("xato", e)
    finally:
        if conn:
            c.close()
            conn.close()

# adminscreatetable()
def add_admin(USER_ID,admin_name):
    try:
        conn = connect('avtoelon.db')
        c = conn.cursor()
        
        c.execute("INSERT INTO ADMINS (admin_name,USER_ID) VALUES (?,?)", (USER_ID,admin_name,))
        
        conn.commit()
        return 'bajarildi'
    except (Error, Exception) as e:
        print("xato", e)
    finally:
        if conn:
            c.close()
            conn.close()



def delete_admin(admin_id):
    conn = connect("avtoelon.db")
    if conn:
        try:
            c = conn.cursor()
            c.execute("DELETE FROM admins WHERE USER_ID = ?", (admin_id,))
            conn.commit()
        except Error as e:
            print(f"Xato: {e}")
        finally:
            conn.close()

def readadminstable():
    conn = connect("avtoelon.db")
    if conn:
        try:
            c = conn.cursor()
            c.execute("SELECT * FROM ADMINS")
            rows = c.fetchall()
            print(f"Adminlar: {rows}")  
            return rows
        except Error as e:
            print(f"Xato: {e}")
        finally:
            conn.close()
def delete_comment_from_db(comment_id):
    conn = connect("avtoelon.db")
    if conn:
        try:
            c = conn.cursor()
            c.execute("DELETE FROM IZOHLAR WHERE id = ?", (comment_id,))
            conn.commit()
        except Error as e:
            print(f"Xato: {e}")
        finally:
            conn.close()

# createelontable()
# createtableizohlar()
# userscretetable()
# adminscreatetable()
