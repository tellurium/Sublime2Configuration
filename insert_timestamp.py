import datetime
import sublime_plugin

class InsertTimestampCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    #generate the timestamp
    #timestamp_str = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    timestamp_str = datetime.datetime.now().strftime("%Y-%m-%d")


    #for region in the selection
    #(i.e. if you have multiple regions selected,
    # insert the timestamp in all of them)
    for r in self.view.sel():
      #put in the timestamp
      #(if text is selected, it'll be
      # replaced in an intuitive fashion)
      if r.size() > 0:
        self.view.replace(edit, r, timestamp_str)
      else:
        self.view.insert(edit, r.begin(), timestamp_str)