defmodule Day2 do
  def read do
    nums =
      File.read!("input.txt")
      |> String.trim()
      |> String.split(",")
      |> Enum.map(&String.to_integer/1)

    process({:ok, nums, 0})
    |> IO.inspect()
  end

  def test do
    nums = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]

    process({:ok, nums, 0})
    |> IO.inspect()
  end

  defp process({:ok, nums, index}) do
    [code, pos1, pos2, pos3] = Enum.slice(nums, index, 4)

    case code do
      1 -> {:ok, sum(pos1, pos2, pos3, nums), index + 4}
      2 -> {:ok, multiply(pos1, pos2, pos3, nums), index + 4}
      99 -> {:stop, nums}
    end
    |> process
  end

  defp process({:stop, nums}) do
    nums
  end

  defp sum(pos1, pos2, pos3, nums) do
    List.replace_at(nums, pos3, Enum.at(nums, pos1) + Enum.at(nums, pos2))
  end

  defp multiply(pos1, pos2, pos3, nums) do
    List.replace_at(nums, pos3, Enum.at(nums, pos1) * Enum.at(nums, pos2))
  end
end

Day2.test()
Day2.read()
