from models import create_table, insert_initial_data, create_admin

def main():
    create_table()
    insert_initial_data()
    create_admin()

if __name__ == "__main__":
    main()