defmodule Day1 do
  def read do
    IO.stream(:stdio, :line)
    |> Stream.map(&String.trim/1)
    |> Stream.map(&String.to_integer/1)
    |> Stream.map(&make_fuel/1)
    |> Enum.sum
    |> IO.puts
  end

  def make_fuel(value) do
    make_fuel(value, 0)
  end
  def make_fuel(0, total), do: total
  def make_fuel(value, total) when div(value,3)-2 >= 0 do
    make_fuel(div(value,3)-2, total + div(value,3)-2)
  end
  def make_fuel(_value, total), do: total


end

Day1.read()
