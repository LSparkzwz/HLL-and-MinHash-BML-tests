data1 = ["745","756","784","984","4344"]
data2 = ["784","806","984","1014","1068","1074","1093","1114","1137","1160","1176","1184","1197","1217","1234","1239","1241","1252","1264","1265","1266","1267","1272","1277","1283","1291","1301","1321","1325","1358","1359","1363","1370","1374","1390","1408","1409","1411","1412","1413","1418","1422","1433","1454","1461","1468","1474","1482","1490","1492","1493","1494","1497","1499","1501","1503","1506","1509","1512","1513","1515","1516","1519","1521","1523","1530","1536","1538","1541","1548","1550","1551","1553","1554","1555","1556","1566","1567","1568","1570","1571","1572","1573","1575","1577","1578","1579","1580","1581","1588","1589","1590","1592","1593","1594","1596","1598","1599","1600","1601","1604","1607","1608","1609","1610","1611","1612","1615","1618","1619","1620","1621","1622","1624","1627","1628","1629","1630","1631","1632","1633","1634","1635","1636","1637","1638","1639","1641","1642","1643","1644","1645","1646","1647","1648","1649","1650","1651","1652","1653","1654","1655","1656"]

set_data1 = set(data1)
set_data2 = set(data2)

from functions.true_inclusion_coeff import true_inclusion_coeff
from functions.hll_bml import hll_bml
from functions.minHash_bml import minHash_bml
from memory_profiler import profile
import timeit

@profile
def mem_true_inclusion_coeff(SX,SY):
    true_inclusion_coeff(SX, SY)
    
@profile
def mem_hll_bml(SX,SY):
    hll_bml(SX,SY)

@profile
def mem_minHash_bml(SX,SY):
    minHash_bml(SX, SY)

mem_true_inclusion_coeff(SX=set_data1, SY=set_data2)
mem_hll_bml(SX=data1,SY=data2)
mem_minHash_bml(SX=set_data1, SY=set_data2)

import cProfile

print("Execution times")
#running the functions one more time to avoid conflict with the memory profiler

cProfile.run('true_inclusion_coeff(SX=set_data1, SY=set_data2)')
cProfile.run('hll_bml(SX=data1,SY=data2)')
cProfile.run('minHash_bml(SX=set_data1, SY=set_data2)')
