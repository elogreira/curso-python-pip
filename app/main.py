import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  
  
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  
  
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    bar_labels, bar_colors = utils.get_convention()
    chart_name = f"Población por año en {country['Country']}"
    charts.generate_bar_chart(country['Country'], labels, values, bar_labels, bar_colors, 'Tamaño', chart_name)
  
if __name__ == '__main__':
  run()