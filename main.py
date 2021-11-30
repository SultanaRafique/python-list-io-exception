import logging
import sys
import os
if __name__ == '__main__':
    is_exist = os.path.exists("problem.log")
    print(is_exist)
    logging.basicConfig(filename="problem.log", level=logging.DEBUG)
    logger = logging.getLogger()
    info = "sultana, 30, PA"

    try:
        # with open("file.txt", mode="a") as f:
        # with open("file.txt", mode="x") as f:
        with open("file.txt", mode="r") as f:
            for line in f.read().split("\n"):
                f.write(info)
                # name, age, location = line.split(",")
                # print(f"name is: {name} age is: {age} location is: {location}")

            # f.write(info + "\n")
            print(f.read())
    except IOError as ie:
        logger.error(ie)
        print(sys.exc_info())
    except FileExistsError as fe:
        logger.error(fe)
        print(sys.exc_info())



