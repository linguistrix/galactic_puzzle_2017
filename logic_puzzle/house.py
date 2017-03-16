class House:
  def __init__(self):
    self.color = None
    self.person = None

  def __str__(self):
    return "%s, %s" % (str(self.color), str(self.person))