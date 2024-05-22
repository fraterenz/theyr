"""Load all the data using `load_all_waypoints`"""

from pathlib import Path
import pandas as pd
import re


VESSELS = {9999982, 9999982}
LOADS = {"Ballast", "Laden"}
TARGET = {"MIN_FUEL", "MIN_TIME"}
GROUPS = ["vessel", "load_cond", "port_dep", "port_arr", "target"]
FILENAME_RE = re.compile(
    r"(\d+)_(Ballast|Laden)_(.+)_to_(.+)_(MIN_FUEL|MIN_TIME)_waypoints.csv"
)


def parse_filename(path: Path):
    # assume 9999982_Ballast_Vera_Cruz_to_Nouadhibou_MIN_FUEL_waypoints.csv
    assert path.suffix == ".csv", f"should be csv found {path.suffix}"
    name = path.name
    try:
        groups = {k: v for k, v in zip(GROUPS, FILENAME_RE.match(name).groups())}
    except AttributeError as e:
        print(f"failed to load {path}")
        raise e
    assert len(groups) == len(GROUPS)

    return groups


def load_csv(path: Path):
    df = pd.read_csv(path, sep=",", index_col=False)
    df["wavePeriod [s]"] = df["wavePeriod [s]"].astype(int)
    # all waypoints that have distance gr than 100 km
    df["isOcean"] = df["distance [NM]"] > 54
    df["filename"] = path.name
    return df


def load_voyage(path: Path) -> pd.DataFrame:
    assert isinstance(path, Path), f"path should be a Path found {type(path)}"
    df = load_csv(path)
    info = parse_filename(path)
    df["port_dep"] = info["port_dep"]
    df["port_arr"] = info["port_arr"]
    df["vessel"] = info["vessel"]
    df.vessel = df.vessel.astype("category")
    df["load_cond"] = info["load_cond"]
    df.load_cond = df.load_cond.astype("category")
    df["target"] = info["target"]
    df.target = df.target.astype("category")
    return df


def load_all_waypoints(path2dir: Path) -> pd.DataFrame:
    assert isinstance(
        path2dir, Path
    ), f"path2dir should be a Path found {type(path2dir)}"
    assert isinstance(
        path2dir, Path
    ), f"path2dir should be a path to directory found {path2dir}"
    waypoints = [
        load_voyage(x)
        for x in path2dir.iterdir()
        if x.is_file() and "waypoints" in x.name
    ]
    return pd.concat([waypoint for waypoint in waypoints], axis=0)
