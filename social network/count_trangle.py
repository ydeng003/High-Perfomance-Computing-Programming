from pyspark import SparkContext
sc = SparkContext(appName="count_trangle")
from operator import add
import sys

if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: count_trangle_pyspark <input_file> <output_file>"
        exit(-1)

def find_vertex(line):
    result = []
    lines = line.collect()
    for line in lines:
        vex, ends = line.split(' ')
        ends = ends.split(',')
        ends = sorted(ends)
        for end in ends:
            result.append(vex + ','+ end + ' '+ str(-1))

        for i in range(len(ends)):
            for j in range(i + 1, len(ends)):
                result.append(ends[i] + ',' + ends[j] + ' '+ str(vex))
    return result
    
def find_trangle(vertexs):
    edges = []
    ends = []
    result = []
    for vex in vertexs:
        key, value = vex.split(' ')
        if value == str(-1):
            edges.append(key)
        else:
            ends.append(vex)
    for end in ends:
        e , s = end.split(' ')
        e1, e2 = e.split(',')
        if s < e1:
            if e in edges:
                result.append((int(s) ,int(e1),int(e2)))
    return result    


lines = sc.textFile(sys.argv[1])
vertexs = find_vertex(lines)
trangles = find_trangle(vertexs)
sc.parallelize(trangles).saveAsTextFile(sys.argv[2])
sc.stop()

