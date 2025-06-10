"""
    Description of program: Simple shell program that simulates a file system using a tree with basic commands
    Filename: morgan_simple_shell.py
    Date: 06/10/25
    Course: COMP1353
    Assignment: Project 5 - A Simple Shell (File System Tree) 
    Collaborators: N/A
    Internet Source:stackoverflow.com
"""

import pickle

class TreeNode:
    def __init__(self, name, parent, is_directory):
        self.name = name
        self.children = [] if is_directory else None
        self.parent = parent
        self.is_directory = is_directory
    
    def append_child(self, name, is_directory):
        child = TreeNode(name, self, is_directory)
        if self.children is not None:
            self.children.append(child)
        return child
    
    def is_root(self):
        return self.parent is None
    
    def __str__(self):
        if self.is_directory:
            return f"{self.name} <directory>"
        else:
            return self.name


class FileSystem:
    def __init__(self):
        self.root = TreeNode("", None, True)
        self.current_directory = self.root
    
    def check_make_file(self, name):
        if self.current_directory.children is not None:
            for child in self.current_directory.children:
                if child.name == name:
                    raise ValueError(f"'{name}' already exists")
    
    def ls(self):
        if self.current_directory.children is not None:
            for child in self.current_directory.children:
                print(child)
    
    def mkdir(self, dirname):
        self.check_make_file(dirname)
        self.current_directory.append_child(dirname, True)
    
    def touch(self, name):
        self.check_make_file(name)
        self.current_directory.append_child(name, False)
    
    def cd(self, name):
        if name == "..":
            if not self.current_directory.is_root():
                self.current_directory = self.current_directory.parent
        else:
            if self.current_directory.children is not None:
                for child in self.current_directory.children:
                    if child.name == name and child.is_directory:
                        self.current_directory = child
                        return
            raise ValueError(f"Directory '{name}' not found")
    
    def rm(self, filename):
        if self.current_directory.children is not None:
            for i, child in enumerate(self.current_directory.children):
                if child.name == filename:
                    if child.is_directory:
                        raise ValueError(f"'{filename}' is a directory, use rmdir")
                    self.current_directory.children.pop(i)
                    return
        raise ValueError(f"File '{filename}' not found")
    
    def rmdir(self, dirname):
        if self.current_directory.children is not None:
            for i, child in enumerate(self.current_directory.children):
                if child.name == dirname:
                    if not child.is_directory:
                        raise ValueError(f"'{dirname}' is not a directory")
                    if child.children and len(child.children) > 0:
                        raise ValueError(f"Directory '{dirname}' is not empty")
                    self.current_directory.children.pop(i)
                    return
        raise ValueError(f"Directory '{dirname}' not found")
    
    def tree(self):
        self._tree_helper(self.current_directory, 0)
    
    def _tree_helper(self, node, level):
        print("\t" * level + str(node))
        if node.children is not None:
            for child in node.children:
                self._tree_helper(child, level + 1)
    
    def pwd(self):
        path_parts = []
        current = self.current_directory
        
        while current is not None:
            if current.name != "":
                path_parts.append(current.name)
            current = current.parent
        
        path_parts.reverse()
        if not path_parts:
            print("/")
        else:
            print("/" + "/".join(path_parts) + "/")


def main():
    try:
        with open("file_system.bin", "rb") as file_source:
            file_system = pickle.load(file_source)
            print("File System loaded")
    except:
        print("Creating a new file system: file doesn't exist or data file is out of date because FileSystem class changed")
        file_system = FileSystem()
    
    while True:
        command = input("$ ").strip().split()
        if not command:
            continue
        
        cmd = command[0]
        
        if cmd == "quit":
            break
        
        if cmd == "ls":
            file_system.ls()
        
        if cmd == "pwd":
            file_system.pwd()
        
        if cmd == "tree":
            file_system.tree()
        
        if cmd == "cd":
            try:
                file_system.cd(command[1])
            except:
                print("Error with cd command")
        
        if cmd == "mkdir":
            try:
                file_system.mkdir(command[1])
            except:
                print("Error creating directory")
        
        if cmd == "touch":
            try:
                file_system.touch(command[1])
            except:
                print("Error creating file")
        
        if cmd == "rm":
            try:
                file_system.rm(command[1])
            except:
                print("Error removing file")
        
        if cmd == "rmdir":
            try:
                file_system.rmdir(command[1])
            except:
                print("Error removing directory")
    
    with open("file_system.bin", "wb") as file_destination:
        pickle.dump(file_system, file_destination)
        print("File system saved")


if __name__ == "__main__":
    main()