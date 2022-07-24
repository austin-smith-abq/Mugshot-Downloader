from inmates import collect_inmates
from PageClass import MDC, driver


inmates = collect_inmates()
for i in inmates:

    MDC(i, inmates[i]).get_mugshot()

driver.close()
