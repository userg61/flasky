def trace1(file: object, lineno: object, name: object, pid: object, ppid: object, pr_name: object, dop: object = "") -> object:
    print(f"\t\t\t@#$%| {file} {lineno}\t{name}\tpid={pid} \tparent pid={ppid}\t{pr_name} | {dop}")
    ...


def trace2(file, lineno, name, pid, ppid, pr_name, dop=""):
    print(f"\t\t\t\t@#$%|| {file} {lineno}\t{name}\tpid={pid} \tparent pid={ppid}\t{pr_name} | {dop}")
    ...

