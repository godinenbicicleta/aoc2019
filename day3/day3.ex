defmodule Day3 do
  def read(path) do
    [line1, line2] =path
      |> File.read!()
      |> String.trim()
      |> String.split("\n")
      |> Enum.map(&String.split(&1, ","))

    positions1 = get_positions(line1)
    positions2 = get_positions(line2)

    candidates = MapSet.intersection(
      positions1,
      positions2
    )
    |> MapSet.delete({0,0})

    get_closest(candidates)

  end

  def get_closest(set) do
    Enum.reduce(
      set,
      100000000000 ,
      fn {x,y}, acc ->
        cond do
          abs(x)+abs(y) < acc -> abs(x) + abs(y)
          true -> acc
        end
      end
    )
  end

  def get_positions(line) do
    Enum.reduce(line, [{0,0}], &process_line/2)
    |> MapSet.new
  end

  def process_line(instruction, result) do
    {direction, steps}  = String.split_at(instruction,1)
    add_steps(direction, String.to_integer(steps), result)
  end

  def add_steps(_direction, 0, result ), do: result
  def add_steps("R", steps, result = [{x,y}| _tail] ) do
    add_steps("R", steps-1, [{x+1,y}|result])
  end
  def add_steps("L", steps, result = [{x,y}| _tail] ) do
    add_steps("L", steps-1, [{x-1,y}|result])
  end
  def add_steps("U", steps, result = [{x,y}| _tail] ) do
    add_steps("U", steps-1, [{x,y+1}|result])
  end
  def add_steps("D", steps, result = [{x,y}| _tail] ) do
    add_steps("D", steps-1, [{x,y-1}|result])
  end

end
