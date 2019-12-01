defmodule Day1 do
  def read do
    IO.stream(:stdio, :line)
    |> Stream.map(&String.trim/1)
    |> Stream.map(&String.to_integer/1)
    |> Stream.map(fn x -> div(x,3)-2 end)
    |> Enum.sum
    |> IO.puts
  end
end

Day1.read()
