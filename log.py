import sys
import logging
logging.basicConfig(filename="problem.log",level=logging.DEBUG)
logger = logging.getLogger()
my_list = [2, 3, 4]
try:
    x = 1 / 1
    for i in range(5):
        print(my_list[i])
except IndexError as ie:
    print(ie)
    print("Index Error")
    print(sys.exc_info())
    logger.info(ie)
    logger.error(ie)
except ZeroDivisionError as zde:
    print(zde)
    print("division by zero exception")
    print(sys.exc_info())
    logger.info(zde)
    logger.error(zde)
except Exception as e:
    print(e)
    print(" EXCEPTION")
    print(sys.exc_info())
    logger.info(e)
    logger.error(e)
else:
    logger.error("Everything is OK!")
finally:
    logger.info("Application finished!")

try:
    num = 0
    assert num != 0, "num is not equal to zerp "
except:
    print("this is not correct")

