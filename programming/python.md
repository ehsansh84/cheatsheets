# Python cheatsheet by Ehsan Shirzadi

### Simple inline for:
```
l = [1,2,3,4,5,6,7,8,9]
p = [True if v > 5 else False for v in l]
```
Contents of p will be: `[False, False, False, False, False, True, True, True, True]`

### A good way to config logger:
```
import logging
logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("This is a debug log")
logger.info("This is an info log")
logger.critical("This is critical")
logger.error("An error occurred")
```

Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
