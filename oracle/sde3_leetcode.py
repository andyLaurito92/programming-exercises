"""
Exercises are coming from this page: https://leetcode.com/discuss/post/6682655/oracle-sde3-march-2025-by-anonymous_user-z7mu/
"""

# 1. Reverse a string without using a library
def reverse(astr: str) -> str:
    if astr is None:
        return None
    return ''.join([c for c in reversed(astr)])

assert "aloh" == reverse("hola")
assert "" == reverse("")
assert "epep" == reverse("pepe")
assert reverse(None) is None


# 2. You are given a dependency tree, where you have nested dependencies.
# Implement the code to traverse and print those dependencies, handle version
# conflicts, taking the latest version and printing accordingly.

from typing import Optional
from collections import deque


class DependencyTreeNode:
    def __init__(self, name: str, version:str,
                 dependencies: Optional[tuple['DependencyTreeNode']] = None) -> None:
        self.name = name
        self.version = version # TODO: Add validation if we want to match X.Y.Z version
        self.dependencies = dependencies

    def checkVersionConflict(self):
        version_per_dependency = {}
        version_conflict = False
        def checkConflict(node, level):
            # IMPORTANT If we don't define the nonlocal, then
            # Python creates a local variable version_conflict and
            # the variable I want to update never gets updated!!
            nonlocal version_conflict 
            version = version_per_dependency.get(node.name)
            if version is None:
                version_per_dependency[node.name] = node.version
            elif version != node.version:
                version_conflict = True
                latest_version = version if version > node.version else node.version
                print((f"Conflict with dependecy {node.name}."
                       f" Have both {node.version} and {version}"
                       f" Will keep version {latest_version} which is the latest"))
                version_per_dependency[node.name] = latest_version

        self.bfs(checkConflict)
        if version_conflict:
            print("Conflict found")
        else:
            print("No conflict found")
        
    def bfs(self, func):
        level = 0
        seen = set()
        tosee = deque()
        tosee.append((self, level))
        while len(tosee) > 0:
            curr, level = tosee.popleft()
            func(curr, level)
            seen.add(curr)
            if curr.dependencies is None:
                continue
            for dependency in curr.dependencies:
                if dependency not in seen:
                    tosee.append((dependency, level+1))

    def dfs(self, func, level=0):
        seen = set()
        def dfs_rec(node, level):
            func(node, level)
            if node.dependencies is None:
                return
            for dependency in node.dependencies:
                if dependency not in seen:
                    seen.add(dependency)
                    dfs_rec(dependency, level+1)

        seen.add(self)
        dfs_rec(self, 0)

    def __str__(self):
        if self.dependencies is None:
            return f"{self.name} {self.version}"
        else:
            res = []

            def printnode(node, level):
                res.append("\t"*level)
                res.append(f"{node.name} {node.version} \n")

            self.dfs(printnode)
            return ''.join(res)


dependencyTree = DependencyTreeNode("Pandas", "1.0.0",
                                    (DependencyTreeNode("Numpy", "1.1.1",
                                                        [DependencyTreeNode("matplotlib", "1.1.1")]
                                                        ),
                                     DependencyTreeNode("matplotlib", "1.2.3")
                                    ))

print(dependencyTree)

dependencyTree.checkVersionConflict()



# 3. Create a magic matrix from given number.
# magic matrix - sum(rows) == sum(columns) == sum(diagonal)
def magicmatrix(n: int) -> list[list[int]]:
    
