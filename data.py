import os
import sys
import json


class Data:
  def __init__(self, json_file):
    self.json_file = json_file
    self.f = open(json_file, 'r+')
    self.data = json.load(self.f)

  def get_data(self):
      return self.data

  def insert_data(self, name=None, url=None, price=None, lowest_price=None):
    item = {"name": name, "url": url,
            "price": price, "lowest_price": lowest_price}
    self.data.append(item)

  def flush(self):
      json_object = json.dumps(self.data)
      self.f.truncate(0)
      self.f.close()
      self.f = open(self.json_file, 'r+')
      self.f.write(json_object)
      self.f.flush()

  def close(self):
      self.flush()
      self.f.close()
      self.data=None
      self.f=None


# json_file = os.path.join(sys.path[0], "db.json")
# api = Data(json_file)
# api.insert_data("It Doesn’t Have to Be Crazy at Work",
#                 "https://www.amazon.it/Doesnt-Have-Be-Crazy-Work/dp/0008323445",
#                 1555, 1555)
# api.flush()
# print(api.get_data())
