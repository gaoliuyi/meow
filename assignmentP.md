# Cheating sheet

## 排序算法

### 1.冒泡排序

排序方法：从左向右扫，相邻两个逆序就交换，每一轮将最大的数放到最右边之后再从最左边继续扫

代码实现

```python
# Optimized Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if (swapped == False):
            break


# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)
    print(' '.join(map(str, arr)))
```

冒泡排序一般不适用于大数据

冒泡排序是稳定排序

当数组初始已经排序好时，复杂度为n，平均复杂度和最坏复杂度都是n^2

### 2.选择排序

排序方法：每次将未排序部分数组的最大（或最小）与最右（或最左）的数字进行交换

代码实现：

```python
A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

        # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print(' '.join(map(str, A)))

# Output: 11 12 22 25 64 
```

选择排序的复杂度都是n^2，是不稳定排序



### 3.插入排序

排序方法：从数列的第二个数字（第一个数字）开始，依次与数列中的数字比大小，直到找到合适的位置插入为止

代码实现

```python
def insertion_sort(arr):														# cost	times
    for i in range(1, len(arr)):										# c1		n
        j = i																				# c2 		n - 1
        
        # Insert arr[j] into the
        # sorted sequence arry[0..j-1]							#	0			n - 1
        while arr[j - 1] > arr[j] and j > 0:				# c4		\sum_{j=2}^{n} t_j
            arr[j - 1], arr[j] = arr[j], arr[j - 1] # c5		\sum_{j=2}^{n} t_j - 1
            j -= 1																	# c6		\sum_{j=2}^{n} t_j - 1


arr = [2, 6, 5, 1, 3, 4]
insertion_sort(arr)
print(arr)

# [1, 2, 3, 4, 5, 6]
```

最好时间复杂度n，平均n^2,最坏n^2，是稳定排序算法

### 4.快排

快排一般是先选数组最右（或最左）侧的数作为一个pivot，左指针从左往右找大于pivot的数，右指针从右往左找小于pivot的数，若逆序则左右指针所指的数交换，最终若左指针所指的数大于pivot则与pivot交换，并以左指针位置为分界递归

代码实现

```python
def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i <= j:
        while i <= right and arr[i] < pivot:
            i += 1
        while j >= left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


arr = [22, 11, 88, 66, 55, 77, 33, 44]
quicksort(arr, 0, len(arr) - 1)
print(arr)

# [11, 22, 33, 44, 55, 66, 77, 88]
```

最好复杂度nlogn,平均nlogn,最坏n^2,额外占用内存logn，不是稳定排序



### 5.归并排序

归并排序是将数组连续分为几乎等长的左右数组，之后将左右数组当中的最小数依次插到原数组的左侧，并将剩余的数加入数组，通过递归函数实现

```python
def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2

		L = arr[:mid]	# Dividing the array elements
		R = arr[mid:] # Into 2 halves

		mergeSort(L) # Sorting the first half
		mergeSort(R) # Sorting the second half

		i = j = k = 0
		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	mergeSort(arr)
	print(' '.join(map(str, arr)))
# Output: 5 6 7 11 12 13
```

稳定排序算法，且时间复杂度恒定为nlogn，但占用额外内存n



### 6.希尔排序

设置一个gap，将相隔gap的数左向右依次排序并逐渐以某种方式缩小gap，下面这种希尔排序的时间复杂度为n^2

```python
def shellSort(arr, n):
    # code here
    gap = n // 2

    while gap > 0:
        j = gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j < n:
            i = j - gap  # This will keep help in maintain gap value

            while i >= 0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]

                i = i - gap  # To check left side also
            # If the element present is greater than current element
            j += 1
        gap = gap // 2


# driver to check the code
arr2 = [12, 34, 54, 2, 3]

shellSort(arr2, len(arr2))
print(' '.join(map(str, arr2)))

# Output: 2 3 12 34 54
```

经过优化后的希尔排序最优为nlogn，平均n^(4/3),最坏n^(3/2),希尔排序不是稳定排序



## 线性数据结构：栈，队列，双端队列，线性表

### 栈 stack：

last in first out

| **Stack Operation** | **Stack Contents**   | **Return Value** |
| ------------------- | -------------------- | ---------------- |
| `s.isEmpty()`       | `[]`                 | `True`           |
| `s.push(4)`         | `[4]`                |                  |
| `s.push('dog')`     | `[4,'dog']`          |                  |
| `s.peek()`          | `[4,'dog']`          | `'dog'`          |
| `s.push(True)`      | `[4,'dog',True]`     |                  |
| `s.size()`          | `[4,'dog',True]`     | `3`              |
| `s.isEmpty()`       | `[4,'dog',True]`     | `False`          |
| `s.push(8.4)`       | `[4,'dog',True,8.4]` |                  |
| `s.pop()`           | `[4,'dog',True]`     | `8.4`            |
| `s.pop()`           | `[4,'dog']`          | `True`           |
| `s.size()`          | `[4,'dog']`          | `2`              |

###  类实现栈

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

s = Stack()
```

### 中序，前序和后序表达式

| **Infix Expression** | **Prefix Expression** | **Postfix Expression** |
| -------------------- | --------------------- | ---------------------- |
| A + B                | + A B                 | A B +                  |
| A + B * C            | + A * B C             | A B C * +              |

| **Infix Expression** | **Prefix Expression** | **Postfix Expression** |
| -------------------- | --------------------- | ---------------------- |
| (A + B) * C          | * + A B C             | A B + C *              |

| **Infix Expression** | **Prefix Expression** | **Postfix Expression** |
| -------------------- | --------------------- | ---------------------- |
| A + B * C + D        | + + A * B C D         | A B C * + D +          |
| (A + B) * (C + D)    | * + A B + C D         | A B + C D + *          |
| A * B + C * D        | + * A B * C D         | A B * C D * +          |
| A + B + C + D        | + + + A B C D         | A B + C + D +          |

### 队列 quene：

first in first out

| **Queue Operation** | **Queue Contents**   | **Return Value** |
| ------------------- | -------------------- | ---------------- |
| `q.isEmpty()`       | `[]`                 | `True`           |
| `q.enqueue(4)`      | `[4]`                |                  |
| `q.enqueue('dog')`  | `['dog',4]`          |                  |
| `q.enqueue(True)`   | `[True,'dog',4]`     |                  |
| `q.size()`          | `[True,'dog',4]`     | `3`              |
| `q.isEmpty()`       | `[True,'dog',4]`     | `False`          |
| `q.enqueue(8.4)`    | `[8.4,True,'dog',4]` |                  |
| `q.dequeue()`       | `[8.4,True,'dog']`   | `4`              |
| `q.dequeue()`       | `[8.4,True]`         | `'dog'`          |
| `q.size()`          | `[8.4,True]`         | `2`              |

类实现quene

```python
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()

q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
print(q.items)

q.dequeue()
print(q.items)
# output:
# [3, 'dog', 'hello']
# [3, 'dog']
```

### 双端队列

| **Deque Operation** | **Deque Contents**         | **Return Value** |
| ------------------- | -------------------------- | ---------------- |
| `d.isEmpty()`       | `[]`                       | `True`           |
| `d.addRear(4)`      | `[4]`                      |                  |
| `d.addRear('dog')`  | `['dog',4,]`               |                  |
| `d.addFront('cat')` | `['dog',4,'cat']`          |                  |
| `d.addFront(True)`  | `['dog',4,'cat',True]`     |                  |
| `d.size()`          | `['dog',4,'cat',True]`     | `4`              |
| `d.isEmpty()`       | `['dog',4,'cat',True]`     | `False`          |
| `d.addRear(8.4)`    | `[8.4,'dog',4,'cat',True]` |                  |
| `d.removeRear()`    | `['dog',4,'cat',True]`     | `8.4`            |
| `d.removeFront()`   | `['dog',4,'cat']`          | `True`           |

## 3.1 实现双端队列



```python
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
```





### 线性表：

线性表包含数组和链表，

数组是一种连续存储结构，它将线性表的元素按照一定的顺序依次存储在内存中的连续地址空间上。数组需要预先分配一定的内存空间，每个元素占用相同大小的内存空间，并可以通过索引来进行快速访问和操作元素。访问元素的时间复杂度为O(1)，因为可以直接计算元素的内存地址。然而，插入和删除元素的时间复杂度较高，平均为O(n)，因为需要移动其他元素来保持连续存储的特性。

**链表**是一种存储结构，它是线性表的链式存储方式。链表通过节点的相互链接来实现元素的存储。每个节点包含元素本身以及指向下一个节点的指针。链表的插入和删除操作非常高效，时间复杂度为O(1)，因为只需要调整节点的指针。然而，访问元素的时间复杂度较高，平均为O(n)，因为必须从头节点开始遍历链表直到找到目标元素。



如果需要频繁进行随机访问操作，数组是更好的选择。如果需要频繁进行插入和删除操作，链表更适合。通过了解它们的特点和性能，可以根据实际情况做出选择。



双端队列duque可以视为stack和quene的一个合体

## 并查集Disjoint Set

### 按照排序合并

```python
class DisjSet:
	def __init__(self, n):
		# Constructor to create and initialize sets of n items
		self.rank = [1] * n
		self.parent = [i for i in range(n)]


	# Finds set of given item x
	def find(self, x):
		
		# Finds the representative of the set that x is an element of
		if (self.parent[x] != x):
			
			# if x is not the parent of itself
			# Then x is not the representative of its set
			self.parent[x] = self.find(self.parent[x])
			
			# so we recursively call Find on its parent
			# and move i's node directly under the
			# representative of this set

		return self.parent[x]


	# Do union of two sets represented by x and y.
	def Union(self, x, y):
		
		# Find current sets of x and y
		xset = self.find(x)
		yset = self.find(y)

		# If they are already in same set
		if xset == yset:
			return

		# Put smaller ranked item under
		# bigger ranked item if ranks are different
		if self.rank[xset] < self.rank[yset]:
			self.parent[xset] = yset

		elif self.rank[xset] > self.rank[yset]:
			self.parent[yset] = xset

		# If ranks are same, then move y under x (doesn't matter
    # which one goes where) and increment rank of x's tree
		else:
			self.parent[yset] = xset
			self.rank[xset] = self.rank[xset] + 1
```

### 按照大小合并

```python
class UnionFind:
	def __init__(self, n):
		self.Parent = list(range(n))
		self.Size = [1] * n

	# Function to find the representative (or the root node) for the set that includes i
	def find(self, i):
		if self.Parent[i] != i:
			# Path compression: Make the parent of i the root of the set
			self.Parent[i] = self.find(self.Parent[i])
		return self.Parent[i]

	# Unites the set that includes i and the set that includes j by size
	def unionBySize(self, i, j):
		# Find the representatives (or the root nodes) for the set that includes i
		irep = self.find(i)

		# And do the same for the set that includes j
		jrep = self.find(j)

		# Elements are in the same set, no need to unite anything.
		if irep == jrep:
			return

		# Get the size of i’s tree
		isize = self.Size[irep]

		# Get the size of j’s tree
		jsize = self.Size[jrep]

		# If i’s size is less than j’s size
		if isize < jsize:
			# Then move i under j
			self.Parent[irep] = jrep

			# Increment j's size by i's size
			self.Size[jrep] += self.Size[irep]
		# Else if j’s size is less than i’s size
		else:
			# Then move j under i
			self.Parent[jrep] = irep

			# Increment i's size by j's size
			self.Size[irep] += self.Size[jrep]
```

#### 并查集的一种简单的写法

```python
def find(x):
    if p[x]==x:
        return x
    else:
        p[x]=find(p[x])
        return p[x]
```

## 图算法

### 拓扑排序

拓扑排序（Topological Sorting）是对有向无环图（DAG）进行排序的一种算法。它将图中的顶点按照一种线性顺序进行排列，使得对于任意的有向边 (u, v)，顶点 u 在排序中出现在顶点 v 的前面。

拓扑排序是对深度优先搜索的一种简单而强大的改进，其算法如下。 (1) 对图`g`调用`dfs(g)`。之所以调用深度优先搜索函数，是因为要计算每一个顶点的结束时间。 (2) 基于结束时间，将顶点按照递减顺序存储在列表中。 (3) 将有序列表作为拓扑排序的结果返回。

#### dfs求解拓扑排序：计算时间，按照时间顺序递减存储结果

#### bfs/kahn算法实现拓扑排序：计算每个顶点的入度，将入度为0的点依次加入

```python
from collections import deque, defaultdict

def topological_sort(graph):
    indegree = defaultdict(int)
    result = []
    queue = deque()

    # 计算每个顶点的入度
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    # 将入度为 0 的顶点加入队列
    for u in graph:
        if indegree[u] == 0:
            queue.append(u)

    # 执行拓扑排序
    while queue:
        u = queue.popleft()
        result.append(u)

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    # 检查是否存在环
    if len(result) == len(graph):
        return result
    else:
        return None
```

拓扑排序问题一定要小心输入数据中隐藏的孤立点



### 强连通单元

强连通单元：有向图中任意两点可以相互到达的子图

#### kosaraju算法：

1. **第一次DFS**：在第一次DFS中，我们对图进行标准的深度优先搜索，但是在此过程中，我们记录下顶点完成搜索的顺序。这一步的目的是为了找出每个顶点的完成时间（即结束时间）。
2. **反向图**：接下来，我们对原图取反，即将所有的边方向反转，得到反向图。
3. **第二次DFS**：在第二次DFS中，我们按照第一步中记录的顶点完成时间的逆序，对反向图进行DFS。这样，我们将找出反向图中的强连通分量。

Kosaraju算法的关键在于第二次DFS的顺序，它保证了在DFS的过程中，我们能够优先访问到整个图中的强连通分量。因此，Kosaraju算法的时间复杂度为O(V + E)，其中V是顶点数，E是边数。

```python
def dfs1(graph, node, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs1(graph, neighbor, visited, stack)
    stack.append(node)

def dfs2(graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs2(graph, neighbor, visited, component)

def kosaraju(graph):
    # Step 1: Perform first DFS to get finishing times
    stack = []
    visited = [False] * len(graph)
    for node in range(len(graph)):
        if not visited[node]:
            dfs1(graph, node, visited, stack)
    
    # Step 2: Transpose the graph
    transposed_graph = [[] for _ in range(len(graph))]
    for node in range(len(graph)):
        for neighbor in graph[node]:
            transposed_graph[neighbor].append(node)
    
    # Step 3: Perform second DFS on the transposed graph to find SCCs
    visited = [False] * len(graph)
    sccs = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            scc = []
            dfs2(transposed_graph, node, visited, scc)
            sccs.append(scc)
    return sccs
```

#### tarjan算法

Tarjan算法是一种图算法，用于查找有向图中的强连通分量。强连通分量是指在有向图中，存在一条路径可以从任意一个顶点到达另一个顶点的一组顶点。

Tarjan算法使用了一种称为深度优先搜索（DFS）的技术来遍历图，并在遍历的过程中标记和识别强连通分量。算法的基本思想是，通过在深度优先搜索的过程中维护一个栈来记录已经访问过的顶点，并为每个顶点分配一个"搜索次序"（DFS编号）和一个"最低链接值"。搜索次序表示顶点被首次访问的次序，最低链接值表示从当前顶点出发经过一系列边能到达的最早的顶点的搜索次序。

Tarjan算法的步骤如下：

1. 从图中选择一个未访问的顶点开始深度优先搜索。
2. 为当前顶点分配一个搜索次序和最低链接值，并将其入栈。
3. 对当前顶点的每个邻接顶点进行递归深度优先搜索，如果邻接顶点尚未被访问过，则递归调用。
4. 在递归回溯的过程中，更新当前顶点的最低链接值，使其指向当前顶点和其邻接顶点之间较小的搜索次序。
5. 如果当前顶点的最低链接值等于其自身的搜索次序，那么将从当前顶点开始的栈中的所有顶点弹出，并将它们构成一个强连通分量。

```python
def tarjan(graph):
    def dfs(node):
        nonlocal index, stack, indices, low_link, on_stack, sccs
        index += 1
        indices[node] = index
        low_link[node] = index
        stack.append(node)
        on_stack[node] = True
        
        for neighbor in graph[node]:
            if indices[neighbor] == 0:  # Neighbor not visited yet
                dfs(neighbor)
                low_link[node] = min(low_link[node], low_link[neighbor])
            elif on_stack[neighbor]:  # Neighbor is in the current SCC
                low_link[node] = min(low_link[node], indices[neighbor])
        
        if indices[node] == low_link[node]:
            scc = []
            while True:
                top = stack.pop()
                on_stack[top] = False
                scc.append(top)
                if top == node:
                    break
            sccs.append(scc)
    
    index = 0
    stack = []
    indices = [0] * len(graph)
    low_link = [0] * len(graph)
    on_stack = [False] * len(graph)
    sccs = []
    
    for node in range(len(graph)):
        if indices[node] == 0:
            dfs(node)
    
    return sccs
```

#### dijkestra算法

1. - Dijkstra算法使用优先队列（通常是最小堆）来保存待访问的顶点，并按照顶点到起始顶点的距离进行排序。它根据路径长度来决定下一个要访问的顶点，从而保证每次都是选择最短路径的顶点进行访问。

虽然Dijkstra算法的实现方式和BFS有些相似，但是它们解决的问题和具体实现细节有很大的不同。BFS适用于无权图的最短路径问题，而Dijkstra算法适用于有权图的最短路径问题。

为了记录从起点到各个终点的总开销，要利用Vertex类中的实例变量distance。该实例变量记录从起点到当前顶点的最小权重路径的总权重。Dijkstra算法针对图中的每个顶点都循环一次，但循环顺序是由一个优先级队列控制的。用来决定顺序的正是dist。在创建顶点时，将distance设为一个非常大的值。理论上可以将distance设为无穷大，但是实际一般将其设为一个大于所有可能出现的实际距离的值。



非常重要的一点是，Dijkstra算法只适用于边的权重均为正的情况。如果图2中有一条边的权重为负，那么Dijkstra算法永远不会退出。

#### *多源最短路径Floyd-Warshall算法



求解所有顶点之间的最短路径可以使用**Floyd-Warshall算法**，它是一种多源最短路径算法。Floyd-Warshall算法可以在有向图或无向图中找到任意两个顶点之间的最短路径。

算法的基本思想是通过一个二维数组来存储任意两个顶点之间的最短距离。初始时，这个数组包含图中各个顶点之间的直接边的权重，对于不直接相连的顶点，权重为无穷大。然后，通过迭代更新这个数组，逐步求得所有顶点之间的最短路径。

具体步骤如下：

1. 初始化一个二维数组`dist`，用于存储任意两个顶点之间的最短距离。初始时，`dist[i][j]`表示顶点i到顶点j的直接边的权重，如果i和j不直接相连，则权重为无穷大。

2. 对于每个顶点k，在更新`dist`数组时，考虑顶点k作为中间节点的情况。遍历所有的顶点对(i, j)，如果通过顶点k可以使得从顶点i到顶点j的路径变短，则更新`dist[i][j]`为更小的值。

   `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`

3. 重复进行上述步骤，对于每个顶点作为中间节点，进行迭代更新`dist`数组。最终，`dist`数组中存储的就是所有顶点之间的最短路径。

Floyd-Warshall算法的时间复杂度为$O(V^3)$，其中V是图中的顶点数。它适用于解决稠密图（边数较多）的最短路径问题，并且可以处理负权边和负权回路。

以下是一个使用Floyd-Warshall算法求解所有顶点之间最短路径的示例代码：

```python
def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif j in graph[i]:
                dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
```

#### 最小生成树：prim算法：适用于稠密图

```python
from pythonds3.graphs import PriorityQueue

def prim(graph,start):
    pq = PriorityQueue()
    for vertex in graph:
        vertex.distance = sys.maxsize
        vertex.previous = None
    start.distance = 0
    pq.buildHeap([(v.distance,v) for v in graph])
    while pq:
        distance, current_v = pq.delete()
        for next_v in current_v.get_eighbors():
          new_distance = current_v.get_neighbor(next_v)
          if next_v in pq and new_distance < next_v.distance:
              next_v.previous = current_v
              next_v.distance = new_distance
              pq.change_priority(next_v,new_distance)
```

#### 4.4.2 Kruskal and Disjoint Set



Kruskal算法通常与并查集（Disjoint Set）结构一起使用，但它们并不是同一种算法。

1. **Kruskal算法**：适用于稀疏图

   - Kruskal算法是一种用于解决最小生成树（MST）问题的贪心算法。它通过不断选择具有最小权重的边，并确保选择的边不形成环，最终构建出一个包含所有顶点的最小生成树。
   - 在Kruskal算法中，通常会使用并查集来维护图中顶点的连通性信息。当选择一条边时，通过并查集判断该边的两个端点是否属于同一个连通分量，以避免形成环。

2. **并查集（Disjoint Set）**：

   - 并查集是一种数据结构，用于管理元素的不相交集合。它通常支持两种操作：查找（Find）和合并（Union）。查找操作用于确定某个元素属于哪个集合，合并操作用于将两个集合合并为一个集合。
   - 在Kruskal算法中，我们可以使用并查集来快速判断两个顶点是否属于同一个连通分量。当我们遍历边并选择加入最小生成树时，可以通过并查集来检查该边的两个端点是否已经在同一个连通分量中，以避免形成环。
   - 将图中的所有边按照权重从小到大进行排序。
   - 初始化一个空的边集，用于存储最小生成树的边。
   - 重复以下步骤，直到边集中的边数等于顶点数减一或者所有边都已经考虑完毕：
     - 选择排序后的边集中权重最小的边。
     - 如果选择的边不会导致形成环路（即加入该边后，两个顶点不在同一个连通分量中），则将该边加入最小生成树的边集中。
   - 返回最小生成树的边集作为结果。

   Kruskal算法的核心思想是通过不断选择权重最小的边，并判断是否会形成环路来构建最小生成树。算法开始时，每个顶点都是一个独立的连通分量，随着边的不断加入，不同的连通分量逐渐合并为一个连通分量，直到最终形成最小生成树。

   ```python
   class DisjointSet:
       def __init__(self, num_vertices):
           self.parent = list(range(num_vertices))
           self.rank = [0] * num_vertices
   
       def find(self, x):
           if self.parent[x] != x:
               self.parent[x] = self.find(self.parent[x])
           return self.parent[x]
   
       def union(self, x, y):
           root_x = self.find(x)
           root_y = self.find(y)
   
           if root_x != root_y:
               if self.rank[root_x] < self.rank[root_y]:
                   self.parent[root_x] = root_y
               elif self.rank[root_x] > self.rank[root_y]:
                   self.parent[root_y] = root_x
               else:
                   self.parent[root_x] = root_y
                   self.rank[root_y] += 1
   
   
   def kruskal(graph):
       num_vertices = len(graph)
       edges = []
   
       # 构建边集
       for i in range(num_vertices):
           for j in range(i + 1, num_vertices):
               if graph[i][j] != 0:
                   edges.append((i, j, graph[i][j]))
   
       # 按照权重排序
       edges.sort(key=lambda x: x[2])
   
       # 初始化并查集
       disjoint_set = DisjointSet(num_vertices)
   
       # 构建最小生成树的边集
       minimum_spanning_tree = []
   
       for edge in edges:
           u, v, weight = edge
           if disjoint_set.find(u) != disjoint_set.find(v):
               disjoint_set.union(u, v)
               minimum_spanning_tree.append((u, v, weight))
   
       return minimum_spanning_tree
   ```







## 机考题目模版和典型题目汇总

### Prim最小生成树

#### 27880繁忙的厦门

```python
from heapq import *
n,m=map(int,input().split())
graph={}
for i in range(m):
    u,v,c=map(int,input().split())
    if u in graph:
        graph[u][v]=c
    else:
        graph[u]={}
        graph[u][v]=c
    if v in graph:
        graph[v][u]=c
    else:
        graph[v]={}
        graph[v][u]=c
h=[]
ans=0
heappush(h,(0,1))
v=set()
while h:
    x,y=heappop(h)
    if y in v:
        continue
    v.add(y)
    ans=max(x,ans)
    for u in graph[y]:
        dis=graph[y][u]
        heappush(h,(dis,u))
print(n-1,ans)
```

注意：prim的简单写法：每次弹出最小边节点，并将相邻节点压入堆，这样每次弹出堆的都是最小边，满足了prim的贪心算法要求

注意：heappush有两个参数（，）

#### 5442兔子与星空

```python
from heapq import *

n = int(input())
graph = {chr(i + 65): {} for i in range(n)}
for i in range(n - 1):
    s = list(input().split())
    m = int(s[1])
    if m != 0:
        for j in range(2, 2 * m + 1, 2):
            graph[s[j]][s[0]] = int(s[j + 1])
            graph[s[0]][s[j]] = int(s[j + 1])
mst = []
h = []
heappush(h, (0, 'A'))
v = set()
while h:
    x, y = heappop(h)
    if y in v:
        continue
    v.add(y)
    mst.append(x)
    for u,dis in graph[y].items():
        heappush(h, (dis, u))
print(sum(mst))

```

#### 1258 Agri Net

```python
from heapq import *
while True:
    try:
        n=int(input())
    except EOFError:
        break
    mat=[]
    d=0
    ans=0
    for i in range(n):
        mat.append(list(map(int,input().split())))
    v=set()
    h=[]
    heappush(h,(0,0))
    while h:
        x,y=heappop(h)
        if y in v:
            continue
        v.add(y)
        ans+=x
        dis=1e6
        for i in range(n):
            if mat[y][i]<dis:
                d=mat[y][i]
                heappush(h,(d,i))
    print(ans)
            
```



### 单调栈：

单调栈的题目感觉变形还是比较多的，单调栈实现的基本原理是按一个顺序将所有元素依次入栈，在入栈前将栈内比自己小（或大）的元素全部弹出，弹出后剩下的第一个元素即为第一个比自己大（或小）的元素

比如单调递增栈可以用于寻找比自己小的最后一个元素（正向建立栈）或者比自己大的第一个元素（反向建立栈）

单调递减栈同理

一些题目

#### 28203单调栈

```python
n=int(input())
num=list(map(int,input().split()))
stack=[]
ans=[0]*n
for i in range(n-1,-1,-1):
    while stack and num[stack[-1]]<=num[i]:
        stack.pop()
    if stack:
        ans[i]=stack[-1]+1
    stack.append(i)
print(*ans)
```

#### 28190奶牛排队

```python
ans=0
n=int(input())
h=[int(input()) for i in range(n)]
l=[-1]*n
r=[n]*n
stack=[]
for i in range(n):
    while stack and h[stack[-1]]<h[i]:
        stack.pop()
    if stack:
        l[i]=stack[-1]
    stack.append(i)
stack=[]
for i in range(n-1,-1,-1):
    while stack and h[stack[-1]]>h[i]:
        stack.pop()
    if stack:
        r[i]=stack[-1]
    stack.append(i)
for i in range(n-1,-1,-1):
    for j in range(l[i]+1,i):
        if r[j]>i:
            ans=max(ans,i-j+1)
            break
print(ans)
```



#### 26977接雨水

```python
n=int(input())
num=list(map(int,input().split()))
stack=[]
ans=0
minh=0
h=0
for i in range(n-1,-1,-1):
    while stack and num[stack[-1]]<num[i]:
        h=num[stack[-1]]
        stack.pop()
        if not stack:
            break
        minh=min(num[i],num[stack[-1]])
        d=stack[-1]-i-1
        ans+=(minh-h)*d
    stack.append(i)
print(ans)
```

接雨水这个题目还是挺难的，主要是得想清楚怎么算这个雨水量，能看出是单调栈但细节还是不好想

#### 27205 护林员盖房子 加强版

```python
m,n=map(int,input().split())
a=[list(map(int,input().split())) for i in range(m)]
def maxs(a):
    rows=len(a)
    cols=len(a[0])
    h=[0 for i in range(cols+1)]
    ans=0
 
    for i in range(rows):
        stack=[-1]
        for j in range(cols+1):
            if j==cols or a[i][j]==1:
                x=0
            else:
                x=h[j]+1
            h[j]=x
            while len(stack)>1 and h[stack[-1]]>x:
                ans=max(ans,h[stack[-1]]*(j-stack[-2]-1))
               
                stack.pop()
            stack.append(j)
    return ans
    
print(maxs(a))
                
```







### Dijkestra算法：

**Dijkstra算法**：Dijkstra算法用于解决单源最短路径问题，即从给定源节点到图中所有其他节点的最短路径。算法的基本思想是通过不断扩展离源节点最近的节点来逐步确定最短路径。具体步骤如下：

- 初始化一个距离数组，用于记录源节点到所有其他节点的最短距离。初始时，源节点的距离为0，其他节点的距离为无穷大。
- 选择一个未访问的节点中距离最小的节点作为当前节点。
- 更新当前节点的邻居节点的距离，如果通过当前节点到达邻居节点的路径比已知最短路径更短，则更新最短路径。
- 标记当前节点为已访问。
- 重复上述步骤，直到所有节点都被访问或者所有节点的最短路径都被确定。

Dijkstra算法的时间复杂度为O(V^2)，其中V是图中的节点数。当使用优先队列（如最小堆）来选择距离最小的节点时，可以将时间复杂度优化到O((V+E)logV)，其中E是图中的边数。

```python
# 03424: Candies
# http://cs101.openjudge.cn/practice/03424/
import heapq

def dijkstra(N, G, start):
    INF = float('inf')
    dist = [INF] * (N + 1)  # 存储源点到各个节点的最短距离
    dist[start] = 0  # 源点到自身的距离为0
    pq = [(0, start)]  # 使用优先队列，存储节点的最短距离
    while pq:
        d, node = heapq.heappop(pq)  # 弹出当前最短距离的节点
        if d > dist[node]:  # 如果该节点已经被更新过了，则跳过
            continue
        for neighbor, weight in G[node]:  # 遍历当前节点的所有邻居节点
            new_dist = dist[node] + weight  # 计算经当前节点到达邻居节点的距离
            if new_dist < dist[neighbor]:  # 如果新距离小于已知最短距离，则更新最短距离
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))  # 将邻居节点加入优先队列
    return dist



N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]  # 图的邻接表表示
for _ in range(M):
    s, e, w = map(int, input().split())
    G[s].append((e, w))


start_node = 1  # 源点
shortest_distances = dijkstra(N, G, start_node)  # 计算源点到各个节点的最短距离
print(shortest_distances[-1])  # 输出结果
```



#### 一些典型题目

#### 3424 candies

```python
from heapq import *
def dijk(n,g,start):
    dis=[float('inf')]*(n+1)
    dis[start]=0
    pq=[(0,start)]
    while pq:
        d,now=heappop(pq)
        if d>dis[now]:
            continue
        dis[now]=d
        for u,v in g[now]:
            newdis=dis[now]+v
            if newdis<dis[u]:
                dis[u]=newdis
                heappush(pq,(newdis,u))
    return dis
n,m=map(int,input().split())
g=[[] for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())    
    g[a].append((b,c))
start=1
ans=dijk(n,g,start)
print(ans[-1])
```

#### 21515电话线路

```python
from heapq import *
inf=float('inf')
n,p,k=map(int,input().split())
dist=[[inf]*(k+1) for i in range(n+1)]
vis=[[False]*(n+1) for i in range(n+1)]
g={i:[] for i in range(n+1)}
for _ in range(p):
    a,b,l=map(int,input().split())
    g[a].append((b,l))
    g[b].append((a,l))
def dijkestra(r=1):
    dist[r][0]=0
    h=[(0,r,0)]
    while h:
        x,i,j=heappop(h)
        if vis[i][j]:
            continue
        vis[i][j]=True
        for v,w in g[i]:
            if dist[v][j]>max(x,w):
                dist[v][j]=max(x,w)
                heappush(h,(dist[v][j],v,j))
            if j<k and dist[v][j+1]>x:
                dist[v][j+1]=dist[i][j]
                heappush(h,(dist[v][j+1],v,j+1))
    return dist
dijkestra(1)
ans=inf
for i in range(k+1):
    ans=min(ans,dist[n][i])
if ans!=inf:
    print(ans)
else:
    print(-1)
```

这个题目需要dijkestra+dp

#### 5443兔子与樱花

```python
from heapq import heappop,heappush
def dijkstra(graph,start,end):
    dis={place:float("inf") for place in places}
    pq=[(0,start)]
    dis[start]=0
    path={place:None for place in places}
    while pq:
        distance,node=heappop(pq)
        if distance>dis[node]:
            continue
        if node==end:
            return path
        for place,cost in graph[node].items():
            newdistance=distance+cost
            if newdistance<dis[place]:
                dis[place]=newdistance
                path[place]=node
                heappush(pq,(newdistance,place))
n=int(input())
places=[input().strip() for i in range(n)]
graph={place:{} for place in places}
q=int(input())
for i in range(q):
    a,b,c=input().split()
    c=int(c)
    graph[a][b]=c
    graph[b][a]=c
r=int(input())
for _ in range(r):
    a,b=input().split()
    if a==b:
        print(a)
        continue
    path=dijkstra(graph,a,b)
    way=[b]
    x=b
    while path[x] is not None:
        way.append(path[x])
        x=path[x]
    ans=''
    for i in range(len(way)-1,0,-1):
        ans+=f"{way[i]}->({graph[way[i]][way[i-1]]})->"
    ans+=f"{b}"
    print(ans)
```

这个题目需要典型的dijkestra，因为需要记录路径，故需要开一个path数组记录前驱

一般的比较简单的有向图最短路问题也可以直接用bfs+heapq解决

#### 如7735roads

```python
from heapq import *
k=int(input())
n=int(input())
r=int(input())
road=[[] for i in range(n+1)]
for i in range(r):
    s,d,l,t=map(int,input().split())
    road[s].append((l,d,t))
def dijk(road):
    h=[]
    vis=set()
    heappush(h,(0,1,0))
    while h:
        l,s,t=heappop(h)
        
        if s==n:
            return l
        if (s,t) in vis:
            continue
        vis.add((s,t))
        if road[s]:
            for dis,ns,dt in road[s]:
                nl=l+dis
                nt=dt+t
                if nt<=k:
                    heappush(h,(nl,ns,nt))
                    
                   
                    
    return -1
print(dijk(road))

```

### 拓扑排序：

拓扑排序是一种针对于有向无环图的算法，可以有效解决有向无环图（DAG）是否有环的问题

解决拓扑排序问题一般实际操作中使用Kahn算法会比较简单

#### 4084拓扑排序

```python
from collections import defaultdict
from heapq import *


def toposort(g):
    ind = defaultdict(int)
    ans = []
    h = []
    for u in g:
        for y in g[u]:
            ind[y] += 1
    for u in range(1,v+1):
        if ind[u] == 0:
            heappush(h, u)
    while h:
        u = heappop(h)
        ans.append(u)
        if u in g:
            for y in g[u]:
                ind[y] -= 1
                if ind[y] == 0:
                    heappush(h, y)

    return ans


v, a = map(int, input().split())
g = {}
for _ in range(a):
    b, c = map(int, input().split())
    if b not in g:
        g[b] = [c]
    else:
        g[b].append(c)
ans = toposort(g)
if ans:
    for i, vertex in enumerate(ans):
        if i < len(ans) - 1:
            print(f"v{vertex}", end=" ")
        else:
            print(f"v{vertex}")
else:
    print("No topological order exists due to a cycle in the graph.")

```

注意可能有孤立点没有被加入图中，但其入度仍为0，需要对其进行拓扑排序



#### 9202舰队、海域出击

```python
from collections import deque
for _  in range(int(input())):
    n,m=map(int,input().split())
    graph={}
    for i in range(1,n+1):
        graph[i]=[]
    ind=[0]*(n+1)
    ind[0]=100
    for i in range(m):
        x,y=map(int,input().split())
        if x in graph:
            graph[x].append(y)
        ind[y]+=1
    def toposort(graph,n):
        ans=[]
        q=deque()
        for u in graph:
            if ind[u]==0:
                q.append(u)
        while q:
            a=q.popleft()
            ans.append(a)
            if graph[a]:
                for i in graph[a]:
                    ind[i]-=1
                    if ind[i]==0:
                        q.append(i)
                
           
        if len(ans)==n:
            return 'No'
        else:
            return 'Yes'
    print(toposort(graph,n))
```

拓扑排序模版题，没有难度



一定要注意拓扑排序解决的是DAG的问题，如果是判断无向图的有环问题需要一种比较巧妙的方法

#### 27635判断无向图是否连通有无回路

```python

n,m=map(int,input().split())
g={i:[] for i in range(n)}
for _ in range(m):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)

def connect(g,n):
    i=1
    v=[False]*n
    stack=[0]
    v[0]=True
    while stack:
        node=stack.pop()
        for new in g[node]:
            if not v[new]:
                stack.append(new)
                v[new]=True
                i+=1
    if i==n:
        return True
def cycle(g,n):
    def dfs(node,v,father):
        v[node]=True
        for new in g[node]:
            if not v[new]:
                if dfs(new,v,node):
                    return True
            elif new!=father:
                return True
        return False
    v=[False]*n
    for i in range(n):
        if not v[i]:
            if dfs(i,v,-1):
                return True
    return False
if connect(g,n):
    print("connected:yes")
else:
    print('connected:no')
if cycle(g,n):
    print("loop:yes")
else:
    print('loop:no')
```



### 并查集Disjointset

常规并查集题目：

#### 1611 the suspects

```python
class DisjSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    x = DisjSet(n)
    for i in range(m):
        p = list(map(int, input().split()))
        for j in range(2, p[0] + 1):
            x.union(p[1], p[j])
    ans = 0
    for i in range(n):
        if x.find(i) == x.find(0):
            ans += 1
    print(ans)
```



有一点点变形的题目

#### 18250冰阔落

```python
ans=0

class Disjointset:
    def __init__(self,n):
        self.father=[0]+[i for i in range(1,n+1)]
    def find(self,x):
        if self.father[x]!=x:
            self.father[x]=self.find(self.father[x])
        return self.father[x]
    def union(self,x,y):
        global ans
        xset=self.find(x)
        yset=self.find(y)
        if xset==yset:
            print('Yes')
        else:
            print('No')
            self.father[yset]=xset
            ans+=1
            v.add(yset)
            
while True:
    try:
        n,m=map(int,input().split())
        ans=0
        v=set()
        v.add(0)
        disjset=Disjointset(n)
        for _ in range(m):
            x,y=map(int,input().split())
            disjset.union(x,y)
        print(n-ans)
        a=[i for i in range(1,n+1) if i not in v]
        print(*a)
    except EOFError:
        break
```

每次需要计算出合并的次数，得到最后剩下的冰阔落数量



一些比较烧脑的并查集题目，一般不是直接合并，而是告诉你两个东西不在一个集合里面，这时候要开几倍的空间利用差n的整数倍来标记合并

#### 1703 发现它，抓住它

```python
p=[]
def find(x):
    if p[x]==x:
        return x
    else:
        p[x]=find(p[x])
        return p[x]
for _ in range(int(input())):
    n,m=map(int,input().split())
    p=[i for i in range(2*n+1)]
    for i in range(m):
        s=input().split()
        b=int(s[1])
        c=int(s[2])
        if s[0]=='D':
            
            p[find(b+n)]=find(c)
            p[find(b)]=find(c+n)
        elif s[0]=="A":
            if find(b)==find(c):
                print('In the same gang.')
            elif find(b)==find(c+n) or find(c)==find(b+n):
                print('In different gangs.')
            else:
                print('Not sure yet.')
            
```

#### 1182食物链

```python
n,k=map(int,input().split())
p=[i for i in range(3*n+1)]
def find(x):
    if p[x]==x:
        return x
    else:
        p[x]=find(p[x])
        return p[x]
ans=0
for i in range(k):
    t,x,y=map(int,input().split())
    if x>n or y>n:
        ans+=1
        continue
    if t==1:
        if find(x+n)==find(y) or find(y+n)==find(x):
            ans+=1
            continue
        p[find(x)]=find(y)
        p[find(x+n)]=find(y+n)
        p[find(x+2*n)]=find(y+2*n)
    else:
        if find(x)==find(y) or find(x)==find(y+n):
            ans+=1
            continue
        p[find(x+n)]=find(y)
        p[find(x+2*n)]=find(y+n)
        p[find(x)]=find(y+2*n)
print(ans)
```

这两个题目本质相同，只是一个用了两倍空间一个用了3倍空间



### 一些稍微有一点点意思的bfs和dfs模版题

#### 28046词梯问题

```python

from collections import deque,defaultdict
from itertools import permutations
basket=defaultdict(list)
for _ in range(int(input())):
    word=input()
    for i in range(4):
        l=list(word)
        l[i]='-'
        basket["".join(l)].append(word)
graph=defaultdict(list)
for words in basket.values():
    for a,b in permutations(words,2):
        graph[a].append(b)
        graph[b].append(a)
start,end=input().split()
q=deque([start])
path={}
vis=set(q)
def bfs():
    while q:
        now=q.popleft()
        for new in graph[now]:
            if new not in vis:
                vis.add(new)
                path[new]=now
                q.append(new)
            if new==end:
                return True
ans=bfs()
if ans:
    n=end
    p=[n]
    while n in path:
        n=path[n]
        p.append(n)
    p.reverse()
    print(*p)
else:
    print('NO')
```

利用桶建图，首先建桶，再将桶转化成邻接表

#### 28050骑士周游

```python
n=int(input())
di=[(-2,-1),(-1,-2),(1,-2),(-2,1),(1,2),(2,1),(2,-1),(-1,2)]

vis=[[1]*n for i in range(n)]
def p(z):
    x,y=z
    edge=[]
    for i, j in di:
        nx = i + x
        ny = j + y
        if 0 <= nx < n and 0 <= ny < n and vis[nx][ny]==1:
            edge.append((nx,ny))
    return edge


def dfs(x,y,i):
    if i==n*n:
        return True
    vis[x][y]=10

    for nx,ny in sorted(p((x,y)),key=lambda z:len(p(z))):
        if vis[nx][ny]==1:
            if dfs(nx,ny,i+1):
                return True
            vis[nx][ny]=1
        else:
            break

sx,sy=map(int,input().split())
ans=dfs(sx,sy,1)
if ans:
    print('success')
else:
    print('fail')
```

warshall算法，首先走可选择的位置数少的格子，

### 树Tree

一些例题

#### 27638 求二叉树的高度和叶子数目

```python

class Tree:
    def __init__(self,left=None,right=None):
        self.left=left
        self.right=right

def height(node):
    if node is None:
        return -1
    return max(height(node.left),height(node.right))+1

def leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return leaves(node.left)+leaves(node.right)
n=int(input())   
nodes=[Tree() for i in range(n)] 
father=[-1]*n
for i in range(n):
    left,right=map(int,input().split())
    if left!=-1:
        nodes[i].left=nodes[left]
        father[left]=i
    if right!=-1:
        nodes[i].right=nodes[right]
        father[right]=i
root=father.index(-1)
print(height(nodes[root]),leaves(nodes[root]))
```

递归求解高度和叶子数目，存储父节点列表用于寻找树根

#### 树的遍历

#### 前序遍历

```python
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
```

#### 后序遍历

```python
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
```

#### 层序遍历

用队列实现

5455二叉搜索树的层次遍历

二叉搜索树BST的性质，左子树总是比根节点小，右子树总是比根节点大，最后排成一维是从小到大排序的

```python
from collections import deque
class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
p=list(map(int,input().split()))
n=len(p)
nodes=[Tree(p[i]) for i in range(n)]

for i in range(1,n):
    root=nodes[0]
    while True:
        if p[i]<root.val:
            if root.left:
                root=root.left
            else:
                root.left=nodes[i]
                break
        elif p[i]>root.val:
            if root.right:
                root=root.right
            else:
                root.right=nodes[i]
                break
        else:
            break
def pout(r):
    q=deque()
    q.append(r)
    ans=[]
    while q:
        node=q.popleft()
        ans.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print(*ans)
pout(nodes[0])
```

#### 已知前中推后序

```python
class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def solve(a,b):
    nodes=[Tree(x) for x in a]
    n=len(a)
    for i in range(1,n):
        if b.index(a[i])<b.index(a[i-1]):
            nodes[i-1].left=nodes[i]
        else:
             x=b.index(a[i])-1
             while True:
                 y=a.index(b[x])
                 if a.index(b[x])<i:
                     nodes[y].right=nodes[i]
                     break
                 x-=1
    return nodes[0]
def pout(root):
    if root.left:
        pout(root.left)
    if root.right:
        pout(root.right)
    if root.val:
        print(root.val,end='')
while True:
    try:
        a=input()
        b=input()
        root=solve(a,b)
        pout(root)
        print()
    except EOFError:
        break
```

前序找左儿子中序找右儿子





#### 前缀树Trie

4089电话号码

```python
class Tree:
    def __init__(self):
        self.child={}
class Tri:
    def __init__(self):
        self.root=Tree()
    def add(self,num):
        node=self.root
        for x in num:
            if x not in node.child:
                node.child[x]=Tree()
            node=node.child[x]
    def search(self,num):
        node=self.root
        for x in num:
            if x not in node.child:
                return 0
            node=node.child[x]
        return 1
for i in range(int(input())):
    t=[]
    for j in range(int(input())):
        t.append(list(input()))
    t.sort(reverse=True)
    tri=Tri()
    s=0
    for num in t:
        s+=tri.search(num)
        if s>0:
            print('NO')
            break
            
        tri.add(num)
        
    else:
        print('YES')
```

#### 多叉树

27928遍历树

```python
tree={}
nodes=[]
child=set()
n=int(input())
for i in range(n):
    s=list(map(int,input().split()))
    a=s[0]
    if len(s)>1:
        
        for i in s[1:]:
            child.add(i)
        s.sort()
        nodes.append(a)
        tree[a]=s
    else:
        nodes.append(a)
for x in nodes:
    if x not in child:
        root=x
        break
def pout(x):
    if x not in tree:
        print(x)
        return
    for y in tree[x]:
        if y==x:
            print(x)
        else:
            pout(y)
pout(root)
```

用字典建树，储存孩子的集合对比寻找根节点

#### 森林

7161森林的带度数层次序列存储

```python
from collections import deque
class Tree:
    def __init__(self,val):
        self.val=val
        self.child=[]
def buildtree(t):
    nodes=[Tree(t[i]) for i in range(0,len(t)-1,2)]
    r=(0,t[0],t[1])
    q=deque()
    q.append(r)
    i=2
    while q:
        a,b,c=q.popleft()
        c=int(c)
        if c!=0:
            for j in range(i,i+2*c,2):
                x=t[j]
                y=int(t[j+1])
                nodes[a>>1].child.append(nodes[j>>1])
                if y!=0:
                    q.append([j,x,y])
            i=i+2*c
    return nodes[0]
def lastorder(r):
    if r.child:
        for x in r.child:
            lastorder(x)
    print(r.val,end=' ')
n=int(input())
for i in range(n):
    t=list(input().split())
    k=buildtree(t)#特别注意不能重新写类否则孩子列表将被初始化覆盖
    lastorder(k)
    
```

注意类的实例化问题，不要重复将类实例化否则将对应不同的实例，需要先将类实例化后的结果储存在列表之后直接调用列表中的元素，而不要创建新的实例



24686树的重量

```python
k,n=map(int,input().split())
t=1<<k
f=[0]*t;g=[0]*t;d=[0]*t
for i in range(t-1,0,-1):
    d[i]=1 if 2*i>t-1 else d[i<<1]+1
for _ in range(n):
    a=list(map(int,input().split()))
    if len(a)==2:
        u=a[1]
        s=f[1]
        while u!=1:
            s+=f[u]
            u>>=1
        ans=s*((1<<d[a[1]])-1)+g[a[1]]
        print(ans)
    elif len(a)==3:
        u=a[1]
        w=a[2]*((1<<d[u])-1)
        f[u]+=a[2]
        while u!=1:
            u>>=1
            g[u]+=w
```

挺难的一个题目，用到了懒更新

#### AVL树

一个n层的AVL树至少有几个节点

```python
n=int(input())
dp=[0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]+1
print(dp[n])
```

#### Huffman树计算最小权值路径

```python
from heapq import heappop,heappush,heapify
n=int(input())
ans=0
p=list(map(int,input().split()))
heapify(p)
for i in range(n-1):
    a=heappop(p)
    b=heappop(p)
    c=a+b
    ans+=c
    heappush(p,c)
print(ans)    

```

#### 二叉堆

```python

class Binheap:
    def  __init__(self):
        self.hlist=[0]
        self.size=0
    def percup(self,i):
        while i//2>0:
            if self.hlist[i]<self.hlist[i//2]:
                self.hlist[i],self.hlist[i//2]=self.hlist[i//2],self.hlist[i]
            i=i//2
    def insert(self,k):
        self.hlist.append(k)
        self.size=self.size+1
        self.percup(self.size)
    def percdown(self,i):
        while (i*2)<=self.size:
            mc=self.minchild(i)
            if self.hlist[i]>self.hlist[mc]:
                self.hlist[i],self.hlist[mc]=self.hlist[mc],self.hlist[i]
            i=mc
    def minchild(self,i):
        if i*2+1>self.size:
            return i*2
        else:
            if self.hlist[i*2]<self.hlist[i*2+1]:
                return i*2
            else:
                return i*2+1
    def delmin(self):
        ans=self.hlist[1]
        self.hlist[1]=self.hlist[self.size]
        self.hlist.pop()
        self.size=self.size-1
        self.percdown(1)
        return ans
bh=Binheap()
for i in range(int(input())):
    a=list(map(int,input().split()))
    if a[0]==1:
        bh.insert(a[1])
    else:
        print(bh.delmin())
```



一个印象比较深刻的题目

2775文件结构图

```python
class root:
    def __init__(self,name):
        self.name=name
        self.d=[]
        self.f=[]
    def build(self,s):
        if s[0]=='f':
            self.f.append(s)
        if s[0]=='d':
            di=root(s)
            self.d.append(di)
            while True:
                s=input()
                if s==']':
                    break
                di.build(s)
def pout(r,i=0):
    print('|     '*i+r.name)
    if r.d:
        for x in r.d:
            pout(x,i+1)
    r.f.sort()
    for y in r.f:
        print('|     '*i+y)
x=0
while True:
    s=input()
    if s=='#':
        break
    x+=1
    r=root('ROOT')
    while True:
        r.build(s)
        s=input()
        if s=='*':
            break
    print(f'DATA SET {x}:')
    pout(r,0)
    print()
```

### 数据结构：栈与队列

栈和队列的题目除了单调栈模版题之外一般都是栈和队列以及字典、堆等数据结构的灵活运用，尤其是用两个字典，两个队列，两个堆，两个栈之类的题目

#### 前中后序表达式

24591中序表达式转后序表达式

shunting yard调度场算法

本质其实就是辅助栈

```python
def trans(s):
    op={'+':1,'-':1,'*':2,"/":2}
    stack=[]
    output=[]
    num=''
    for x in s:
        if x.isnumeric() or x=='.':
            num+=x
        else:
            if num:
                number=float(num) if '.' in num else int(num)
                output.append(number)
                num=''
            if x=="(":
                stack.append(x)
            elif x==")":
                while stack and stack[-1]!='(':
                    output.append(stack.pop())
                stack.pop()
            elif x in op:
                while stack and stack[-1] in op and op[x]<=op[stack[-1]]:
                        output.append(stack.pop())
                stack.append(x)
    if num:
        number=float(num) if '.' in num else int(num)
        output.append(number)
        num=''
    while stack:
        output.append(stack.pop())
    return output
n=int(input())
for i in range(n):
    s=input()
    output=trans(s)
    print(' '.join(map(str,output)))
```

24588后序表达式求值

```python
n=int(input())
for i in range(n):
    a=input().split()
    stack=[]
    for x in a:
        if x in {"+","-","*","/"}:
            b=str(stack.pop())
            c=str(stack.pop())
            d=eval(c+x+b)
            stack.append(d)
        else:
            stack.append(float(x))
    print("{:.2f}".format(stack[0]))
        
```

#### 辅助栈

22067快速堆猪

储存一个数值栈和一个最小值栈

```python
stack=[]
fstack=[]
while True:
    try:
        s=input()
        if s=="min":
            if fstack:
                print(fstack[-1])
                
        elif s=="pop":
            if stack:
                a=stack.pop()
                if a==fstack[-1]:
                    fstack.pop()
        else:
            a,b=s.split()
            b=int(b)
            stack.append(b)
            if fstack:
                if b<=fstack[-1]:
                    fstack.append(b)
            else:
                fstack.append(b)
    except EOFError:
        break
```



#### 队列

27925小组队列

```python
from collections import deque
t=int(input())
dic={}
l={}
for i in range(t):
    dic[i]=list(map(int,input().split()))
    for j in range(len(dic[i])):
        l[dic[i][j]]=i
q={}
h=[]
while True:
    s=input()
    if s=="STOP":
        break
    elif s=="DEQUEUE":
        for x in h:
            if q[x]:
                ans=q[x].popleft()
                print(ans)
                break
    else:
        a,b=s.split()
        b=int(b)
        c=l[b]
        if c in q:
            q[c].append(b)
        else:
            h.append(c)
            q[c]=deque([b])
```

字典里面套deque，用外部列表排序

#### 堆

27947

动态中位数

```python
from heapq import *
def minum(data):
    minh=[]
    maxh=[]
    ans=[]
    for i,num in enumerate(data):
        if not maxh or num>=maxh[0]:
            heappush(maxh,num)
        else:
            heappush(minh,-num)
        if len(maxh)-len(minh)>1:
            heappush(minh,-heappop(maxh))
        elif len(minh)>len(maxh):
            heappush(maxh,-heappop(minh))
        if i%2==0:
            ans.append(maxh[0])
    return ans
t=int(input())
for _ in range(t):
    data=list(map(int,input().split()))
    ans=minum(data)
    print(len(ans))
    print(*ans)
    
```

维护一个大根堆和一个小根堆，保持大根堆和小根堆的元素数量差不超过1，从小根堆（大值堆）的堆顶弹出的即为中位数

#### 括号匹配问题3704

```python

lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break
    
ans = []
for s in lines:
    stack = []
    Mark = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
            Mark += ' '
        elif s[i] == ')':
            if len(stack) == 0:
                Mark += '?'
            else:
                Mark += ' '
                stack.pop()
        else:
            Mark += ' '
    
    while(len(stack)):
        Mark[stack[-1]] = '$'
        stack.pop()
    
    print(s)
    print(''.join(map(str, Mark)))
```

### 归并排序

2299 ultra quicksort

```python
from bisect import *
while True:
    n=int(input())
    if n==0:
        break
    a=[]
    res=0
    for i in range(n):
        num=int(input())
        res+=bisect_left(a,num)
        insort_left(a,num)
    ans=n*(n-1)//2-res
    print(ans)
```

```python
def mergesort(arr,temp,left,right):
    if right-left<=1:
        return 0
    mid=(left+right)//2
    num=mergesort(arr,temp,left,mid)+mergesort(arr,temp,mid,right)
    i,j,k=left,mid,left
    while i<mid and j<right:
        if arr[i]<arr[j]:
            temp[k]=arr[i]
            i+=1
        else:
            temp[k]=arr[j]
            num+=mid-i
            j+=1
        k+=1
    while i<mid:
        temp[k]=arr[i]
        i+=1
        k+=1
    while j<right:
        temp[k]=arr[j]
        j+=1
        k+=1
    for i in range(left,right):
        arr[i]=temp[i]
    return num
while True:
    n=int(input())
    if n==0:
        break
    p=[]
    for i in range(n):
        p.append(int(input()))
    temp=[0]*n
    ans=mergesort(p,temp,0,n)
    print(ans)
```

### bisect库



- `bisect(list, value, lo=0, hi=len(list), key=None)`：在有序列表中查找将值插入的位置，并返回该位置的索引，它是 `bisect_right` 的别名。
- `bisect_left(list, value, lo=0, hi=len(list), key=None)`：在有序列表中查找将值插入的位置，并返回左侧的索引（相同值的最左边位置）。
- `bisect_right(list, value, lo=0, hi=len(list), key=None)`：在有序列表中查找将值插入的位置，并返回右侧的索引（相同值的最右边位置）。
- `insort(list, value, lo=0, hi=len(list), key=None)`：将值插入有序列表中的适当位置，它是 `insort_right` 的别名。
