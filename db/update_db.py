import sqlite3

def updateDB():
    '''ask the user about updatted values'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # ask the user which creature to update
    invalid = True
    while invalid:
        whichCreature = input('Which creature needs updating: ')
        if type(whichCreature) == str and whichCreature !='':
            invalid = False # or break
    # remember - every inout is ALWAYS a string value
    qty = int(float(input('Updated quantity? '))) # we could validate this also
    st = f'''
    UPDATE zoo
    SET count={qty}
    WHERE creature="{whichCreature}" 
    '''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    updateDB()