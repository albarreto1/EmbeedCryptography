# A very simple python script that demonstrates how you can access
# memory and cpu usage information similar to how free and top 
# work on the Raspberry Pi. Goes with uCast #14 and #15.

# Usage: python pi_stats.py

import re, time, sys

class PiStats(object):
  def __init__(self):
    self.total_memory = None
    self.free_memory = None
    self.cached_memory = None
    self.lastCPUInfo = {'total':0, 'active':0}
    self.currentCPUInfo = {'total':0, 'active':0}
    self.temp_in_celsius = None

  def calculate_cpu_percentage(self):
    total_diff = self.currentCPUInfo['total'] - self.lastCPUInfo['total']
    active_diff = self.currentCPUInfo['active'] - self.lastCPUInfo['active']
    return round(float(active_diff) / float(total_diff), 3) * 100.00

  def update_stats(self):
    # Read memory usage from /proc/meminfo
    with open('/proc/meminfo', 'r') as mem_file:
      # Remove the text description, kB, and whitespace before
      # turning file lines into an int
      for i, line in enumerate(mem_file):
        if i == 0: # Total line
          self.total_memory = int(line.strip("MemTotal: \tkB\n")) / 1024
        elif i == 1: # Free line 
          self.free_memory = int(line.strip("MemFree: \tkB\n")) / 1024
        elif i == 4: # Cached line
          self.cached_memory = int(line.strip("Cached: \tkB\n")) / 1024

    self.lastCPUInfo['total'] = self.currentCPUInfo['total']
    self.lastCPUInfo['active'] = self.currentCPUInfo['active']
    self.currentCPUInfo['total'] = 0
    with open('/proc/stat', 'r') as cpu_file:
      for i, line in enumerate(cpu_file):
        if i == 0: 
          cpuStats = re.findall('([0-9]+)', line.strip())
          self.currentCPUInfo['idle'] = int(cpuStats[3]) + int(cpuStats[4])
          for t in cpuStats:
            self.currentCPUInfo['total'] += int(t)

          self.currentCPUInfo['active'] = self.currentCPUInfo['total'] - self.currentCPUInfo['idle']
          self.currentCPUInfo['percent'] = self.calculate_cpu_percentage()


  def get_memory_info(self):
    # In linux the cached memory is available for program use so we'll
    # include it in the free amount when calculating the usage percent
    used_val = (self.total_memory - self.free_memory)
    free_val = (self.free_memory)
    percent_val = float(used_val - self.cached_memory) / float(self.total_memory)
    return {'total': self.total_memory, 'cached': self.cached_memory,  'used': used_val, 'free': free_val, 'percent': round(percent_val, 3) * 100.00 }

  def get_cpu_info(self):
    return self.currentCPUInfo

    def cpuusage_main(title):
        stats = PiStats()
        stats.update_stats()
        meminfo = stats.get_memory_info()
        
        file = open(title, "w")
        file.write("total\tused\tfree\tcached\n")
        file.write("%i\t%i\t%i\t%i\n"%(meminfo['total'],meminfo['used'],meminfo['free'],meminfo['cached']))
        file.write("Memory Usage:\t%i%%"%(meminfo['percent']))
        file.write("\n")
        file.write("CPU Usage:\n")
        
        try:
          while True:
            cpu_info = stats.get_cpu_info()
            file.write("\t%i%%\n"%(cpu_info['percent']))
            time.sleep(2);
            stats.update_stats()
        except KeyboardInterrupt:
          file.close()
          print ("Exiting.\n")
          file.close()
          sys.exit(0)
