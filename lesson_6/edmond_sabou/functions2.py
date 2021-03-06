raw_data = [
    ('AL', ['0', '0', '0', '0', '0', '0', '0', '84', '0']),
    ('AT', ['75', '79', '81', '81', '82', '85', '89', '89', '90']),
    ('BA', ['0', '0', '0', '0', '0', '0', '0', '69', '72']),
    ('BE', ['77', '78', '80', '83', '82', '85', '86', '87', '90']),
    ('BG', ['45', '51', '54', '57', '59', '64', '67', '72', '75']),
    ('CH', ['0', '0', '0', '91', '0', '0', '93', '0', '96']),
    ('CY', ['57', '62', '65', '69', '71', '74', '79', '86', '90']),
    ('CZ', ['67', '73', '73', '78', '79', '82', '83', '86', '87']),
    ('DE', ['83', '85', '88', '89', '90', '92', '93', '94', '95']),
    ('DK', ['90', '92', '93', '93', '92', '94', '97', '93', '95']),
    ('EA', ['74', '76', '79', '81', '83', '85', '87', '89', '90']),
    ('EE', ['69', '74', '79', '83', '88', '86', '88', '90', '90']),
    ('EL', ['50', '54', '56', '66', '68', '69', '71', '76', '79']),
    ('ES', ['63', '67', '70', '74', '79', '82', '83', '86', '91']),
    ('FI', ['84', '87', '89', '90', '90', '92', '94', '94', '94']),
    ('FR', ['76', '80', '82', '83', '83', '86', '86', '89', '90']),
    ('HR', ['61', '66', '65', '68', '77', '77', '76', '82', '81']),
    ('HU', ['63', '67', '70', '73', '76', '79', '82', '83', '86']),
    ('IE', ['78', '81', '82', '82', '85', '87', '88', '89', '91']),
    ('IS', ['93', '95', '96', '96', '0', '0', '98', '99', '98']),
    ('IT', ['62', '63', '69', '73', '75', '79', '81', '84', '85']),
    ('LT', ['60', '60', '65', '66', '68', '72', '75', '78', '82']),
    ('LU', ['91', '93', '94', '96', '97', '97', '97', '93', '95']),
    ('LV', ['64', '69', '72', '73', '76', '77', '79', '82', '85']),
    ('ME', ['0', '55', '0', '0', '0', '0', '71', '72', '74']),
    ('MK', ['0', '58', '65', '68', '69', '75', '74', '79', '82']),
    ('MT', ['75', '77', '78', '80', '81', '81', '85', '84', '86']),
    ('NL', ['94', '94', '95', '96', '96', '97', '98', '98', '98']),
    ('NO', ['92', '93', '94', '93', '97', '97', '97', '96', '98']),
    ('PL', ['67', '70', '72', '75', '76', '80', '82', '84', '87']),
    ('PT', ['58', '61', '62', '65', '70', '74', '77', '79', '81']),
    ('RO', ['47', '54', '58', '61', '68', '72', '76', '81', '84']),
    ('RS', ['0', '0', '0', '0', '64', '0', '68', '73', '80']),
    ('SE', ['91', '92', '93', '90', '91', '94', '95', '93', '96']),
    ('SI', ['73', '74', '76', '77', '78', '78', '82', '87', '89']),
    ('SK', ['71', '75', '78', '78', '79', '81', '81', '81', '82']),
    ('TR', ['0', '47', '49', '60', '70', '76', '81', '84', '88']),
    ('UK', ['83', '87', '88', '90', '91', '93', '94', '95', '96']),
    ('XK', ['0', '0', '0', '0', '0', '0', '89', '93', '93']),
]


#######################################################################################################################
def create():
    new_dict = {country: data_list for country, data_list in raw_data}

    return {
        country: [
            {"year": str(year), "coverage": data}
            for year, data in enumerate(data_list, start=2011)
        ]
        for country, data_list in new_dict.items()
    }


#######################################################################################################################
#
# get_year_data(data_set, "2019")
#
# >>> {'2019': [('Romania', 84), ('Germany', 95), ..., ('Latvia', 85)]}
#
def get_year_data(new_data_set, year):
    #    print(type(new_data_set))
    #    print(new_data_set)
    new = {
        year: [(country, index["coverage"])
               for country in new_data_set.keys()
               for index in new_data_set[country]
               if index["year"] == year]  # Q: De ce este nevoie sa pun str(year)??
    }  # fara str imi returneaza asta -> {2019: []}

    return new


#######################################################################################################################
# get_country_data(dataset, "Romania")
#
# >>> {'Romania': [('2019', 84), ('2018', 86), ..., ('2011', 72)]}
#
def get_country_data(new_data_set, country):
    new2 = {
        country: [(value["year"], value["coverage"])
                  for value in new_data_set[country]]
    }

    return new2


#######################################################################################################################
def perform_average(country_data):

    # retrieve values only from the current dict. down-side: I have a list in a list
    only_values = [x for x in country_data.values()]

    # the result of this is a list of tuples
    flat_list = [outer for inner in only_values for outer in inner]

    # get the second value from the tuple which is the index need to calculate average
    test = [x[1] for x in flat_list]

    # transforms the list of str to int
    normal_list = [int(i) for i in test]

    average = sum(normal_list) / len(normal_list)
    print(f"\nThe average coverage per country is --> {average}")


##################################################################################
new_data_set = create()
print(new_data_set)

test = get_year_data(new_data_set, "2016")
print(test)

get2 = get_country_data(new_data_set, "RO")
print(get2)

country_data = get_country_data(new_data_set, "RO")
perform_average(country_data)
