def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def get_convention():
  bar_labels = ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']
  bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:brown', 'tab:olive', 'tab:cyan']
  return bar_labels, bar_colors

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result
