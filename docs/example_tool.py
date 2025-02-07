# Example tool used with the example notebook
# This is meant to represent an analysis tool that would be stored in another repository.

class exampleTool:
  def __init__(self):
    print('Initialized')

  @classmethod
  def run_sim(self, slew_distance, config=None):

    print(f"Running Simulation with speed of {config["observatory"]["motion"]["slew_avg_speed"] }!")

    slew_time = slew_distance/config["observatory"]["motion"]["slew_avg_speed"] + config["observatory"]["acquisition"]["offset_measure_time_coarse"]

    return slew_time



