defmodule Prueba do
  def read do
    IO.stream(:stdio, :line)
    |> Stream.map(&String.trim/1)
    |> Enum.map(&String.to_integer/1)
  end
end

Prueba.read()
|> IO.inspect
