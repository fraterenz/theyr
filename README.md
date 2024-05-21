## README

Load data using the `Voyage` class, from which we can get the data using the attribute of the class `.df`.
There are two options to do this:
1. Load all waypoints from `path2dir`: `load_all_waypoints(Path(path2dir))`, returns a list of `Voyage`s.
2. Load one waypoint `mywaypoint.csv`: `my_voyage = load_voyage(Path("/path2waypoint/mywaypoint.csv"))`, return an instance of `Voyage`.

