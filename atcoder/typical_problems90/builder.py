import re
from collections import defaultdict
from glob import glob
from os.path import abspath, basename, dirname
from re import sub, template

from jinja2 import Environment, FileSystemLoader
from requests import Response, Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

CUR_DIR = dirname(abspath(__file__))
ses = Session()
retry = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
ses.mount('https://', HTTPAdapter(max_retries=retry))


def gen_urls(n: int) -> tuple:
    if n//26 > 1 and n % 26 == 0:
        idx = chr(96 + n//26-1)
    elif n // 26 > 0:
        idx = chr(96 + n//26)
    else:
        idx = ""
    idx += "z" if n % 26 == 0 else chr(96 + n % 26)
    problem_id = "typical90_{}".format(idx)
    return (problem_id, "https://atcoder.jp/contests/typical90/tasks/"+problem_id)


def get_problems() -> dict:
    try:
        url: str = "https://kenkoooo.com/atcoder/resources/problems.json"
        resp: Response = ses.request("get", url, timeout=3)
        problems: dict = defaultdict(dict)
        for d in resp.json():
            if d["contest_id"] != "typical90":
                continue
            problems[d["id"]] = d
        return problems
    except Exception:
        raise Exception("Could not get problem title.")


def main():
    env = Environment(loader=FileSystemLoader(CUR_DIR+"/templates"))
    tmpl = env.get_template("README.md.j2")
    problems = get_problems()
    items = []
    for p in glob(CUR_DIR+"/*.py"):
        if basename(__file__) in p:
            continue
        path = p.replace(CUR_DIR, ".")
        n = int(sub(r"\D", "", path))
        prob_id, url = gen_urls(n)
        title = problems[prob_id]["title"]
        items.append((n, title, url, path))
    items.sort()
    ret = tmpl.render(items=items)
    with open(CUR_DIR+"/README.md", "w") as f:
        f.write(ret)


if __name__ == "__main__":
    main()
