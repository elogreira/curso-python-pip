import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values, bar_labels, bar_colors, ylabel, chart_name):
  fig, ax = plt.subplots()
  ax.bar(labels, values, label=bar_labels, color=bar_colors)
  ax.set_ylabel(ylabel)
  ax.set_title(chart_name)
  ax.legend(title='Convenciones')
  #plt.show()
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  #plt.show()
  plt.savefig('chart_pie_final_este_si.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  bar_labels = ['a', 'b', 'c']
  bar_colors = ['tab:red', 'tab:blue', 'tab:green']
  ylabel = 'Valores Eje Y'
  chart_name = 'Gráfica de Prueba'
  generate_bar_chart(labels, values, bar_labels, bar_colors, ylabel, chart_name)
  # generate_pie_chart(labels, values)