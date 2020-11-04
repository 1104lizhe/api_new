import sys
import time
from _pytest import terminal


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    total = terminalreporter._numcollected
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    error = len(terminalreporter.stats.get('error', []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    pass_rate = '{:.2%}'.format(float(passed) / float(total))
    print("total:", total)
    print('passed:', passed)
    print('failed:', failed)
    print('error:', error)
    print('skipped:', skipped)
    print('通过率:', pass_rate)
    # terminalreporter._sessionstarttime 会话开始时间
    duration = time.time() - terminalreporter._sessionstarttime
    print('total times:', duration, 'seconds')
    #  通过率不到100%则不在继续执行
    if passed/total < 1:
        sys.exit(1)
    else:
        sys.exit(0)



if __name__ == '__main__':
    print(100 / 100)
    if 100 / 100 < 1:
        print(11111)
    a = '{:.2%}'.format(10 / 100)
    print(float(a))