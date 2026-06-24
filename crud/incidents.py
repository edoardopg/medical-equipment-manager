from database import get_connection


class Incidents:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
    def insert(self,id_equipment,date,type_error,description):
        self.cursor.execute('''INSERT INTO incidents (id_equipment,date,type_error,description) VALUES (?,?,?,?)''',(id_equipment,date,type_error,description))
        self.conn.commit()
    def list(self):
        self.cursor.execute('''SELECT incidents.*, medical_equipments.name FROM incidents JOIN medical_equipments ON incidents.id_equipment = medical_equipments.id_equipment  
                    ''')
        return self.cursor.fetchall()
    def update(self,date,type_error,description,id_incident): 
        self.cursor.execute('''UPDATE incidents SET date=?,type_error=?,description=? WHERE id_incident=?''',(date,type_error,description,id_incident))
        self.conn.commit()
    def delete(self,id_incident):
        self.cursor.execute('''DELETE FROM incidents WHERE id_incident=?''',(id_incident,))
        self.conn.commit()
    def find_by_id(self,id_incident):
        self.cursor.execute('''SELECT incidents.*, medical_equipments.name FROM incidents JOIN medical_equipments ON incidents.id_equipment = medical_equipments.id_equipment WHERE id_incident=?''',(id_incident,))
        return self.cursor.fetchone()
    