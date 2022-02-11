from glob import glob
from os.path import abspath, basename, dirname
from re import sub
from typing import Dict, List, Tuple, TypedDict

from jinja2 import Environment, FileSystemLoader, Template
from requests import Response, Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

cur_dir = dirname(abspath(__file__))
ses = Session()
retry = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
ses.mount('https://', HTTPAdapter(max_retries=retry))


class Problems(TypedDict):
    id: str
    contest_id: str
    title: str


def __gen_urls(n: int) -> tuple:
    if n//26 > 1 and n % 26 == 0:
        idx: str = chr(96 + n//26-1)
    elif n // 26 > 0:
        idx = chr(96 + n//26)
    else:
        idx = ""
    idx += "z" if n % 26 == 0 else chr(96 + n % 26)
    problem_id: str = "typical90_{}".format(idx)
    return (problem_id, "https://atcoder.jp/contests/typical90/tasks/"+problem_id)


def __get_problems() -> Dict[str, Problems]:
    try:
        url: str = "https://kenkoooo.com/atcoder/resources/problems.json"
        resp: Response = ses.request("get", url, timeout=3)
        problems: Dict[str, Problems] = {}
        for d in resp.json():
            if d["contest_id"] == "typical90":
                problems[d["id"]] = d
        return problems
    except Exception:
        raise Exception("Could not get problem title.")


def __builder() -> List[Tuple[int, str, str, str]]:
    items, problems = set([]), __get_problems()
    for p in glob(cur_dir+"/*.py"):
        if basename(__file__) in p:
            continue
        path: str = p.replace(cur_dir, ".")
        n: int = int(sub(r"\D", "", path))
        prob_id, url = __gen_urls(n)
        title: str = problems[prob_id]["title"]
        items.add((n, title, url, path))
    return sorted(list(items))


def __main() -> None:
    env: Environment = Environment(loader=FileSystemLoader(cur_dir+"/templates"))
    template: Template = env.get_template("README.md.j2")
    items: List[Tuple[int, str, str, str]] = __builder()
    ret: str = template.render(items=items)
    with open(cur_dir+"/README.md", "w") as f:
        f.write(ret)


if __name__ == "__main__":
    __main()
