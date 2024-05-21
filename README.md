## README
Install this package with `pip install git+https://github.com/fraterenz/theyr`.

Load data using the `Voyage` class, from which we can get the data using the attribute of the class `.df`.
There are two options to do this, both will return a pandas dataframe:
1. load all waypoints from `path2dir`: `voyage.load_all_waypoints(Path(path2dir))`,
2. load one waypoint `mywaypoint.csv`: `my_voyage = voyage.load_voyage(Path("/path2waypoint/mywaypoint.csv"))`,

