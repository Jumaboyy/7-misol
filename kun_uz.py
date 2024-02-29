from database import db

def categori():
    category=input('Kategoriyani kiritng:')
    db.insert_category(category)
    ha_yoq=input('Yana kategoriya qo`shasizmi? : ')
    if ha_yoq=='ha':
        categori()

def run():
    while True:
        command=input('Sizga nima kerak ? (categori): ')
        if command=='stop':
            break
        elif command=='categori':
            categori()









if __name__ =='__main__':
    db.create_table_categories()
    db.create_table_articels()
    run()

