defmodule Day3 do
  def read(path) do
    [line1, line2] =path
      |> File.read!()
      |> String.trim()
      |> String.split("\n")
      |> Enum.map(&String.split(&1, ","))

    positions1 = get_positions(line1)
    positions2 = get_positions(line2)

    map1 = for {x,y,step_num} <- positions1, into: %{} do
      {{x,y},step_num}
    end


    map2 = for {x,y,step_num} <- positions2, Map.has_key?(map1,{x,y}),into: %{} do
      {{x,y},step_num}
    end

    Enum.filter(map1, &Map.has_key?(map2, elem(&1,0)))
    |> Enum.map(fn {key, value} -> {key, value + Map.get(map2, key)} end)
    |> Enum.sort(&(elem(&2,1)>=elem(&1,1)))
    |> Enum.take(1)



  end


  def get_positions(line) do
    Enum.reduce(line, [{0,0,0}], &process_line/2)
    |> Enum.filter(fn {_, _, s} -> s>0 end)
    |> Enum.sort(&(elem(&2,2)>=elem(&1,2)))
  end

  def process_line(instruction, result) do
    {direction, steps}  = String.split_at(instruction,1)
    add_steps(direction, String.to_integer(steps), result)
  end

  def add_steps(_direction, 0, result ), do: result
  def add_steps("R", steps, result = [{x,y,total_steps}| _tail] ) do
    add_steps("R", steps-1, [{x+1,y, total_steps + 1}|result])
  end
  def add_steps("L", steps, result = [{x,y, total_steps}| _tail] ) do
    add_steps("L", steps-1, [{x-1,y, total_steps + 1}|result])
  end
  def add_steps("U", steps, result = [{x,y, total_steps}| _tail] ) do
    add_steps("U", steps-1, [{x,y+1, total_steps + 1}|result])
  end
  def add_steps("D", steps, result = [{x,y, total_steps}| _tail] ) do
    add_steps("D", steps-1, [{x,y-1, total_steps + 1}|result])
  end

end
