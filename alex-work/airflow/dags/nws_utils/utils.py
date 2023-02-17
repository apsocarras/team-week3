from bs4 import BeautifulSoup

def ffList(ls:list) -> list:
  """Like ffill() from pandas, except for lists"""
  for i in range(len(ls)):
    if not ls[i] and i > 0:
        ls[i] = ls[i-1]
  return ls

def getColsFromTable(table:list, location:str):
  """Get cols from list of <tr> elements"""
  cols = [[ele.getText() for ele in tr.find_all("font")] for tr in table] # these are rows in the table's current landscape orientation
  location_col = ['location']
  location_col.extend([location]*24)
  cols.insert(1, location_col)
  cols.insert(19, location_col) # for second table
  return cols

def getDict(col_list:list):
  """Get dictionary from list of columns (which are also lists)"""
  data_map = {}
  for col in col_list:
    if col[0] not in data_map.keys(): # cols from first half of table
      data_map[col[0]] = col[1:]
    else: # cols from second half
      data_map[col[0]].extend(col[1:])
  data_map['Date'] = ffList(data_map['Date'])
  return data_map