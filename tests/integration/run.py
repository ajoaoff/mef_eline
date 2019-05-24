import subprocess
from time import sleep
import sys


def run():
    kytos = subprocess.Popen(['kytosd', '-f', '-E'])
    sleep(5)
    subprocess.run(['bash', 'tests/integration/of_core.sh'])
    subprocess.run(['kytos', 'napps', 'disable', 'kytos/mef_eline'])
    subprocess.run(['kytos', 'napps', 'install', 'kytos/pathfinder'])
    subprocess.run(['kytos', 'napps', 'enable', 'kytos/topology'])
    subprocess.run(['kytos', 'napps', 'enable', 'kytos/storehouse'])
    subprocess.run(['kytos', 'napps', 'install', 'kytos/flow_manager'])
    sleep(2)
    subprocess.run(['kytos', 'napps', 'disable', 'kytos/of_core'])
    sleep(2)
    subprocess.run(['kytos', 'napps', 'enable', 'kytos/of_core'])
    subprocess.run(['kytos', 'napps', 'enable', 'kytos/mef_eline'])
    sleep(5)
    mininet = subprocess.Popen(['sudo', 'pytest', 'tests/integration/hooks/pre/mn_topo13.py'])
    sleep(10)
    subprocess.run(['tests/integration/run_tests.sh'])
    returncode = mininet.wait()
    kytos.terminate()
    return returncode


if __name__ == "__main__":
    sys.exit(run())
