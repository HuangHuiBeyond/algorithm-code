## 图的三种表示方式，每一种方式都能表示无向图和有向图，扩展之后也都能表示带权值图
## 1.邻接表：定义为每个节点所连接的节点的集合，一般用用数组表示这种映射关系
## 2.邻接矩阵：当节点i和j相连的时候，array[i][j] = 1,否则为0
## 3.边列表（边的集合，有向图时由前节点指向后节点）

## 三种表示方式的互相转化
## 1.邻接矩阵 -> 邻接表
## 2.邻接表 -> 邻接矩阵
## 3.边列表 -> 邻接表

graph_array = [[0, 0, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 1, 1],
               [1, 1, 0, 1, 1, 0, 0],
               [0, 0, 1, 0, 1, 0, 1],
               [0, 0, 1, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0],
               [0, 1, 0, 1, 0, 0, 0]]

graph_list = [[2],
              [2, 5, 6],
              [0, 1, 3, 4],
              [2, 4, 6],
              [2, 3],
              [1],
              [1, 3]]
edges = [[0, 2],
         [1, 2],
         [1, 5],
         [1, 6],
         [2, 3],
         [2, 4],
         [3, 4],    
         [3, 6]]


def array_to_list(graph_array):
    size = len(graph_array)
    length = len(graph_array[0])
    res = []
    for i in range(size):
        temp = []
        for j in range(length):
            if graph_array[i][j] == 1:
                temp.append(j)
        res.append(temp)
    return res
print(array_to_list(graph_array))


def list_to_array(graph_list):
    size = len(graph_list)
    res = []
    for i in range(size):
        temp = [0] * size
        for j in graph_list[i]:
            temp[j] = 1
        res.append(temp)
    return res
print(list_to_array(graph_list))


def edges_to_list(edges, n): ## n表示顶点数
    res = [[] for _ in range(n)]
    for  node1, node2 in edges:
        res[node1].append(node2)
        res[node2].append(node1)
    return res
print(edges_to_list(edges, 7))


def list_to_edges(graph_list):
    size = len(graph_list)
    res = []
    for i in range(size):
        for j in graph_list[i]:
            if j > i:
                res.append([i, j])
    return res
print(list_to_edges(graph_list))

def array_to_edges(graph_array):
        res = []
        size = len(graph_array)
        for i in range(size):
            for j in range(i, size):
                if graph_array[i][j] > 0 and graph_array[i][j] < MAX:
                    res.append([i, j, graph_array[i][j]])
        return res


def edges_to_array(edges, n):
    res = [[0] * n for _ in range(n)]
    for pre, cur in edges:
        res[pre][cur] = 1
        res[cur][pre] = 1
    return res
print(edges_to_array(edges, 7))



## 基于邻接表和队列的BFS
def BFS(graph_list, start_node):
    queue = []
    queue.append(start_node)
    visited = set()
    visited.add(start_node)
    res = []
    while len(queue) > 0:
        vertex = queue.pop(0)
        res.append(vertex)
        for node in graph_list[vertex]:
            if node not in visited:
                queue.append(node)
                visited.add(node)            
    return res
print(BFS(graph_list, 1))

# 基于邻接表和栈的DFS
def DFS(graph_list, start_node):
    stack = []
    stack.append(start_node)
    visited = set()
    visited.add(start_node)
    res = []
    while len(stack) > 0:
        vertex = stack.pop()
        res.append(vertex)
        for node in graph_list[vertex]:
            if node not in visited:
                stack.append(node)
                visited.add(node)            
    return res
print(DFS(graph_list, 1))

## 基于邻接表和递归的DFS
def DFS1(graph_list, start_node):
    res = []
    visited = set()
    def _dfs(node, visited):
        res.append(node)
        visited.add(node)
        for i in graph_list[node]:
            if i not in visited:
                _dfs(i, visited)
    _dfs(start_node, visited)
    return res
print(DFS1(graph_list, 1))


## leetcode207：判断有向图是否有环
## 输入：边列表表示的有向图
## 输出：有向图是否有环（从有向图的某一个节点出发，最后又能回到该节点）
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 方法1：通过入度来检查是否有环，使用的是宽度优先遍历
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = []
        # Get the indegree and adjacency of every course. 
        for cur, pre in prerequisites:  
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # Get all the courses with the indegree of 0. ## 使用队列，所以是bfs
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
        # BFS TopSort.
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)
        return not numCourses

        ## 方法2：通过深度优先遍历，从某一个节点出发，又回到了这个节点，证明有环存在。这种场景下只能使用深度优先遍历
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True  
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True
        
        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True

## leetcode210：拓扑排序：找出无环有向图的一种可行排序
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 方法1：深度优先遍历
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            stack.append(i)
            return True
        
        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        stack = []
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return []
        return stack[::-1]  ## 最先入栈的是最后要学的


        ## 方法2：入度法，用队列
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = []
        res = []
        # Get the indegree and adjacency of every course. 
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # Get all the courses with the indegree of 0. ## 使用队列，所以是bfs
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
        # BFS TopSort.
        while queue:
            pre = queue.pop(0)
            res.append(pre)
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur)  ## 检查入度，为0加入队列
        return res if not numCourses else []




## 关键路径
## 解决完成一件工作需要的最少时间（拓扑排序主要解决一件工作能否顺利进行）
## 关键路径指的是从起点到终点具有最大权值和的路径
graph_list = [[[1, 3], [2, 4]], 
               [[3, 5], [4, 6]],
               [[5, 7], [3, 8]],
               [[4, 3]],
               [[7, 4], [6, 9]], 
               [[7, 6]],
               [[9, 2]],
               [[8, 5]], 
               [[9, 3]], 
               []]


def TopoSort(graph_list):
        ## 方法2：入度法，用队列

        ## 针对graph_list写一个拓扑排序 
        size = len(graph_list)
        indegrees = [0 for _ in range(size)]
        queue = []
        res = []
        for i in graph_list:
            for j in i:
                indegrees[j[0]] += 1
        # Get all the courses with the indegree of 0. ## 使用队列，所以是bfs
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
        # BFS TopSort.
        while queue:
            pre = queue.pop(0)
            res.append(pre)
            size -= 1
            for cur in graph_list[pre]:
                indegrees[cur[0]] -= 1
                if not indegrees[cur[0]]: queue.append(cur[0])  ## 检查入度，为0加入队列
        return res if not size else []
# print(TopoSort(graph_list))



def list_to_array(graph_list):
    size = len(graph_list)
    res = []
    for i in range(size):
        temp = [0] * size
        for j in graph_list[i]:
            temp[j[0]] = j[1]
        res.append(temp)
    return res
graph = list_to_array(graph_list)
# print(graph)


def events_earliest_time(vnum, graph, toposeq):
    ee = [0] * vnum
    for i in toposeq:
        for j in range(vnum):
            if graph[i][j] != 0:
                if ee[i] + graph[i][j] > ee[j]:
                    ee[j] = ee[i] + graph[i][j]
    return ee

def events_latest_time(vnum, graph, toposeq, eelast):
    le = [eelast] * vnum
    for k in range(vnum - 2, -1, -1):
        i = toposeq[k]
        for j in range(vnum):
            if graph[i][j] != 0:
                if le[j] - graph[i][j] < le[i]:
                    le[i] = le[j] - graph[i][j]
    return le

vnum = len(graph)
toposeq = TopoSort(graph_list)
ee = events_earliest_time(vnum, graph, toposeq)
print(ee)
le = events_latest_time(vnum, graph, toposeq, max(ee))
print(le)

def critical_path(graph_list):
    def list_to_array(graph_list):
        size = len(graph_list)
        res = []
        for i in range(size):
            temp = [0] * size
            for j in graph_list[i]:
                temp[j[0]] = j[1]
            res.append(temp)
        return res
    graph = list_to_array(graph_list)

    def events_earliest_time(vnum, graph, toposeq):
        ee = [0] * vnum
        for i in toposeq:
            for j in range(vnum):
                if graph[i][j] != 0:
                    if ee[i] + graph[i][j] > ee[j]:
                        ee[j] = ee[i] + graph[i][j]
        return ee

    def events_latest_time(vnum, graph, toposeq, eelast):
        le = [eelast] * vnum
        for k in range(vnum - 2, -1, -1):
            i = toposeq[k]
            for j in range(vnum):
                if graph[i][j] != 0:
                    if le[j] - graph[i][j] < le[i]:
                        le[i] = le[j] - graph[i][j]
        return le
    
    def crt_path(vnum, graph, ee, le):
        crt_path = []
        for i in range(vnum):
            for j in range(vnum):
                if graph[i][j] > 0:
                    if ee[i] == le[j] - graph[i][j]:
                        crt_path.append((i, j, graph[i][j]))
        return crt_path, sum([i[2] for i in crt_path])

    toposeq = TopoSort(graph_list)
    if not toposeq:
        return False
    vnum = len(graph)
    ee = events_earliest_time(vnum, graph, toposeq)
    le = events_latest_time(vnum, graph, toposeq, ee[-1])
    return crt_path(vnum, graph, ee, le)
crt_path = critical_path(graph_list)
print(crt_path)




## 最小生成树
## 解决的是给定一个n个节点的带权重的无向连通图，求权重之和最小的n-1条边
## 输入带权值的无向连通图（连通图的定义：任意两个点都有路径相连）
## 邻接矩阵表示
MAX = float('inf')
graph_array = [[0, 34, 46, MAX, MAX, 16],
               [34, 0, MAX, MAX, 12, MAX],
               [46, MAX, 0, 17, MAX, 25],
               [MAX, MAX, 17, 0, 38, 25],
               [MAX, 12, MAX, 38, 0, 26],
               [16, MAX, 25, 25, 26, 0]]
## kruskal是基于边的算法，需要用边列表来表示图
## 
def kruskal(graph_array):
    size = len(graph_array)

    def array_to_edges(graph_array):
        res = []
        for i in range(size):
            for j in range(i, size):
                if graph_array[i][j] > 0 and graph_array[i][j] < MAX:
                    res.append([i, j, graph_array[i][j]])
        return res
    edges = array_to_edges(graph_array)
    edges.sort(key = lambda x:x[2]) ## 从小到大排序，从最小的开始选
    
    group = [[i] for i in range(size)]
    res = []
    for edge in edges:
        for i in range(len(group)):
            if edge[0] in group[i]:
                m = i
            if edge[1] in group[i]:
                n = i
        if m != n:
            res.append(edge)  ## 结果是边的集合
            group[m] = group[m] + group[n]
            group[n] = []
    return res,sum([i[2] for i in res])
print(kruskal(graph_array))


## prim算法是基于顶点的算法，用邻接矩阵来表示就可以
def prim(graph_array):
    res = []
    size = len(graph_array)
    seleted_node = [0]
    candidate_node = [i for i in range(1, size)]  
    while len(candidate_node) > 0:
        begin, end, minweight = 0, 0, MAX
        for i in seleted_node:
            for j in candidate_node:
                if graph_array[i][j] < minweight:
                    minweight = graph_array[i][j]
                    begin = i
                    end = j
        res.append([begin, end, minweight])
        seleted_node.append(end)
        candidate_node.remove(end)
    return res, sum([i[2] for i in res])
print(prim(graph_array))




## 最短路径
## 连通图中起点到终点的最短距离（有无向均可）
## Dijkstra算法实现有向图最短路径

MAX = float('inf')
graph_array = [[0, 1, 12, MAX, MAX, MAX],
         [MAX, 0, 9, 3, MAX, MAX],
         [MAX, MAX, 0, MAX, 5, MAX],
         [MAX, MAX, 4, 0, 13, 15],
         [MAX, MAX, MAX, MAX, 0, 4],
         [MAX, MAX, MAX, MAX, MAX, 0]]


## 适用于输出给定城市到另外城市的最短路径
def Dijkstra(graph_array, node_of_interest):
    dis = {}
    for i in range(len(graph_array[node_of_interest])):
        
        dis[i] = graph_array[node_of_interest][i]

    visited = []

    min_dis = None
    min_dis_point = None

    for i in range(len(dis)):
        sort_dis = sorted(dis.items(), key=lambda item: item[1])
        # 找到dis中距离起始点距离最小的点
        for p, d in sort_dis:
            if p not in visited:
                min_dis_point = p
                min_dis = d
                visited.append(p)
                break
        for j in range(len(graph_array)):
            # 权重小于MAX的为相邻点
            if graph_array[min_dis_point][j] < MAX:
                update = min_dis + graph_array[min_dis_point][j]
                # 若经过min_dis_point到j的距离比起点直达j的距离大，则更新
                if dis[j] > update: 
                    dis[j] = update
    return dis
print(Dijkstra(graph_array, 2))

## 适用于输出任意一个城市出发到另一个城市的最短路径
def Floyd(graph_array):
    graph_dis = graph_array.copy()
    #k表示作为中转站的城市
    size = len(graph_dis)
    for k in range(size):
        #i同样表示起点
        for i in range(size):
            #j表示终点
            for j in range(size):
                update = graph_dis[i][k]+graph_dis[k][j]
                if graph_dis[i][j]>update:
                    graph_dis[i][j]=update
    return graph_dis
print(Floyd(graph_array))




## leetcode847：访问所有节点的最短路径
## graph用邻接表表示
def shortestPathLength(graph: List[List[int]]) -> int:
    n=len(graph)
    if n==1 and graph[0]==[]:
        return 0
    tar=(1<<n)-1
    ans=float('inf')
    
    def f(i):
        dic={(i,1<<i)}      #状态记录
        que={(i,1<<i)}      #宽搜队列
        tans=1      #临时步长记录
        while que:
            tmp=set()
            for j,t in que:     #que宽搜队列中，j节点，t已访问过的状态
                for k in graph[j]:      #遍历j节点的联通点
                    p=t|(1<<k)      #对节点进行访问
                    if p==tar:      #如果全部访问，就统计最短的临时步长
                        nonlocal ans
                        ans=min(ans,tans)
                        return
                    if (k,p) not in dic:        #不进入重复的状态
                        dic|={(k,p)}
                        tmp|={(k,p)}
            que=tmp
            tans+=1
        
    for i in range(n): #从各个节点开始走
        f(i)      
        
    return ans


## 旅行商问题
'''旅行商问题（Traveling Salesman Problem,TSP）'''

## 脚本之家代码
# 用邻接表表示带权图
# n = 5 # 节点数
# a,b,c,d,e = range(n) # 节点名称
# graph = [
#   {b:7, c:6, d:1, e:3},
#   {a:7, c:3, d:7, e:8},
#   {a:6, b:3, d:12, e:11},
#   {a:1, b:7, c:12, e:2},
#   {a:3, b:8, c:11, d:2}
# ]
# x = [0]*(n+1) # 一个解（n+1元数组，长度固定）
# X = []     # 一组解
# best_x = [0]*(n+1) # 已找到的最佳解（路径）
# min_cost = 0    # 最小旅费
# # 冲突检测
# def conflict(k):
#   global n,graph,x,best_x,min_cost, graph_list
#   # 第k个节点，是否前面已经走过
#   if k < n and x[k] in x[:k]:
#     return True
#   # 回到出发节点
#   if k == n and x[k] != x[0]:
#     return True
#   # 前面部分解的旅费之和超出已经找到的最小总旅费
#   cost = sum([graph[node1][node2] for node1,node2 in zip(x[:k], x[1:k+1])])
#   if 0 < min_cost < cost:
#     return True
#   return False # 无冲突
# # 旅行商问题（TSP）
# def tsp(k): # 到达（解x的）第k个节点
#   global n,a,b,c,d,e,graph,x,X,min_cost,best_x, graph_list
#   if k > n: # 解的长度超出，已走遍n+1个节点 （若不回到出发节点，则 k==n）
#     cost = sum([graph[node1][node2] for node1,node2 in zip(x[:-1], x[1:])]) # 计算总旅费
#     if min_cost == 0 or cost < min_cost:
#       best_x = x[:]
#       min_cost = cost
#       #print(x)
#   else:
#     for node in graph_list[x[k-1]]: # 遍历节点x[k-1]的邻接节点（状态空间）  ## 默认是遍历键
#       x[k] = node[0]
#       if not conflict(k): # 剪枝
#         tsp(k+1)
# # 测试
# x[0] = 3 # 出发节点：路径x的第一个节点（随便哪个）
# tsp(1)  # 开始处理解x中的第2个节点
# print(best_x)
# print(min_cost)

graph_list = [[[1, 7], [2, 6], [3, 1], [4, 3]],
         [[0, 7], [2, 3], [3, 7], [4, 8]],
         [[0, 6], [1, 3], [3, 12], [4, 11]],
         [[0, 1], [1, 7], [2, 12], [4, 2]],
         [[0, 3], [1, 8], [2, 11], [3, 2]]]

def TSP(graph_list, start_node):
    def list_to_array(graph_list):
        size = len(graph_list)
        res = []
        for i in range(size):
            temp = [0] * size
            for j in graph_list[i]:
                temp[j[0]] = j[1]
            res.append(temp)
        return res

    graph = list_to_array(graph_list)  
    n = len(graph_list)
    x = [0]*(n+1) # 一个解（n+1元数组，长度固定）
    best_x = [0]*(n+1) # 已找到的最佳解（路径）
    min_cost = float('inf')    # 最小旅费
    # 冲突检测
    def conflict(k):
    
        # 第k个节点，是否前面已经走过
        if k < n and x[k] in x[:k]:
            return True
        # 回到出发节点
        if k == n and x[k] != x[0]:
            return True
        # 前面部分解的旅费之和超出已经找到的最小总旅费
        cost = sum([graph[node1][node2] for node1,node2 in zip(x[:k], x[1:k+1])])
        if 0 < min_cost < cost:
            return True
        return False # 无冲突

    # 旅行商问题（TSP）
    def tsp(k): # 到达（解x的）第k个节点
        # nonlocal best_x
        nonlocal min_cost
        nonlocal best_x
    
        if k > n: # 解的长度超出，已走遍n+1个节点 （若不回到出发节点，则 k==n）
            cost = sum([graph[node1][node2] for node1,node2 in zip(x[:-1], x[1:])]) # 计算总旅费
            if  cost < min_cost:
                best_x = x[:]
                min_cost = cost
            #print(x)
        else:
            for node in graph_list[x[k-1]]: # 遍历节点x[k-1]的邻接节点（状态空间）  ## 默认是遍历键
                x[k] = node[0]
                if not conflict(k): # 剪枝
                    tsp(k+1)
    
    # 测试
    x[0] = start_node # 出发节点：路径x的第一个节点（随便哪个）
    tsp(1)  # 开始处理解x中的第2个节点
    return best_x, min_cost

print(TSP(graph_list, 2))




    



    
