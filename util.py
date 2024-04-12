def get_census_codes(minority):
    
    assert minority in {'Asian', 'Black', 'Hispanic', 'Native'}
    
    # Census codes available at http://starr.tamu.edu/files/2013/01/Census-Codes.pdf
    if minority == 'Asian':
        codes = ['P0030006'] # Asian alone
        codes += ['P0030013','P0030017','P0030020','P0030023','P0030024'] # Asian (among 2 races)
        codes += ['P0030028','P0030031','P0030034','P0030035','P0030037','P0030040','P0030041','P0030043','P0030044','P0030046'] # 3
        codes += ['P0030048','P0030051','P0030052','P0030054','P0030055','P0030057','P0030058','P0030059','P0030061','P0030062'] # 4
        codes += ['P0030064','P0030065','P0030067','P0030068','P0030069'] # 5
        codes += ['P0030071'] # 6
    elif minority == 'Black':
        codes = ['P0030004'] # Black or African American alone 
        codes += ['P0030011','P0030016','P0030017','P0030018','P0030019'] # Black or African American (among 2 races)
        codes += ['P0030027','P0030028','P0030029','P0030030','P0030037','P0030038','P0030039','P0030040','P0030041','P0030042'] # 3
        codes += ['P0030048','P0030049','P0030050','P0030051','P0030052','P0030053','P0030058','P0030059','P0030060','P0030061'] # 4
        codes += ['P0030064','P0030065', 'P0030066','P0030067','P0030069'] # 5
        codes += ['P0030071'] # 6
    elif minority == 'Hispanic':
        codes = ['P0040002'] # Hispanic or Latino VAP
    elif minority == 'Native':
        codes = ['P0030005'] # American Indian and Alaska Native alone
        codes += ['P0030012','P0030016','P0030020','P0030021','P0030022'] # American Indian and Alaska Native (among 2 races)
        codes += ['P0030027','P0030031','P0030032','P0030033','P0030037','P0030038','P0030039','P0030043','P0030044','P0030045'] # 3
        codes += ['P0030048','P0030049','P0030050','P0030054','P0030055','P0030056','P0030058','P0030059','P0030060','P0030062'] # 4
        codes += ['P0030064','P0030065','P0030066','P0030068','P0030069'] # 5
        codes += ['P0030071'] # 6
            
    return codes

number_of_districts = {
    ('AL','CD'): 7, ('AL','SS'): 35, ('AL','SH'): 105,
    ('AK','CD'): 1, ('AK','SS'): 20, ('AK','SH'): 40,
    ('AZ','CD'): 9, ('AZ','SS'): 30, ('AZ','SH'): 30,
    ('AR','CD'): 4, ('AR','SS'): 35, ('AR','SH'): 100,
    ('CA','CD'): 52, ('CA','SS'): 40, ('CA','SH'): 80,
    ('CO','CD'): 8, ('CO','SS'): 35, ('CO','SH'): 65,
    ('CT','CD'): 5, ('CT','SS'): 36, ('CT','SH'): 151,
    ('DE','CD'): 1, ('DE','SS'): 21, ('DE','SH'): 41,
    ('FL','CD'): 28, ('FL','SS'): 40, ('FL','SH'): 120,
    ('GA','CD'): 14, ('GA','SS'): 56, ('GA','SH'): 180,
    ('HI','CD'): 2, ('HI','SS'): 25, ('HI','SH'): 51,
    ('ID','CD'): 2, ('ID','SS'): 35, ('ID','SH'): 35,
    ('IL','CD'): 17, ('IL','SS'): 59, ('IL','SH'): 118,
    ('IN','CD'): 9, ('IN','SS'): 50, ('IN','SH'): 100,
    ('IA','CD'): 4, ('IA','SS'): 50, ('IA','SH'): 100,
    ('KS','CD'): 4, ('KS','SS'): 40, ('KS','SH'): 125,
    ('KY','CD'): 6, ('KY','SS'): 38, ('KY','SH'): 100,
    ('LA','CD'): 6, ('LA','SS'): 39, ('LA','SH'): 105,
    ('ME','CD'): 2, ('ME','SS'): 35, ('ME','SH'): 151,
    ('MD','CD'): 8, ('MD','SS'): 47, ('MD','SH'): 47,
    ('MA','CD'): 9, ('MA','SS'): 40, ('MA','SH'): 160,
    ('MI','CD'): 13, ('MI','SS'): 38, ('MI','SH'): 110,
    ('MN','CD'): 8, ('MN','SS'): 67, ('MN','SH'): 134,
    ('MS','CD'): 4, ('MS','SS'): 52, ('MS','SH'): 122,
    ('MO','CD'): 8, ('MO','SS'): 34, ('MO','SH'): 163,
    ('MT','CD'): 2, ('MT','SS'): 50, ('MT','SH'): 100,
    ('NE','CD'): 3, ('NE','SS'): 49, ('NE','SH'): 0,
    ('NV','CD'): 4, ('NV','SS'): 21, ('NV','SH'): 42,
    ('NH','CD'): 2, ('NH','SS'): 24, ('NH','SH'): 400,
    ('NJ','CD'): 12, ('NJ','SS'): 40, ('NJ','SH'): 40,
    ('NM','CD'): 3, ('NM','SS'): 42, ('NM','SH'): 70,
    ('NY','CD'): 26, ('NY','SS'): 63, ('NY','SH'): 150,
    ('NC','CD'): 14, ('NC','SS'): 50, ('NC','SH'): 120,
    ('ND','CD'): 1, ('ND','SS'): 47, ('ND','SH'): 47,
    ('OH','CD'): 15, ('OH','SS'): 33, ('OH','SH'): 99,
    ('OK','CD'): 5, ('OK','SS'): 48, ('OK','SH'): 101,
    ('OR','CD'): 6, ('OR','SS'): 30, ('OR','SH'): 60,
    ('PA','CD'): 17, ('PA','SS'): 50, ('PA','SH'): 203,
    ('RI','CD'): 2, ('RI','SS'): 38, ('RI','SH'): 75,
    ('SC','CD'): 7, ('SC','SS'): 46, ('SC','SH'): 124,
    ('SD','CD'): 1, ('SD','SS'): 35, ('SD','SH'): 35,
    ('TN','CD'): 9, ('TN','SS'): 33, ('TN','SH'): 99,
    ('TX','CD'): 38, ('TX','SS'): 31, ('TX','SH'): 150,
    ('UT','CD'): 4, ('UT','SS'): 29, ('UT','SH'): 75,
    ('VT','CD'): 1, ('VT','SS'): 30, ('VT','SH'): 150,
    ('VA','CD'): 11, ('VA','SS'): 40, ('VA','SH'): 100,
    ('WA','CD'): 10, ('WA','SS'): 49, ('WA','SH'): 49,
    ('WV','CD'): 2, ('WV','SS'): 17, ('WV','SH'): 100,
    ('WI','CD'): 8, ('WI','SS'): 33, ('WI','SH'): 99,
    ('WY','CD'): 1, ('WY','SS'): 31, ('WY','SH'): 62
}