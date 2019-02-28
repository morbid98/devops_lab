import psutil
import configparser
import time
from crontab import CronTab
import json

cron = CronTab(user=True)
job = cron.new(command='python monitor.py')
job.every_reboot()
cron.write()

config = configparser.ConfigParser()
config.read('config.ini')
interval = int(config["common"]["interval"])
output = config["common"]["output"]


class LogMonitor:
    snapCount = 1

    @staticmethod
    def result():
        tStamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        cpu = psutil.cpu_percent(interval=1, percpu=True)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        io = psutil.disk_io_counters()
        net = psutil.net_io_counters()
        outCPU = "Overall cpu load(for each core)\n {}\n ".format(cpu)
        outMem = "Overall virtual memory load\n {} \n ".format(mem)
        outDisk = "Overall disk usage\n {}\n ".format(disk)
        outIO = "Overall I/O stats\n {}\n ".format(io)
        outNet = "Overall network stats\n {}\n ".format(net)
        outStat = [outCPU, outMem, outDisk, outIO, outNet]
        snapPrint = "SNAPSHOT {0}: {1}:\n".format(LogMonitor.snapCount, tStamp)
        if output == 'raw':
            with open("output.txt", "a") as file:
                file.write(snapPrint)
            for member in outStat:
                with open("output.txt", "a") as file:
                    file.write(member)
            LogMonitor.snapCount += 1
        elif output == 'json':
            with open("output.json", "a") as file:
                json.dump(snapPrint, file)
            for member in outStat:
                with open("output.json", 'a') as file:
                    json.dump(member, file)
        else:
            print("Check your config file, something is broken!")
            exit(1)


while True:
    LogMonitor.result()
    time.sleep(interval * 60)
